# -*- coding: utf-8 -*-
"""
HiveOS 全网全量显卡热门超频参数爬取与 Windows/Linux 跨平台转换引擎
"""

import os
import sys
import re
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(CURRENT_DIR, "config.json")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "presets")


def load_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def clean_gpu_name(raw_name):
    """
    清洗 HiveOS 原始显卡名（去除显存后缀、提取中括号内标准名称）
    例: 'GeForce RTX 3070 8GB' -> 'GeForce RTX 3070'
    例: 'AD104 [GeForce RTX 4070 SUPER]' -> 'GeForce RTX 4070 SUPER'
    """
    n = re.sub(r'\s+\d+(?:GB|MB|G|M)$', '', raw_name, flags=re.I).strip()
    m = re.search(r'\[(.*?)\]', n)
    if m:
        n = m.group(1).strip()
    return n


def fetch_all_gpu_models_from_hive():
    """
    从 HiveOS 全网统计接口自动获取目前在线运行的所有显卡型号 (NVIDIA + AMD)
    """
    url = "https://api2.hiveos.farm/api/v2/hive/stats"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            
            nv_raw = data.get("nvidia_models", [])
            amd_raw = data.get("amd_models", [])
            
            nv_list = []
            seen_nv = set()
            for item in nv_raw:
                clean = clean_gpu_name(item.get("name", ""))
                if clean and clean not in seen_nv:
                    seen_nv.add(clean)
                    nv_list.append({"name": clean, "brand": "nvidia", "share": item.get("amount", 0)})
                    
            amd_list = []
            seen_amd = set()
            for item in amd_raw:
                clean = clean_gpu_name(item.get("name", ""))
                if clean and clean not in seen_amd:
                    seen_amd.add(clean)
                    amd_list.append({"name": clean, "brand": "amd", "share": item.get("amount", 0)})
                    
            return nv_list, amd_list
    except Exception as e:
        print(f"[-] 自动拉取全量显卡列表失败: {e}")
        return [], []


def fetch_presets_from_hive(gpu_model, brand, algo):
    """
    请求 HiveOS 公开超频数据库
    """
    base_url = "https://api2.hiveos.farm/api/v2/hive/overclocks"
    params = {
        "gpu_brand": brand,
        "gpu_model": gpu_model,
        "algo": algo
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("data", [])
    except Exception:
        return []
    return []


def convert_preset(hive_item, brand, tdp):
    """
    将 HiveOS 参数换算为 Windows MSI Afterburner 和通用 Miner 命令行
    """
    cfg = hive_item.get("config", {})
    raw_core = cfg.get("core_clock")
    raw_mem = cfg.get("mem_clock")
    raw_pl = cfg.get("power_limit")
    raw_vddc = cfg.get("core_vddc") or cfg.get("vddc")
    
    # 显存换算 (NVIDIA 在 Windows 下除以 2; AMD 在 Windows 下通常为 1:1)
    if brand == "nvidia":
        win_mem = round(raw_mem / 2) if raw_mem is not None else 0
    else:
        win_mem = raw_mem if raw_mem is not None else 0
        
    is_locked_core = False
    win_core_offset = 0
    win_locked_core = 0
    
    if raw_core is not None:
        if abs(raw_core) >= 500:
            is_locked_core = True
            win_locked_core = raw_core
        else:
            win_core_offset = raw_core
            
    win_pl_percent = None
    if raw_pl is not None and tdp:
        win_pl_percent = round((raw_pl / tdp) * 100)
        
    # 生成挖矿内核通用 .bat 参数
    bat_args = []
    if is_locked_core:
        bat_args.append(f"--lock-cclock {win_locked_core}")
    elif win_core_offset:
        bat_args.append(f"--cclock {win_core_offset:+d}")
        
    if win_mem:
        bat_args.append(f"--mclock {win_mem:+d}")
        
    if raw_pl:
        bat_args.append(f"--pl {raw_pl}")
        
    if raw_vddc:
        bat_args.append(f"--cvddc {raw_vddc}")
        
    bat_cmd = " ".join(bat_args)
    
    return {
        "rating": hive_item.get("rating", 0),
        "miners_count": hive_item.get("cardinality", 0),
        "hiveos_linux": cfg,
        "windows_msi_afterburner": {
            "core_mode": "lock" if is_locked_core else "offset",
            "core_value": f"{win_locked_core} (需按Ctrl+F锁频)" if is_locked_core else f"{win_core_offset:+d}",
            "mem_offset": f"{win_mem:+d}",
            "power_limit_percent": f"{win_pl_percent}%" if win_pl_percent else "默认"
        },
        "windows_miner_bat_args": bat_cmd
    }


def query_single_card(gpu_info, algos, tdp_db):
    name = gpu_info["name"]
    brand = gpu_info["brand"]
    tdp = tdp_db.get(name, 200)
    
    presets = {}
    has_any = False
    for algo_item in algos:
        algo_label = algo_item["name"]
        algo_key = algo_item["algo"]
        
        raw_list = fetch_presets_from_hive(name, brand, algo_key)
        if raw_list:
            best = raw_list[0]
            presets[algo_label] = convert_preset(best, brand, tdp)
            has_any = True
        time.sleep(0.1)  # 避免瞬时打满
        
    return name, brand, tdp, presets, has_any


def generate_readme(all_database):
    readme_path = os.path.join(CURRENT_DIR, "README.md")
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    total_cards = sum(len(cards) for cards in all_database.values())
    
    lines = [
        "# ⚡ GPU Mining Overclock Database (全网显卡跨平台超频静态数据库)",
        "",
        "> 基于 HiveOS 官方全网矿机真实大数据驱动，全面收录主流 NVIDIA & AMD 显卡，并已全自动完成 **Linux (HiveOS) ➔ Windows (MSI Afterburner / 内核批处理参数)** 换算。",
        f"> **收录显卡总数**: `{total_cards}` 款 | **最后自动同步**: `{now_str}`",
        "",
        "## 💡 跨平台换算说明",
        "- **显存频率（N卡）**：HiveOS 填传输速率，Windows 显存显示基准频率，**在 Windows 下已自动除以 2**，避免直接照抄导致驱动崩溃。",
        "- **功耗限制**：HiveOS 是绝对瓦数（W），Windows 微星小飞机是百分比（%），已根据各显卡出厂 TDP 自动计算好百分比。",
        "- **挖矿内核直连**：每个配置均附带 `--lock-cclock / --mclock / --pl`，可直接复制进 Windows `.bat` 脚本。",
        "",
        "---",
        ""
    ]
    
    for brand, cards in all_database.items():
        brand_name = "🟢 NVIDIA" if brand == "nvidia" else "🔴 AMD"
        lines.append(f"## {brand_name} 显卡超频推荐")
        lines.append("")
        
        for gpu_name, data in cards.items():
            presets = data.get("presets", {})
            if not presets:
                continue
                
            lines.append(f"### 🎮 {gpu_name}")
            lines.append("| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |")
            lines.append("| :--- | :--- | :--- | :--- | :--- |")
            
            for algo_label, info in presets.items():
                h = info["hiveos_linux"]
                w = info["windows_msi_afterburner"]
                bat = info["windows_miner_bat_args"]
                rating = f"{info['rating'] * 100:.1f}% ({info['miners_count']}人)"
                
                h_str = f"Core: {h.get('core_clock', '-')} / Mem: {h.get('mem_clock', '-')} / PL: {h.get('power_limit', '-')}W"
                w_str = f"Core: {w['core_value']} / Mem: {w['mem_offset']} / PL: {w['power_limit_percent']}"
                bat_str = f"`{bat}`" if bat else "默认"
                
                lines.append(f"| **{algo_label}** | {h_str} | {w_str} | {bat_str} | {rating} |")
            lines.append("")
            
    lines.append("## 📦 CDN 免密调用方式")
    lines.append("在任意项目、脚本或挖矿客户端中，可直接通过 jsDelivr CDN 免密拉取对应显卡的独立 JSON：")
    lines.append("```bash")
    lines.append("# 获取单张显卡 JSON (示例)")
    lines.append("curl https://cdn.jsdelivr.net/gh/<你的GitHub用户名>/<你的仓库名>@main/presets/nvidia/GeForce_RTX_3070.json")
    lines.append("```")
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\n[+] 成功生成全局说明文档: {readme_path}")


def main():
    print("=" * 65)
    print("🚀 HiveOS GPU 全网全量显卡超频静态数据库生成器")
    print("=" * 65)
    
    cfg = load_config()
    algos = cfg.get("algos", [])
    tdp_db = cfg.get("tdp_database", {})
    auto_all = cfg.get("auto_discover_all_gpus", True)
    
    gpu_queue = []
    
    if auto_all:
        print("[*] 正在从 HiveOS 实时同步全网所有显卡名单 (NVIDIA + AMD) ...")
        nv_models, amd_models = fetch_all_gpu_models_from_hive()
        print(f"[+] 成功发现: NVIDIA 显卡 {len(nv_models)} 款，AMD 显卡 {len(amd_models)} 款")
        gpu_queue.extend(nv_models)
        gpu_queue.extend(amd_models)
    else:
        # 手动列表
        for g in cfg.get("gpus", []):
            brand = "amd" if ("radeon" in g.lower() or "rx " in g.lower()) else "nvidia"
            gpu_queue.append({"name": g, "brand": brand})
            
    print(f"[*] 待处理显卡总数: {len(gpu_queue)} 款，币种算法: {len(algos)} 种")
    print("-" * 65)
    
    os.makedirs(os.path.join(OUTPUT_DIR, "nvidia"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "amd"), exist_ok=True)
    
    all_database = {"nvidia": {}, "amd": {}}
    valid_count = 0
    
    # 采用轻量多线程并发拉取 (4 个 worker，安全防限流)
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(query_single_card, gpu, algos, tdp_db): gpu for gpu in gpu_queue}
        
        idx = 0
        for future in as_completed(futures):
            idx += 1
            name, brand, tdp, presets, has_any = future.result()
            
            status = f"✅ 录入 ({len(presets)} 种算法)" if has_any else "⚪ 暂无预设"
            print(f"[{idx:03d}/{len(gpu_queue):03d}] [{brand.upper():<6}] {name:<35} -> {status}")
            
            if has_any:
                valid_count += 1
                all_database[brand][name] = {
                    "gpu": name,
                    "brand": brand,
                    "tdp": tdp,
                    "presets": presets
                }
                
                # 保存单卡 JSON
                safe_name = name.replace(" ", "_").replace("/", "_")
                card_file = os.path.join(OUTPUT_DIR, brand, f"{safe_name}.json")
                with open(card_file, "w", encoding="utf-8") as f:
                    json.dump({
                        "gpu": name,
                        "brand": brand,
                        "tdp": tdp,
                        "updated_at": datetime.utcnow().isoformat() + "Z",
                        "presets": presets
                    }, f, indent=2, ensure_ascii=False)
                    
    # 保存全网总汇 JSON
    all_file = os.path.join(OUTPUT_DIR, "all_presets.json")
    with open(all_file, "w", encoding="utf-8") as f:
        json.dump({
            "updated_at": datetime.utcnow().isoformat() + "Z",
            "total_gpus": valid_count,
            "database": all_database
        }, f, indent=2, ensure_ascii=False)
    print(f"\n[+] 全量数据已汇总保存至: {all_file}")
    
    # 生成 README.md
    generate_readme(all_database)
    print(f"\n🎉 全量数据库构建完毕！共成功收录并转换 {valid_count} 款主流显卡的真实超频参数！")


if __name__ == "__main__":
    main()
