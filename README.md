# ⚡ GPU Mining Overclock Database (全网显卡跨平台超频静态数据库)

> 基于 HiveOS 官方全网矿机真实大数据驱动，全面收录主流 NVIDIA & AMD 显卡，并已全自动完成 **Linux (HiveOS) ➔ Windows (MSI Afterburner / 内核批处理参数)** 换算。
> **收录显卡总数**: `89` 款 | **最后自动同步**: `2026-11-12 07:31:15 UTC`

## 💡 跨平台换算说明
- **显存频率（N卡）**：HiveOS 填传输速率，Windows 显存显示基准频率，**在 Windows 下已自动除以 2**，避免直接照抄导致驱动崩溃。
- **功耗限制**：HiveOS 是绝对瓦数（W），Windows 微星小飞机是百分比（%），已根据各显卡出厂 TDP 自动计算好百分比。
- **挖矿内核直连**：每个配置均附带 `--lock-cclock / --mclock / --pl`，可直接复制进 Windows `.bat` 脚本。

---

## 🟢 NVIDIA 显卡超频推荐

### 🎮 GeForce RTX 3070
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 120 / Mem: 2300 / PL: 150W | Core: +120 / Mem: +1150 / PL: 68% | `--cclock +120 --mclock +1150 --pl 150` | 50.0% (1人) |
| **RVN (Ravencoin)** | Core: - / Mem: 1000 / PL: 150W | Core: +0 / Mem: +500 / PL: 68% | `--mclock +500 --pl 150` | 6.7% (2人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 68% | `--cclock +200 --pl 150` | 1.5% (64人) |
| **DNX (Dynex)** | Core: 200 / Mem: 0 / PL: 150W | Core: +200 / Mem: +0 / PL: 68% | `--cclock +200 --pl 150` | 0.2% (10人) |
| **CFX (Conflux)** | Core: 100 / Mem: 500 / PL: 180W | Core: +100 / Mem: +250 / PL: 82% | `--cclock +100 --mclock +250 --pl 180` | 3.3% (1人) |
| **NEXA (Nexa)** | Core: - / Mem: 2100 / PL: 150W | Core: +0 / Mem: +1050 / PL: 68% | `--mclock +1050 --pl 150` | 13.3% (4人) |
| **RXD (Radiant)** | Core: 200 / Mem: 2200 / PL: 145W | Core: +200 / Mem: +1100 / PL: 66% | `--cclock +200 --mclock +1100 --pl 145` | 0.0% (1人) |
| **CLORE / NEOX** | Core: - / Mem: 1000 / PL: 150W | Core: +0 / Mem: +500 / PL: 68% | `--mclock +500 --pl 150` | 6.7% (2人) |

### 🎮 CMP 50HX
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 255 / Mem: 0 / PL: -W | Core: +255 / Mem: +0 / PL: 默认 | `--cclock +255` | 0.2% (3人) |
| **RVN (Ravencoin)** | Core: 270 / Mem: 0 / PL: -W | Core: +270 / Mem: +0 / PL: 默认 | `--cclock +270` | 0.4% (5人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 80W | Core: +200 / Mem: +0 / PL: 40% | `--cclock +200 --pl 80` | 0.1% (2人) |
| **CFX (Conflux)** | Core: 280 / Mem: - / PL: 150W | Core: +280 / Mem: +0 / PL: 75% | `--cclock +280 --pl 150` | 0.6% (8人) |
| **NEXA (Nexa)** | Core: 215 / Mem: 1400 / PL: 215W | Core: +215 / Mem: +700 / PL: 108% | `--cclock +215 --mclock +700 --pl 215` | 0.4% (6人) |
| **RXD (Radiant)** | Core: 255 / Mem: - / PL: 145W | Core: +255 / Mem: +0 / PL: 72% | `--cclock +255 --pl 145` | 0.2% (3人) |
| **CLORE / NEOX** | Core: 270 / Mem: 0 / PL: -W | Core: +270 / Mem: +0 / PL: 默认 | `--cclock +270` | 0.4% (5人) |

### 🎮 CMP 30HX
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 100 / Mem: - / PL: 70W | Core: +100 / Mem: +0 / PL: 35% | `--cclock +100 --pl 70` | 1.0% (8人) |
| **RVN (Ravencoin)** | Core: 90 / Mem: - / PL: 125W | Core: +90 / Mem: +0 / PL: 62% | `--cclock +90 --pl 125` | 1.0% (8人) |
| **ERG (Ergo)** | Core: 175 / Mem: - / PL: -W | Core: +175 / Mem: +0 / PL: 默认 | `--cclock +175` | 0.1% (1人) |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 62% | `--pl 125` | 1.4% (11人) |
| **CLORE / NEOX** | Core: 90 / Mem: - / PL: 125W | Core: +90 / Mem: +0 / PL: 62% | `--cclock +90 --pl 125` | 1.0% (8人) |

### 🎮 GeForce RTX 5060 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 350 / Mem: 0 / PL: 0W | Core: +350 / Mem: +0 / PL: 默认 | `--cclock +350` | 0.8% (6人) |
| **RVN (Ravencoin)** | Core: 300 / Mem: 3000 / PL: 150W | Core: +300 / Mem: +1500 / PL: 75% | `--cclock +300 --mclock +1500 --pl 150` | 5.2% (4人) |
| **ERG (Ergo)** | Core: 0 / Mem: 1620 / PL: 150W | Core: +0 / Mem: +810 / PL: 75% | `--mclock +810 --pl 150` | 1.3% (1人) |
| **DNX (Dynex)** | Core: 0 / Mem: - / PL: 140W | Core: +0 / Mem: +0 / PL: 70% | `--pl 140` | 0.1% (1人) |
| **CFX (Conflux)** | Core: 280 / Mem: - / PL: 150W | Core: +280 / Mem: +0 / PL: 75% | `--cclock +280 --pl 150` | 1.1% (8人) |
| **NEXA (Nexa)** | Core: 300 / Mem: - / PL: 160W | Core: +300 / Mem: +0 / PL: 80% | `--cclock +300 --pl 160` | 3.9% (3人) |
| **CLORE / NEOX** | Core: 300 / Mem: 3000 / PL: 150W | Core: +300 / Mem: +1500 / PL: 75% | `--cclock +300 --mclock +1500 --pl 150` | 5.2% (4人) |

### 🎮 CMP 40HX
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 0 / Mem: 0 / PL: 175W | Core: +0 / Mem: +0 / PL: 88% | `--pl 175` | 1.0% (2人) |
| **RVN (Ravencoin)** | Core: 90 / Mem: - / PL: 125W | Core: +90 / Mem: +0 / PL: 62% | `--cclock +90 --pl 125` | 3.9% (8人) |
| **ERG (Ergo)** | Core: 0 / Mem: - / PL: -W | Core: +0 / Mem: +0 / PL: 默认 | 默认 | 3.4% (7人) |
| **CLORE / NEOX** | Core: 90 / Mem: - / PL: 125W | Core: +90 / Mem: +0 / PL: 62% | `--cclock +90 --pl 125` | 3.9% (8人) |

### 🎮 GeForce RTX 3080
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 250 / Mem: 0 / PL: 300W | Core: +250 / Mem: +0 / PL: 94% | `--cclock +250 --pl 300` | 0.9% (17人) |
| **RVN (Ravencoin)** | Core: 100 / Mem: 2000 / PL: 260W | Core: +100 / Mem: +1000 / PL: 81% | `--cclock +100 --mclock +1000 --pl 260` | 1.8% (1人) |
| **ERG (Ergo)** | Core: 150 / Mem: - / PL: 300W | Core: +150 / Mem: +0 / PL: 94% | `--cclock +150 --pl 300` | 3.6% (2人) |
| **DNX (Dynex)** | Core: 200 / Mem: - / PL: 250W | Core: +200 / Mem: +0 / PL: 78% | `--cclock +200 --pl 250` | 7.3% (4人) |
| **CFX (Conflux)** | Core: 100 / Mem: 500 / PL: 250W | Core: +100 / Mem: +250 / PL: 78% | `--cclock +100 --mclock +250 --pl 250` | 20.0% (1人) |
| **NEXA (Nexa)** | Core: 135 / Mem: -1800 / PL: 190W | Core: +135 / Mem: -900 / PL: 59% | `--cclock +135 --mclock -900 --pl 190` | 0.4% (8人) |
| **CLORE / NEOX** | Core: 100 / Mem: 2000 / PL: 260W | Core: +100 / Mem: +1000 / PL: 81% | `--cclock +100 --mclock +1000 --pl 260` | 1.8% (1人) |

### 🎮 GeForce RTX 3060 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 100 / Mem: 950 / PL: 130W | Core: +100 / Mem: +475 / PL: 65% | `--cclock +100 --mclock +475 --pl 130` | 8.3% (1人) |
| **RVN (Ravencoin)** | Core: 150 / Mem: 810 / PL: 150W | Core: +150 / Mem: +405 / PL: 75% | `--cclock +150 --mclock +405 --pl 150` | 0.7% (17人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 75% | `--cclock +200 --pl 150` | 1.2% (32人) |
| **DNX (Dynex)** | Core: 150 / Mem: 0 / PL: 145W | Core: +150 / Mem: +0 / PL: 72% | `--cclock +150 --pl 145` | 0.3% (9人) |
| **CFX (Conflux)** | Core: 0 / Mem: 2000 / PL: 150W | Core: +0 / Mem: +1000 / PL: 75% | `--mclock +1000 --pl 150` | 0.3% (7人) |
| **NEXA (Nexa)** | Core: 135 / Mem: -2000 / PL: 140W | Core: +135 / Mem: -1000 / PL: 70% | `--cclock +135 --mclock -1000 --pl 140` | 0.7% (17人) |
| **RXD (Radiant)** | Core: 200 / Mem: 2200 / PL: 125W | Core: +200 / Mem: +1100 / PL: 62% | `--cclock +200 --mclock +1100 --pl 125` | 0.0% (1人) |
| **CLORE / NEOX** | Core: 150 / Mem: 810 / PL: 150W | Core: +150 / Mem: +405 / PL: 75% | `--cclock +150 --mclock +405 --pl 150` | 0.7% (17人) |

### 🎮 CMP 90HX
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 190 / Mem: -2000 / PL: 235W | Core: +190 / Mem: -1000 / PL: 118% | `--cclock +190 --mclock -1000 --pl 235` | 0.2% (1人) |
| **RVN (Ravencoin)** | Core: 285 / Mem: -2000 / PL: -W | Core: +285 / Mem: -1000 / PL: 默认 | `--cclock +285 --mclock -1000` | 2.7% (15人) |
| **ERG (Ergo)** | Core: - / Mem: 1800 / PL: 170W | Core: +0 / Mem: +900 / PL: 85% | `--mclock +900 --pl 170` | 1.1% (6人) |
| **DNX (Dynex)** | Core: 250 / Mem: -2000 / PL: 190W | Core: +250 / Mem: -1000 / PL: 95% | `--cclock +250 --mclock -1000 --pl 190` | 3.9% (22人) |
| **CFX (Conflux)** | Core: - / Mem: -2000 / PL: 170W | Core: +0 / Mem: -1000 / PL: 85% | `--mclock -1000 --pl 170` | 0.5% (3人) |
| **CLORE / NEOX** | Core: 285 / Mem: -2000 / PL: -W | Core: +285 / Mem: -1000 / PL: 默认 | `--cclock +285 --mclock -1000` | 2.7% (15人) |

### 🎮 GeForce RTX 3070 Laptop GPU
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 150 / Mem: 1500 / PL: 0W | Core: +150 / Mem: +750 / PL: 默认 | `--cclock +150 --mclock +750` | 0.2% (2人) |
| **RVN (Ravencoin)** | Core: 200 / Mem: - / PL: 115W | Core: +200 / Mem: +0 / PL: 57% | `--cclock +200 --pl 115` | 1.2% (16人) |
| **ERG (Ergo)** | Core: 0 / Mem: - / PL: -W | Core: +0 / Mem: +0 / PL: 默认 | 默认 | 1.5% (20人) |
| **DNX (Dynex)** | Core: 190 / Mem: 3100 / PL: -W | Core: +190 / Mem: +1550 / PL: 默认 | `--cclock +190 --mclock +1550` | 0.2% (2人) |
| **CFX (Conflux)** | Core: 195 / Mem: - / PL: -W | Core: +195 / Mem: +0 / PL: 默认 | `--cclock +195` | 2.9% (38人) |
| **CLORE / NEOX** | Core: 200 / Mem: - / PL: 115W | Core: +200 / Mem: +0 / PL: 57% | `--cclock +200 --pl 115` | 1.2% (16人) |

### 🎮 GeForce RTX 3060
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 120 / Mem: 1800 / PL: 130W | Core: +120 / Mem: +900 / PL: 76% | `--cclock +120 --mclock +900 --pl 130` | 5.0% (1人) |
| **RVN (Ravencoin)** | Core: 1 / Mem: 1650 / PL: 145W | Core: +1 / Mem: +825 / PL: 85% | `--cclock +1 --mclock +825 --pl 145` | 25.0% (1人) |
| **ERG (Ergo)** | Core: 175 / Mem: - / PL: -W | Core: +175 / Mem: +0 / PL: 默认 | `--cclock +175` | 1.0% (12人) |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 74% | `--pl 125` | 0.4% (5人) |
| **CFX (Conflux)** | Core: - / Mem: 900 / PL: 125W | Core: +0 / Mem: +450 / PL: 74% | `--mclock +450 --pl 125` | 1.8% (22人) |
| **NEXA (Nexa)** | Core: 100 / Mem: -2000 / PL: 130W | Core: +100 / Mem: -1000 / PL: 76% | `--cclock +100 --mclock -1000 --pl 130` | 1.3% (16人) |
| **RXD (Radiant)** | Core: 255 / Mem: - / PL: 140W | Core: +255 / Mem: +0 / PL: 82% | `--cclock +255 --pl 140` | 0.2% (2人) |
| **CLORE / NEOX** | Core: 1 / Mem: 1650 / PL: 145W | Core: +1 / Mem: +825 / PL: 85% | `--cclock +1 --mclock +825 --pl 145` | 25.0% (1人) |

### 🎮 GeForce RTX 4060 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 200 / Mem: - / PL: 136W | Core: +200 / Mem: +0 / PL: 85% | `--cclock +200 --pl 136` | 2.0% (3人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 94% | `--cclock +200 --pl 150` | 3.4% (5人) |
| **DNX (Dynex)** | Core: 200 / Mem: 0 / PL: 150W | Core: +200 / Mem: +0 / PL: 94% | `--cclock +200 --pl 150` | 7.1% (1人) |
| **CLORE / NEOX** | Core: 200 / Mem: - / PL: 136W | Core: +200 / Mem: +0 / PL: 85% | `--cclock +200 --pl 136` | 2.0% (3人) |

### 🎮 GeForce RTX 4070
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 250 / Mem: 810 / PL: 100W | Core: +250 / Mem: +405 / PL: 50% | `--cclock +250 --mclock +405 --pl 100` | 0.5% (1人) |
| **RVN (Ravencoin)** | Core: 2505 / Mem: 1700 / PL: 180W | Core: 2505 (需按Ctrl+F锁频) / Mem: +850 / PL: 90% | `--lock-cclock 2505 --mclock +850 --pl 180` | 4.2% (8人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 75% | `--cclock +200 --pl 150` | 2.1% (4人) |
| **DNX (Dynex)** | Core: 200 / Mem: 0 / PL: 170W | Core: +200 / Mem: +0 / PL: 85% | `--cclock +200 --pl 170` | 1.1% (2人) |
| **CFX (Conflux)** | Core: 200 / Mem: - / PL: 240W | Core: +200 / Mem: +0 / PL: 120% | `--cclock +200 --pl 240` | 5.8% (11人) |
| **NEXA (Nexa)** | Core: 150 / Mem: - / PL: 178W | Core: +150 / Mem: +0 / PL: 89% | `--cclock +150 --pl 178` | 1.6% (3人) |
| **CLORE / NEOX** | Core: 2505 / Mem: 1700 / PL: 180W | Core: 2505 (需按Ctrl+F锁频) / Mem: +850 / PL: 90% | `--lock-cclock 2505 --mclock +850 --pl 180` | 4.2% (8人) |

### 🎮 GeForce RTX 3070 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 250 / Mem: 0 / PL: 220W | Core: +250 / Mem: +0 / PL: 76% | `--cclock +250 --pl 220` | 0.4% (4人) |
| **RVN (Ravencoin)** | Core: - / Mem: 2000 / PL: 175W | Core: +0 / Mem: +1000 / PL: 60% | `--mclock +1000 --pl 175` | 0.6% (6人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 52% | `--cclock +200 --pl 150` | 1.5% (16人) |
| **DNX (Dynex)** | Core: 0 / Mem: - / PL: 200W | Core: +0 / Mem: +0 / PL: 69% | `--pl 200` | 0.4% (4人) |
| **CFX (Conflux)** | Core: 0 / Mem: 1480 / PL: 210W | Core: +0 / Mem: +740 / PL: 72% | `--mclock +740 --pl 210` | 0.2% (2人) |
| **NEXA (Nexa)** | Core: 0 / Mem: 710 / PL: 180W | Core: +0 / Mem: +355 / PL: 62% | `--mclock +355 --pl 180` | 0.1% (1人) |
| **RXD (Radiant)** | Core: -300 / Mem: 1500 / PL: 140W | Core: -300 / Mem: +750 / PL: 48% | `--cclock -300 --mclock +750 --pl 140` | 0.1% (1人) |
| **CLORE / NEOX** | Core: - / Mem: 2000 / PL: 175W | Core: +0 / Mem: +1000 / PL: 60% | `--mclock +1000 --pl 175` | 0.6% (6人) |

### 🎮 GeForce GTX 1660 SUPER
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 100 / Mem: -1004 / PL: 80W | Core: +100 / Mem: -502 / PL: 64% | `--cclock +100 --mclock -502 --pl 80` | 1.4% (14人) |
| **RVN (Ravencoin)** | Core: 175 / Mem: -1004 / PL: 85W | Core: +175 / Mem: -502 / PL: 68% | `--cclock +175 --mclock -502 --pl 85` | 40.0% (4人) |
| **ERG (Ergo)** | Core: 50 / Mem: -1004 / PL: 110W | Core: +50 / Mem: -502 / PL: 88% | `--cclock +50 --mclock -502 --pl 110` | 0.4% (4人) |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 100% | `--pl 125` | 2.2% (21人) |
| **CFX (Conflux)** | Core: 50 / Mem: -2000 / PL: 90W | Core: +50 / Mem: -1000 / PL: 72% | `--cclock +50 --mclock -1000 --pl 90` | 0.3% (3人) |
| **NEXA (Nexa)** | Core: 125 / Mem: - / PL: 100W | Core: +125 / Mem: +0 / PL: 80% | `--cclock +125 --pl 100` | 0.6% (6人) |
| **CLORE / NEOX** | Core: 175 / Mem: -1004 / PL: 85W | Core: +175 / Mem: -502 / PL: 68% | `--cclock +175 --mclock -502 --pl 85` | 40.0% (4人) |

### 🎮 GeForce RTX 3080 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 250 / Mem: 0 / PL: 230W | Core: +250 / Mem: +0 / PL: 66% | `--cclock +250 --pl 230` | 0.3% (2人) |
| **RVN (Ravencoin)** | Core: 200 / Mem: 0 / PL: 0W | Core: +200 / Mem: +0 / PL: 默认 | `--cclock +200` | 0.8% (6人) |
| **ERG (Ergo)** | Core: 150 / Mem: - / PL: 300W | Core: +150 / Mem: +0 / PL: 86% | `--cclock +150 --pl 300` | 2.3% (17人) |
| **DNX (Dynex)** | Core: 200 / Mem: - / PL: 250W | Core: +200 / Mem: +0 / PL: 71% | `--cclock +200 --pl 250` | 1.3% (10人) |
| **CFX (Conflux)** | Core: 0 / Mem: 2600 / PL: 350W | Core: +0 / Mem: +1300 / PL: 100% | `--mclock +1300 --pl 350` | 0.3% (2人) |
| **NEXA (Nexa)** | Core: 225 / Mem: - / PL: 300W | Core: +225 / Mem: +0 / PL: 86% | `--cclock +225 --pl 300` | 1.9% (14人) |
| **CLORE / NEOX** | Core: 200 / Mem: 0 / PL: 0W | Core: +200 / Mem: +0 / PL: 默认 | `--cclock +200` | 0.8% (6人) |

### 🎮 GeForce RTX 5080
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: - / Mem: - / PL: 300W | Core: +0 / Mem: +0 / PL: 150% | `--pl 300` | 1.6% (4人) |
| **ERG (Ergo)** | Core: 499 / Mem: - / PL: 290W | Core: +499 / Mem: +0 / PL: 145% | `--cclock +499 --pl 290` | 1.2% (3人) |
| **CLORE / NEOX** | Core: - / Mem: - / PL: 300W | Core: +0 / Mem: +0 / PL: 150% | `--pl 300` | 1.6% (4人) |

### 🎮 GeForce RTX 4070 SUPER
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: - / Mem: 3000 / PL: 200W | Core: +0 / Mem: +1500 / PL: 91% | `--mclock +1500 --pl 200` | 1.9% (2人) |
| **CFX (Conflux)** | Core: 240 / Mem: - / PL: 210W | Core: +240 / Mem: +0 / PL: 95% | `--cclock +240 --pl 210` | 0.9% (1人) |
| **NEXA (Nexa)** | Core: 320 / Mem: - / PL: 200W | Core: +320 / Mem: +0 / PL: 91% | `--cclock +320 --pl 200` | 1.9% (2人) |
| **CLORE / NEOX** | Core: - / Mem: 3000 / PL: 200W | Core: +0 / Mem: +1500 / PL: 91% | `--mclock +1500 --pl 200` | 1.9% (2人) |

### 🎮 GeForce RTX 5060
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 0 / Mem: 0 / PL: 150W | Core: +0 / Mem: +0 / PL: 75% | `--pl 150` | 1.1% (1人) |
| **CLORE / NEOX** | Core: 0 / Mem: 0 / PL: 150W | Core: +0 / Mem: +0 / PL: 75% | `--pl 150` | 1.1% (1人) |

### 🎮 GeForce RTX 5070
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 350 / Mem: 0 / PL: 0W | Core: +350 / Mem: +0 / PL: 默认 | `--cclock +350` | 0.4% (1人) |
| **RVN (Ravencoin)** | Core: 400 / Mem: - / PL: 240W | Core: +400 / Mem: +0 / PL: 120% | `--cclock +400 --pl 240` | 1.1% (3人) |
| **ERG (Ergo)** | Core: 250 / Mem: - / PL: 210W | Core: +250 / Mem: +0 / PL: 105% | `--cclock +250 --pl 210` | 1.5% (4人) |
| **CFX (Conflux)** | Core: - / Mem: 0 / PL: 200W | Core: +0 / Mem: +0 / PL: 100% | `--pl 200` | 0.7% (2人) |
| **NEXA (Nexa)** | Core: 300 / Mem: - / PL: 160W | Core: +300 / Mem: +0 / PL: 80% | `--cclock +300 --pl 160` | 0.7% (2人) |
| **CLORE / NEOX** | Core: 400 / Mem: - / PL: 240W | Core: +400 / Mem: +0 / PL: 120% | `--cclock +400 --pl 240` | 1.1% (3人) |

### 🎮 GeForce RTX 2060 SUPER
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 80 / Mem: - / PL: -W | Core: +80 / Mem: +0 / PL: 默认 | `--cclock +80` | 0.6% (2人) |
| **RVN (Ravencoin)** | Core: -150 / Mem: 2500 / PL: 140W | Core: -150 / Mem: +1250 / PL: 80% | `--cclock -150 --mclock +1250 --pl 140` | 20.0% (6人) |
| **ERG (Ergo)** | Core: 140 / Mem: -1500 / PL: 130W | Core: +140 / Mem: -750 / PL: 74% | `--cclock +140 --mclock -750 --pl 130` | 0.6% (2人) |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 71% | `--pl 125` | 0.3% (1人) |
| **CFX (Conflux)** | Core: 179 / Mem: 0 / PL: 155W | Core: +179 / Mem: +0 / PL: 89% | `--cclock +179 --pl 155` | 2.0% (7人) |
| **CLORE / NEOX** | Core: -150 / Mem: 2500 / PL: 140W | Core: -150 / Mem: +1250 / PL: 80% | `--cclock -150 --mclock +1250 --pl 140` | 20.0% (6人) |

### 🎮 GeForce RTX 5070 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 350 / Mem: 0 / PL: 0W | Core: +350 / Mem: +0 / PL: 默认 | `--cclock +350` | 0.3% (1人) |
| **RVN (Ravencoin)** | Core: 200 / Mem: 0 / PL: 0W | Core: +200 / Mem: +0 / PL: 默认 | `--cclock +200` | 0.9% (3人) |
| **ERG (Ergo)** | Core: 499 / Mem: - / PL: 290W | Core: +499 / Mem: +0 / PL: 145% | `--cclock +499 --pl 290` | 0.3% (1人) |
| **DNX (Dynex)** | Core: 200 / Mem: - / PL: 250W | Core: +200 / Mem: +0 / PL: 125% | `--cclock +200 --pl 250` | 1.2% (4人) |
| **CFX (Conflux)** | Core: 499 / Mem: - / PL: 280W | Core: +499 / Mem: +0 / PL: 140% | `--cclock +499 --pl 280` | 0.6% (2人) |
| **CLORE / NEOX** | Core: 200 / Mem: 0 / PL: 0W | Core: +200 / Mem: +0 / PL: 默认 | `--cclock +200` | 0.9% (3人) |

### 🎮 GeForce RTX 3090
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 250 / Mem: 0 / PL: 230W | Core: +250 / Mem: +0 / PL: 66% | `--cclock +250 --pl 230` | 1.0% (5人) |
| **RVN (Ravencoin)** | Core: 1400 / Mem: 1000 / PL: 330W | Core: 1400 (需按Ctrl+F锁频) / Mem: +500 / PL: 94% | `--lock-cclock 1400 --mclock +500 --pl 330` | 33.3% (1人) |
| **ERG (Ergo)** | Core: 150 / Mem: - / PL: 300W | Core: +150 / Mem: +0 / PL: 86% | `--cclock +150 --pl 300` | 0.6% (3人) |
| **DNX (Dynex)** | Core: 200 / Mem: - / PL: 250W | Core: +200 / Mem: +0 / PL: 71% | `--cclock +200 --pl 250` | 1.6% (8人) |
| **CFX (Conflux)** | Core: - / Mem: 0 / PL: 200W | Core: +0 / Mem: +0 / PL: 57% | `--pl 200` | 0.6% (3人) |
| **NEXA (Nexa)** | Core: 270 / Mem: - / PL: 185W | Core: +270 / Mem: +0 / PL: 53% | `--cclock +270 --pl 185` | 0.4% (2人) |
| **CLORE / NEOX** | Core: 1400 / Mem: 1000 / PL: 330W | Core: 1400 (需按Ctrl+F锁频) / Mem: +500 / PL: 94% | `--lock-cclock 1400 --mclock +500 --pl 330` | 33.3% (1人) |

### 🎮 GeForce RTX 4070 Ti SUPER
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **CFX (Conflux)** | Core: 195 / Mem: - / PL: 200W | Core: +195 / Mem: +0 / PL: 70% | `--cclock +195 --pl 200` | 0.5% (1人) |

### 🎮 GeForce RTX 4070 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 53% | `--cclock +200 --pl 150` | 3.8% (8人) |
| **DNX (Dynex)** | Core: 0 / Mem: - / PL: 200W | Core: +0 / Mem: +0 / PL: 70% | `--pl 200` | 0.9% (2人) |
| **NEXA (Nexa)** | Core: 300 / Mem: - / PL: 160W | Core: +300 / Mem: +0 / PL: 56% | `--cclock +300 --pl 160` | 0.5% (1人) |

### 🎮 CMP 170HX
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 0 / Mem: 0 / PL: 150W | Core: +0 / Mem: +0 / PL: 75% | `--pl 150` | 33.3% (4人) |
| **CFX (Conflux)** | Core: 50 / Mem: - / PL: 160W | Core: +50 / Mem: +0 / PL: 80% | `--cclock +50 --pl 160` | 2.9% (1人) |
| **CLORE / NEOX** | Core: 0 / Mem: 0 / PL: 150W | Core: +0 / Mem: +0 / PL: 75% | `--pl 150` | 33.3% (4人) |

### 🎮 GeForce RTX 2060
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1100 / Mem: 600 / PL: 125W | Core: 1100 (需按Ctrl+F锁频) / Mem: +300 / PL: 62% | `--lock-cclock 1100 --mclock +300 --pl 125` | 17.9% (12人) |
| **RVN (Ravencoin)** | Core: 100 / Mem: 450 / PL: 125W | Core: +100 / Mem: +225 / PL: 62% | `--cclock +100 --mclock +225 --pl 125` | 100.0% (8人) |
| **ERG (Ergo)** | Core: 0 / Mem: - / PL: -W | Core: +0 / Mem: +0 / PL: 默认 | 默认 | 0.3% (1人) |
| **DNX (Dynex)** | Core: 0 / Mem: - / PL: 150W | Core: +0 / Mem: +0 / PL: 75% | `--pl 150` | 4.5% (3人) |
| **CFX (Conflux)** | Core: - / Mem: 2000 / PL: 120W | Core: +0 / Mem: +1000 / PL: 60% | `--mclock +1000 --pl 120` | 0.3% (1人) |
| **NEXA (Nexa)** | Core: 0 / Mem: 1200 / PL: 125W | Core: +0 / Mem: +600 / PL: 62% | `--mclock +600 --pl 125` | 0.6% (2人) |
| **CLORE / NEOX** | Core: 100 / Mem: 450 / PL: 125W | Core: +100 / Mem: +225 / PL: 62% | `--cclock +100 --mclock +225 --pl 125` | 100.0% (8人) |

### 🎮 GeForce GTX 1660 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 100 / Mem: - / PL: 70W | Core: +100 / Mem: +0 / PL: 58% | `--cclock +100 --pl 70` | 4.7% (18人) |
| **RVN (Ravencoin)** | Core: 100 / Mem: 450 / PL: 125W | Core: +100 / Mem: +225 / PL: 104% | `--cclock +100 --mclock +225 --pl 125` | 2.9% (11人) |
| **ERG (Ergo)** | Core: 90 / Mem: - / PL: 85W | Core: +90 / Mem: +0 / PL: 71% | `--cclock +90 --pl 85` | 1.0% (4人) |
| **DNX (Dynex)** | Core: 50 / Mem: 500 / PL: 90W | Core: +50 / Mem: +250 / PL: 75% | `--cclock +50 --mclock +250 --pl 90` | 0.3% (1人) |
| **CFX (Conflux)** | Core: - / Mem: 0 / PL: 120W | Core: +0 / Mem: +0 / PL: 100% | `--pl 120` | 0.3% (1人) |
| **CLORE / NEOX** | Core: 100 / Mem: 450 / PL: 125W | Core: +100 / Mem: +225 / PL: 104% | `--cclock +100 --mclock +225 --pl 125` | 2.9% (11人) |

### 🎮 P104-100
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 205 / Mem: -2000 / PL: -W | Core: +205 / Mem: -1000 / PL: 默认 | `--cclock +205 --mclock -1000` | 3.7% (7人) |
| **CLORE / NEOX** | Core: 205 / Mem: -2000 / PL: -W | Core: +205 / Mem: -1000 / PL: 默认 | `--cclock +205 --mclock -1000` | 3.7% (7人) |

### 🎮 P106-100
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 80 / Mem: 200 / PL: 60W | Core: +80 / Mem: +100 / PL: 30% | `--cclock +80 --mclock +100 --pl 60` | 9.7% (15人) |
| **RVN (Ravencoin)** | Core: 0 / Mem: 0 / PL: 120W | Core: +0 / Mem: +0 / PL: 60% | `--pl 120` | 33.3% (1人) |
| **CLORE / NEOX** | Core: 0 / Mem: 0 / PL: 120W | Core: +0 / Mem: +0 / PL: 60% | `--pl 120` | 33.3% (1人) |

### 🎮 GeForce RTX 4060
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 200 / Mem: - / PL: 115W | Core: +200 / Mem: +0 / PL: 100% | `--cclock +200 --pl 115` | 2.5% (2人) |
| **ERG (Ergo)** | Core: 0 / Mem: - / PL: -W | Core: +0 / Mem: +0 / PL: 默认 | 默认 | 2.5% (2人) |
| **DNX (Dynex)** | Core: 0 / Mem: - / PL: 140W | Core: +0 / Mem: +0 / PL: 122% | `--pl 140` | 2.5% (2人) |
| **CLORE / NEOX** | Core: 200 / Mem: - / PL: 115W | Core: +200 / Mem: +0 / PL: 100% | `--cclock +200 --pl 115` | 2.5% (2人) |

### 🎮 GeForce RTX 4090
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 330 / Mem: - / PL: 425W | Core: +330 / Mem: +0 / PL: 94% | `--cclock +330 --pl 425` | 0.9% (1人) |
| **ERG (Ergo)** | Core: 300 / Mem: - / PL: 360W | Core: +300 / Mem: +0 / PL: 80% | `--cclock +300 --pl 360` | 0.9% (1人) |
| **CFX (Conflux)** | Core: 250 / Mem: 0 / PL: 350W | Core: +250 / Mem: +0 / PL: 78% | `--cclock +250 --pl 350` | 25.0% (1人) |
| **NEXA (Nexa)** | Core: 200 / Mem: - / PL: 400W | Core: +200 / Mem: +0 / PL: 89% | `--cclock +200 --pl 400` | 25.0% (1人) |
| **CLORE / NEOX** | Core: 330 / Mem: - / PL: 425W | Core: +330 / Mem: +0 / PL: 94% | `--cclock +330 --pl 425` | 0.9% (1人) |

### 🎮 CMP 70HX
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 0 / Mem: 0 / PL: 175W | Core: +0 / Mem: +0 / PL: 88% | `--pl 175` | 1.1% (2人) |
| **RVN (Ravencoin)** | Core: 250 / Mem: 1000 / PL: 105W | Core: +250 / Mem: +500 / PL: 52% | `--cclock +250 --mclock +500 --pl 105` | 0.6% (1人) |
| **ERG (Ergo)** | Core: 1400 / Mem: 1600 / PL: 150W | Core: 1400 (需按Ctrl+F锁频) / Mem: +800 / PL: 75% | `--lock-cclock 1400 --mclock +800 --pl 150` | 1.1% (2人) |
| **DNX (Dynex)** | Core: 150 / Mem: 0 / PL: 170W | Core: +150 / Mem: +0 / PL: 85% | `--cclock +150 --pl 170` | 1.7% (3人) |
| **NEXA (Nexa)** | Core: 300 / Mem: - / PL: 160W | Core: +300 / Mem: +0 / PL: 80% | `--cclock +300 --pl 160` | 0.6% (1人) |
| **CLORE / NEOX** | Core: 250 / Mem: 1000 / PL: 105W | Core: +250 / Mem: +500 / PL: 52% | `--cclock +250 --mclock +500 --pl 105` | 0.6% (1人) |

### 🎮 RTX A2000
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1350 / Mem: 3000 / PL: 0W | Core: 1350 (需按Ctrl+F锁频) / Mem: +1500 / PL: 默认 | `--lock-cclock 1350 --mclock +1500` | 91.7% (11人) |
| **RVN (Ravencoin)** | Core: - / Mem: - / PL: 45W | Core: +0 / Mem: +0 / PL: 22% | `--pl 45` | 1.9% (3人) |
| **DNX (Dynex)** | Core: 260 / Mem: 0 / PL: 60W | Core: +260 / Mem: +0 / PL: 30% | `--cclock +260 --pl 60` | 1.2% (2人) |
| **CLORE / NEOX** | Core: - / Mem: - / PL: 45W | Core: +0 / Mem: +0 / PL: 22% | `--pl 45` | 1.9% (3人) |

### 🎮 GeForce RTX 3060 Laptop GPU
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: - / Mem: 800 / PL: -W | Core: +0 / Mem: +400 / PL: 默认 | `--mclock +400` | 8.2% (8人) |
| **CFX (Conflux)** | Core: 195 / Mem: - / PL: -W | Core: +195 / Mem: +0 / PL: 默认 | `--cclock +195` | 5.2% (5人) |
| **CLORE / NEOX** | Core: - / Mem: 800 / PL: -W | Core: +0 / Mem: +400 / PL: 默认 | `--mclock +400` | 8.2% (8人) |

### 🎮 CMP 100-210
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 150 / Mem: 1800 / PL: 150W | Core: +150 / Mem: +900 / PL: 75% | `--cclock +150 --mclock +900 --pl 150` | 2.6% (2人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 75% | `--cclock +200 --pl 150` | 15.6% (12人) |
| **DNX (Dynex)** | Core: 0 / Mem: - / PL: 150W | Core: +0 / Mem: +0 / PL: 75% | `--pl 150` | 1.3% (1人) |
| **CLORE / NEOX** | Core: 150 / Mem: 1800 / PL: 150W | Core: +150 / Mem: +900 / PL: 75% | `--cclock +150 --mclock +900 --pl 150` | 2.6% (2人) |

### 🎮 GeForce GTX 1070
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: - / Mem: 900 / PL: 120W | Core: +0 / Mem: +450 / PL: 80% | `--mclock +450 --pl 120` | 3.1% (5人) |
| **RVN (Ravencoin)** | Core: 100 / Mem: 500 / PL: 125W | Core: +100 / Mem: +250 / PL: 83% | `--cclock +100 --mclock +250 --pl 125` | 25.0% (1人) |
| **ERG (Ergo)** | Core: 30 / Mem: 300 / PL: 100W | Core: +30 / Mem: +150 / PL: 67% | `--cclock +30 --mclock +150 --pl 100` | 0.6% (1人) |
| **CLORE / NEOX** | Core: 100 / Mem: 500 / PL: 125W | Core: +100 / Mem: +250 / PL: 83% | `--cclock +100 --mclock +250 --pl 125` | 25.0% (1人) |

### 🎮 GeForce RTX 2070 SUPER
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 80 / Mem: - / PL: -W | Core: +80 / Mem: +0 / PL: 默认 | `--cclock +80` | 1.0% (1人) |
| **RVN (Ravencoin)** | Core: 100 / Mem: 1600 / PL: 130W | Core: +100 / Mem: +800 / PL: 60% | `--cclock +100 --mclock +800 --pl 130` | 100.0% (5人) |
| **ERG (Ergo)** | Core: 200 / Mem: - / PL: 150W | Core: +200 / Mem: +0 / PL: 70% | `--cclock +200 --pl 150` | 1.0% (1人) |
| **DNX (Dynex)** | Core: 0 / Mem: - / PL: 150W | Core: +0 / Mem: +0 / PL: 70% | `--pl 150` | 3.8% (4人) |
| **CFX (Conflux)** | Core: 90 / Mem: 2000 / PL: 130W | Core: +90 / Mem: +1000 / PL: 60% | `--cclock +90 --mclock +1000 --pl 130` | 2.9% (3人) |
| **CLORE / NEOX** | Core: 100 / Mem: 1600 / PL: 130W | Core: +100 / Mem: +800 / PL: 60% | `--cclock +100 --mclock +800 --pl 130` | 100.0% (5人) |

### 🎮 GeForce GTX 1080 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: - / Mem: -1250 / PL: 125W | Core: +0 / Mem: -625 / PL: 50% | `--mclock -625 --pl 125` | 1.3% (1人) |
| **RVN (Ravencoin)** | Core: 70 / Mem: 820 / PL: 210W | Core: +70 / Mem: +410 / PL: 84% | `--cclock +70 --mclock +410 --pl 210` | 9.3% (7人) |
| **ERG (Ergo)** | Core: 50 / Mem: 0 / PL: 130W | Core: +50 / Mem: +0 / PL: 52% | `--cclock +50 --pl 130` | 1.3% (1人) |
| **DNX (Dynex)** | Core: 50 / Mem: 200 / PL: 190W | Core: +50 / Mem: +100 / PL: 76% | `--cclock +50 --mclock +100 --pl 190` | 1.3% (1人) |
| **CFX (Conflux)** | Core: 100 / Mem: 500 / PL: 180W | Core: +100 / Mem: +250 / PL: 72% | `--cclock +100 --mclock +250 --pl 180` | 5.3% (4人) |
| **CLORE / NEOX** | Core: 70 / Mem: 820 / PL: 210W | Core: +70 / Mem: +410 / PL: 84% | `--cclock +70 --mclock +410 --pl 210` | 9.3% (7人) |

### 🎮 GeForce RTX 2080 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 250 / Mem: 0 / PL: 270W | Core: +250 / Mem: +0 / PL: 108% | `--cclock +250 --pl 270` | 12.3% (10人) |
| **RVN (Ravencoin)** | Core: 150 / Mem: 1500 / PL: 180W | Core: +150 / Mem: +750 / PL: 72% | `--cclock +150 --mclock +750 --pl 180` | 9.9% (8人) |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 50% | `--pl 125` | 1.2% (1人) |
| **CFX (Conflux)** | Core: 100 / Mem: 200 / PL: 300W | Core: +100 / Mem: +100 / PL: 120% | `--cclock +100 --mclock +100 --pl 300` | 100.0% (2人) |
| **CLORE / NEOX** | Core: 150 / Mem: 1500 / PL: 180W | Core: +150 / Mem: +750 / PL: 72% | `--cclock +150 --mclock +750 --pl 180` | 9.9% (8人) |

### 🎮 GeForce RTX 2070
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 140 / Mem: 2000 / PL: 140W | Core: +140 / Mem: +1000 / PL: 70% | `--cclock +140 --mclock +1000 --pl 140` | 4.4% (2人) |
| **RVN (Ravencoin)** | Core: 125 / Mem: - / PL: 160W | Core: +125 / Mem: +0 / PL: 80% | `--cclock +125 --pl 160` | 2.2% (1人) |
| **ERG (Ergo)** | Core: -302 / Mem: 1800 / PL: 125W | Core: -302 / Mem: +900 / PL: 62% | `--cclock -302 --mclock +900 --pl 125` | 4.4% (2人) |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 62% | `--pl 125` | 6.7% (3人) |
| **CFX (Conflux)** | Core: - / Mem: 0 / PL: 135W | Core: +0 / Mem: +0 / PL: 68% | `--pl 135` | 2.2% (1人) |
| **CLORE / NEOX** | Core: 125 / Mem: - / PL: 160W | Core: +125 / Mem: +0 / PL: 80% | `--cclock +125 --pl 160` | 2.2% (1人) |

### 🎮 GeForce RTX 3080 Laptop GPU
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 250 / Mem: 810 / PL: 90W | Core: +250 / Mem: +405 / PL: 45% | `--cclock +250 --mclock +405 --pl 90` | 1.1% (1人) |
| **RVN (Ravencoin)** | Core: 0 / Mem: 1500 / PL: 0W | Core: +0 / Mem: +750 / PL: 默认 | `--mclock +750` | 2.1% (2人) |
| **CFX (Conflux)** | Core: 195 / Mem: - / PL: -W | Core: +195 / Mem: +0 / PL: 默认 | `--cclock +195` | 1.1% (1人) |
| **CLORE / NEOX** | Core: 0 / Mem: 1500 / PL: 0W | Core: +0 / Mem: +750 / PL: 默认 | `--mclock +750` | 2.1% (2人) |

### 🎮 GeForce RTX 4080
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 100 / Mem: 1600 / PL: 280W | Core: +100 / Mem: +800 / PL: 88% | `--cclock +100 --mclock +800 --pl 280` | 2.3% (1人) |
| **CFX (Conflux)** | Core: 195 / Mem: - / PL: -W | Core: +195 / Mem: +0 / PL: 默认 | `--cclock +195` | 6.8% (3人) |
| **CLORE / NEOX** | Core: 100 / Mem: 1600 / PL: 280W | Core: +100 / Mem: +800 / PL: 88% | `--cclock +100 --mclock +800 --pl 280` | 2.3% (1人) |

### 🎮 GeForce RTX 4080 SUPER
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **DNX (Dynex)** | Core: 260 / Mem: - / PL: 320W | Core: +260 / Mem: +0 / PL: 100% | `--cclock +260 --pl 320` | 2.1% (1人) |
| **NEXA (Nexa)** | Core: 225 / Mem: - / PL: 300W | Core: +225 / Mem: +0 / PL: 94% | `--cclock +225 --pl 300` | 2.1% (1人) |

### 🎮 GeForce GTX 1660
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: -200 / Mem: 1200 / PL: 70W | Core: -200 / Mem: +600 / PL: 35% | `--cclock -200 --mclock +600 --pl 70` | 2.1% (1人) |
| **RVN (Ravencoin)** | Core: 0 / Mem: 1000 / PL: 75W | Core: +0 / Mem: +500 / PL: 38% | `--mclock +500 --pl 75` | 8.3% (4人) |
| **CLORE / NEOX** | Core: 0 / Mem: 1000 / PL: 75W | Core: +0 / Mem: +500 / PL: 38% | `--mclock +500 --pl 75` | 8.3% (4人) |

### 🎮 GeForce RTX 2080 SUPER
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 75 / Mem: 0 / PL: 180W | Core: +75 / Mem: +0 / PL: 72% | `--cclock +75 --pl 180` | 2.7% (1人) |
| **CFX (Conflux)** | Core: 90 / Mem: 2000 / PL: 160W | Core: +90 / Mem: +1000 / PL: 64% | `--cclock +90 --mclock +1000 --pl 160` | 2.7% (1人) |
| **CLORE / NEOX** | Core: 75 / Mem: 0 / PL: 180W | Core: +75 / Mem: +0 / PL: 72% | `--cclock +75 --pl 180` | 2.7% (1人) |

### 🎮 GeForce RTX 2080
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 100 / Mem: 500 / PL: 158W | Core: +100 / Mem: +250 / PL: 79% | `--cclock +100 --mclock +250 --pl 158` | 3.7% (1人) |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 62% | `--pl 125` | 3.7% (1人) |
| **CLORE / NEOX** | Core: 100 / Mem: 500 / PL: 158W | Core: +100 / Mem: +250 / PL: 79% | `--cclock +100 --mclock +250 --pl 158` | 3.7% (1人) |

### 🎮 GeForce GTX 1080
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: - / Mem: 100 / PL: 100W | Core: +0 / Mem: +50 / PL: 50% | `--mclock +50 --pl 100` | 0.7% (1人) |
| **RVN (Ravencoin)** | Core: 90 / Mem: 500 / PL: 130W | Core: +90 / Mem: +250 / PL: 65% | `--cclock +90 --mclock +250 --pl 130` | 14.2% (21人) |
| **ERG (Ergo)** | Core: 90 / Mem: 500 / PL: 120W | Core: +90 / Mem: +250 / PL: 60% | `--cclock +90 --mclock +250 --pl 120` | 2.0% (3人) |
| **CFX (Conflux)** | Core: 125 / Mem: 500 / PL: 90W | Core: +125 / Mem: +250 / PL: 45% | `--cclock +125 --mclock +250 --pl 90` | 14.3% (1人) |
| **CLORE / NEOX** | Core: 90 / Mem: 500 / PL: 130W | Core: +90 / Mem: +250 / PL: 65% | `--cclock +90 --mclock +250 --pl 130` | 14.2% (21人) |

### 🎮 GeForce GTX 1070 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: - / Mem: 1450 / PL: 120W | Core: +0 / Mem: +725 / PL: 60% | `--mclock +725 --pl 120` | 4.2% (2人) |

### 🎮 P102-100
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **DNX (Dynex)** | Core: - / Mem: - / PL: 125W | Core: +0 / Mem: +0 / PL: 62% | `--pl 125` | 38.9% (7人) |

### 🎮 GeForce RTX 3060 LHR
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 150 / Mem: 1200 / PL: 130W | Core: +150 / Mem: +600 / PL: 65% | `--cclock +150 --mclock +600 --pl 130` | 8.3% (1人) |
| **CFX (Conflux)** | Core: 200 / Mem: 2200 / PL: 150W | Core: +200 / Mem: +1100 / PL: 75% | `--cclock +200 --mclock +1100 --pl 150` | 25.0% (3人) |
| **CLORE / NEOX** | Core: 150 / Mem: 1200 / PL: 130W | Core: +150 / Mem: +600 / PL: 65% | `--cclock +150 --mclock +600 --pl 130` | 8.3% (1人) |

### 🎮 GeForce RTX 3060 Ti LHR
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: - / Mem: 950 / PL: 145W | Core: +0 / Mem: +475 / PL: 72% | `--mclock +475 --pl 145` | 5.1% (2人) |
| **ERG (Ergo)** | Core: - / Mem: 1000 / PL: 100W | Core: +0 / Mem: +500 / PL: 50% | `--mclock +500 --pl 100` | 28.2% (11人) |
| **CLORE / NEOX** | Core: - / Mem: 950 / PL: 145W | Core: +0 / Mem: +475 / PL: 72% | `--mclock +475 --pl 145` | 5.1% (2人) |

### 🎮 GeForce RTX 3070 Ti LHR
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1200 / Mem: 2000 / PL: 230W | Core: 1200 (需按Ctrl+F锁频) / Mem: +1000 / PL: 115% | `--lock-cclock 1200 --mclock +1000 --pl 230` | 31.2% (5人) |
| **ERG (Ergo)** | Core: 1540 / Mem: 2600 / PL: 160W | Core: 1540 (需按Ctrl+F锁频) / Mem: +1300 / PL: 80% | `--lock-cclock 1540 --mclock +1300 --pl 160` | 25.0% (4人) |
| **CLORE / NEOX** | Core: 1200 / Mem: 2000 / PL: 230W | Core: 1200 (需按Ctrl+F锁频) / Mem: +1000 / PL: 115% | `--lock-cclock 1200 --mclock +1000 --pl 230` | 31.2% (5人) |

### 🎮 GeForce RTX 3090 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: - / Mem: 1600 / PL: 310W | Core: +0 / Mem: +800 / PL: 69% | `--mclock +800 --pl 310` | 16.7% (1人) |

### 🎮 RTX A5000
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: - / Mem: 1000 / PL: 230W | Core: +0 / Mem: +500 / PL: 115% | `--mclock +500 --pl 230` | 5.7% (2人) |
| **CFX (Conflux)** | Core: 300 / Mem: 2200 / PL: -W | Core: +300 / Mem: +1100 / PL: 默认 | `--cclock +300 --mclock +1100` | 2.9% (1人) |
| **CLORE / NEOX** | Core: - / Mem: 1000 / PL: 230W | Core: +0 / Mem: +500 / PL: 115% | `--mclock +500 --pl 230` | 5.7% (2人) |

### 🎮 GeForce RTX 3050
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 100 / Mem: - / PL: 70W | Core: +100 / Mem: +0 / PL: 35% | `--cclock +100 --pl 70` | 25.0% (1人) |
| **RVN (Ravencoin)** | Core: 200 / Mem: 200 / PL: 110W | Core: +200 / Mem: +100 / PL: 55% | `--cclock +200 --mclock +100 --pl 110` | 25.0% (1人) |
| **DNX (Dynex)** | Core: 100 / Mem: -2000 / PL: 0W | Core: +100 / Mem: -1000 / PL: 默认 | `--cclock +100 --mclock -1000` | 25.0% (1人) |
| **CLORE / NEOX** | Core: 200 / Mem: 200 / PL: 110W | Core: +200 / Mem: +100 / PL: 55% | `--cclock +200 --mclock +100 --pl 110` | 25.0% (1人) |

### 🎮 P106-090
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 140 / Mem: 0 / PL: 75W | Core: +140 / Mem: +0 / PL: 38% | `--cclock +140 --pl 75` | 50.0% (3人) |

### 🎮 Device 2c09
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **CFX (Conflux)** | Core: 400 / Mem: -502 / PL: 175W | Core: +400 / Mem: -251 / PL: 88% | `--cclock +400 --mclock -251 --pl 175` | 100.0% (1人) |

### 🎮 GeForce RTX 3080 Ti LHR
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: - / Mem: 1600 / PL: 280W | Core: +0 / Mem: +800 / PL: 140% | `--mclock +800 --pl 280` | 50.0% (3人) |
| **ERG (Ergo)** | Core: 1700 / Mem: 2200 / PL: 214W | Core: 1700 (需按Ctrl+F锁频) / Mem: +1100 / PL: 107% | `--lock-cclock 1700 --mclock +1100 --pl 214` | 33.3% (2人) |
| **CLORE / NEOX** | Core: - / Mem: 1600 / PL: 280W | Core: +0 / Mem: +800 / PL: 140% | `--mclock +800 --pl 280` | 50.0% (3人) |

### 🎮 GeForce GTX 1050 Ti
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 200 / Mem: 400 / PL: 75W | Core: +200 / Mem: +200 / PL: 38% | `--cclock +200 --mclock +200 --pl 75` | 100.0% (1人) |
| **CLORE / NEOX** | Core: 200 / Mem: 400 / PL: 75W | Core: +200 / Mem: +200 / PL: 38% | `--cclock +200 --mclock +200 --pl 75` | 100.0% (1人) |

### 🎮 GeForce RTX 3080 LHR
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: - / Mem: 2000 / PL: 250W | Core: +0 / Mem: +1000 / PL: 125% | `--mclock +1000 --pl 250` | 100.0% (1人) |
| **CFX (Conflux)** | Core: 1110 / Mem: 2000 / PL: 0W | Core: 1110 (需按Ctrl+F锁频) / Mem: +1000 / PL: 默认 | `--lock-cclock 1110 --mclock +1000` | 28.6% (4人) |
| **CLORE / NEOX** | Core: - / Mem: 2000 / PL: 250W | Core: +0 / Mem: +1000 / PL: 125% | `--mclock +1000 --pl 250` | 100.0% (1人) |

### 🎮 GeForce RTX 3070 LHR
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1455 / Mem: 2000 / PL: 120W | Core: 1455 (需按Ctrl+F锁频) / Mem: +1000 / PL: 60% | `--lock-cclock 1455 --mclock +1000 --pl 120` | 12.5% (1人) |
| **ERG (Ergo)** | Core: - / Mem: 2300 / PL: 110W | Core: +0 / Mem: +1150 / PL: 55% | `--mclock +1150 --pl 110` | 37.5% (3人) |

## 🔴 AMD 显卡超频推荐

### 🎮 Radeon RX 580
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1150 / Mem: 2050 / PL: -W | Core: 1150 (需按Ctrl+F锁频) / Mem: +2050 / PL: 默认 | `--lock-cclock 1150 --mclock +2050` | 1.6% (12人) |
| **RVN (Ravencoin)** | Core: 1100 / Mem: 1500 / PL: -W | Core: 1100 (需按Ctrl+F锁频) / Mem: +1500 / PL: 默认 | `--lock-cclock 1100 --mclock +1500` | 7.0% (52人) |
| **ERG (Ergo)** | Core: 1150 / Mem: 2000 / PL: -W | Core: 1150 (需按Ctrl+F锁频) / Mem: +2000 / PL: 默认 | `--lock-cclock 1150 --mclock +2000` | 1.5% (11人) |
| **DNX (Dynex)** | Core: 1190 / Mem: 1900 / PL: -W | Core: 1190 (需按Ctrl+F锁频) / Mem: +1900 / PL: 默认 | `--lock-cclock 1190 --mclock +1900` | 0.4% (3人) |
| **NEXA (Nexa)** | Core: 1100 / Mem: 1960 / PL: -W | Core: 1100 (需按Ctrl+F锁频) / Mem: +1960 / PL: 默认 | `--lock-cclock 1100 --mclock +1960` | 13.7% (7人) |
| **CLORE / NEOX** | Core: 1100 / Mem: 1500 / PL: -W | Core: 1100 (需按Ctrl+F锁频) / Mem: +1500 / PL: 默认 | `--lock-cclock 1100 --mclock +1500` | 7.0% (52人) |

### 🎮 Radeon RX 5700 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1380 / Mem: 890 / PL: -W | Core: 1380 (需按Ctrl+F锁频) / Mem: +890 / PL: 默认 | `--lock-cclock 1380 --mclock +890` | 1.7% (12人) |
| **RVN (Ravencoin)** | Core: 1400 / Mem: 890 / PL: -W | Core: 1400 (需按Ctrl+F锁频) / Mem: +890 / PL: 默认 | `--lock-cclock 1400 --mclock +890` | 4.2% (30人) |
| **ERG (Ergo)** | Core: 1300 / Mem: 900 / PL: -W | Core: 1300 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1300 --mclock +900` | 0.1% (1人) |
| **DNX (Dynex)** | Core: 1420 / Mem: 890 / PL: -W | Core: 1420 (需按Ctrl+F锁频) / Mem: +890 / PL: 默认 | `--lock-cclock 1420 --mclock +890` | 0.8% (6人) |
| **NEXA (Nexa)** | Core: 1375 / Mem: 875 / PL: -W | Core: 1375 (需按Ctrl+F锁频) / Mem: +875 / PL: 默认 | `--lock-cclock 1375 --mclock +875` | 0.1% (1人) |
| **RXD (Radiant)** | Core: 1380 / Mem: 900 / PL: -W | Core: 1380 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1380 --mclock +900` | 0.1% (1人) |
| **CLORE / NEOX** | Core: 1400 / Mem: 890 / PL: -W | Core: 1400 (需按Ctrl+F锁频) / Mem: +890 / PL: 默认 | `--lock-cclock 1400 --mclock +890` | 4.2% (30人) |

### 🎮 Radeon RX 6700 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1250 / Mem: 1075 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1075 / PL: 默认 | `--lock-cclock 1250 --mclock +1075` | 1.7% (8人) |
| **RVN (Ravencoin)** | Core: 1450 / Mem: 1070 / PL: -W | Core: 1450 (需按Ctrl+F锁频) / Mem: +1070 / PL: 默认 | `--lock-cclock 1450 --mclock +1070` | 2.1% (10人) |
| **ERG (Ergo)** | Core: 1250 / Mem: 1075 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1075 / PL: 默认 | `--lock-cclock 1250 --mclock +1075` | 0.4% (2人) |
| **CFX (Conflux)** | Core: 1540 / Mem: 1075 / PL: -W | Core: 1540 (需按Ctrl+F锁频) / Mem: +1075 / PL: 默认 | `--lock-cclock 1540 --mclock +1075` | 0.2% (1人) |
| **NEXA (Nexa)** | Core: 1350 / Mem: 920 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +920 / PL: 默认 | `--lock-cclock 1350 --mclock +920` | 0.2% (1人) |
| **CLORE / NEOX** | Core: 1450 / Mem: 1070 / PL: -W | Core: 1450 (需按Ctrl+F锁频) / Mem: +1070 / PL: 默认 | `--lock-cclock 1450 --mclock +1070` | 2.1% (10人) |

### 🎮 Radeon RX 6600 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1350 / Mem: 1050 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +1050 / PL: 默认 | `--lock-cclock 1350 --mclock +1050` | 7.4% (28人) |
| **ERG (Ergo)** | Core: 1900 / Mem: 1075 / PL: -W | Core: 1900 (需按Ctrl+F锁频) / Mem: +1075 / PL: 默认 | `--lock-cclock 1900 --mclock +1075` | 0.5% (2人) |
| **DNX (Dynex)** | Core: 1355 / Mem: 1055 / PL: -W | Core: 1355 (需按Ctrl+F锁频) / Mem: +1055 / PL: 默认 | `--lock-cclock 1355 --mclock +1055` | 0.3% (1人) |
| **NEXA (Nexa)** | Core: 1220 / Mem: 1030 / PL: -W | Core: 1220 (需按Ctrl+F锁频) / Mem: +1030 / PL: 默认 | `--lock-cclock 1220 --mclock +1030` | 1.3% (5人) |
| **CLORE / NEOX** | Core: 1350 / Mem: 1050 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +1050 / PL: 默认 | `--lock-cclock 1350 --mclock +1050` | 7.4% (28人) |

### 🎮 Radeon Pro V520
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1600 / Mem: 1200 / PL: -W | Core: 1600 (需按Ctrl+F锁频) / Mem: +1200 / PL: 默认 | `--lock-cclock 1600 --mclock +1200` | 4.4% (10人) |
| **CLORE / NEOX** | Core: 1600 / Mem: 1200 / PL: -W | Core: 1600 (需按Ctrl+F锁频) / Mem: +1200 / PL: 默认 | `--lock-cclock 1600 --mclock +1200` | 4.4% (10人) |

### 🎮 Radeon RX 6600
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1350 / Mem: 800 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +800 / PL: 默认 | `--lock-cclock 1350 --mclock +800` | 0.4% (2人) |
| **RVN (Ravencoin)** | Core: 1150 / Mem: 950 / PL: -W | Core: 1150 (需按Ctrl+F锁频) / Mem: +950 / PL: 默认 | `--lock-cclock 1150 --mclock +950` | 33.3% (2人) |
| **ERG (Ergo)** | Core: 1900 / Mem: 1050 / PL: -W | Core: 1900 (需按Ctrl+F锁频) / Mem: +1050 / PL: 默认 | `--lock-cclock 1900 --mclock +1050` | 0.7% (3人) |
| **DNX (Dynex)** | Core: 1800 / Mem: 920 / PL: -W | Core: 1800 (需按Ctrl+F锁频) / Mem: +920 / PL: 默认 | `--lock-cclock 1800 --mclock +920` | 16.7% (1人) |
| **NEXA (Nexa)** | Core: 1220 / Mem: 1030 / PL: -W | Core: 1220 (需按Ctrl+F锁频) / Mem: +1030 / PL: 默认 | `--lock-cclock 1220 --mclock +1030` | 0.2% (1人) |
| **CLORE / NEOX** | Core: 1150 / Mem: 950 / PL: -W | Core: 1150 (需按Ctrl+F锁频) / Mem: +950 / PL: 默认 | `--lock-cclock 1150 --mclock +950` | 33.3% (2人) |

### 🎮 Radeon RX 570
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1100 / Mem: 2000 / PL: -W | Core: 1100 (需按Ctrl+F锁频) / Mem: +2000 / PL: 默认 | `--lock-cclock 1100 --mclock +2000` | 3.6% (6人) |
| **RVN (Ravencoin)** | Core: 1168 / Mem: 2000 / PL: -W | Core: 1168 (需按Ctrl+F锁频) / Mem: +2000 / PL: 默认 | `--lock-cclock 1168 --mclock +2000` | 100.0% (1人) |
| **ERG (Ergo)** | Core: 1150 / Mem: 2000 / PL: -W | Core: 1150 (需按Ctrl+F锁频) / Mem: +2000 / PL: 默认 | `--lock-cclock 1150 --mclock +2000` | 2.4% (4人) |
| **CLORE / NEOX** | Core: 1168 / Mem: 2000 / PL: -W | Core: 1168 (需按Ctrl+F锁频) / Mem: +2000 / PL: 默认 | `--lock-cclock 1168 --mclock +2000` | 100.0% (1人) |

### 🎮 Radeon RX 6800 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1300 / Mem: 1050 / PL: -W | Core: 1300 (需按Ctrl+F锁频) / Mem: +1050 / PL: 默认 | `--lock-cclock 1300 --mclock +1050` | 4.5% (9人) |
| **ERG (Ergo)** | Core: 0 / Mem: - / PL: -W | Core: +0 / Mem: +0 / PL: 默认 | 默认 | 0.5% (1人) |
| **NEXA (Nexa)** | Core: 1800 / Mem: 1055 / PL: -W | Core: 1800 (需按Ctrl+F锁频) / Mem: +1055 / PL: 默认 | `--lock-cclock 1800 --mclock +1055` | 2.0% (4人) |
| **CLORE / NEOX** | Core: 1300 / Mem: 1050 / PL: -W | Core: 1300 (需按Ctrl+F锁频) / Mem: +1050 / PL: 默认 | `--lock-cclock 1300 --mclock +1050` | 4.5% (9人) |

### 🎮 Radeon RX 470
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1050 / Mem: 1850 / PL: -W | Core: 1050 (需按Ctrl+F锁频) / Mem: +1850 / PL: 默认 | `--lock-cclock 1050 --mclock +1850` | 2.0% (1人) |
| **RVN (Ravencoin)** | Core: 1100 / Mem: 1500 / PL: -W | Core: 1100 (需按Ctrl+F锁频) / Mem: +1500 / PL: 默认 | `--lock-cclock 1100 --mclock +1500` | 13.0% (7人) |
| **ERG (Ergo)** | Core: 1050 / Mem: 1 / PL: -W | Core: 1050 (需按Ctrl+F锁频) / Mem: +1 / PL: 默认 | `--lock-cclock 1050 --mclock +1` | 7.4% (4人) |
| **CLORE / NEOX** | Core: 1100 / Mem: 1500 / PL: -W | Core: 1100 (需按Ctrl+F锁频) / Mem: +1500 / PL: 默认 | `--lock-cclock 1100 --mclock +1500` | 13.0% (7人) |

### 🎮 Radeon RX Vega 56
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1200 / Mem: 800 / PL: -W | Core: 1200 (需按Ctrl+F锁频) / Mem: +800 / PL: 默认 | `--lock-cclock 1200 --mclock +800` | 3.1% (4人) |
| **ERG (Ergo)** | Core: 1269 / Mem: 888 / PL: -W | Core: 1269 (需按Ctrl+F锁频) / Mem: +888 / PL: 默认 | `--lock-cclock 1269 --mclock +888` | 13.0% (17人) |
| **CFX (Conflux)** | Core: 1225 / Mem: - / PL: -W | Core: 1225 (需按Ctrl+F锁频) / Mem: +0 / PL: 默认 | `--lock-cclock 1225` | 3.8% (5人) |
| **CLORE / NEOX** | Core: 1200 / Mem: 800 / PL: -W | Core: 1200 (需按Ctrl+F锁频) / Mem: +800 / PL: 默认 | `--lock-cclock 1200 --mclock +800` | 3.1% (4人) |

### 🎮 Radeon RX 6800
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1250 / Mem: 1055 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1055 / PL: 默认 | `--lock-cclock 1250 --mclock +1055` | 5.8% (8人) |
| **ERG (Ergo)** | Core: 1500 / Mem: 1 / PL: -W | Core: 1500 (需按Ctrl+F锁频) / Mem: +1 / PL: 默认 | `--lock-cclock 1500 --mclock +1` | 6.5% (9人) |
| **CLORE / NEOX** | Core: 1250 / Mem: 1055 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1055 / PL: 默认 | `--lock-cclock 1250 --mclock +1055` | 5.8% (8人) |

### 🎮 Radeon RX 5600 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1350 / Mem: 900 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1350 --mclock +900` | 8.3% (12人) |
| **ERG (Ergo)** | Core: 1300 / Mem: 900 / PL: -W | Core: 1300 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1300 --mclock +900` | 3.5% (5人) |
| **DNX (Dynex)** | Core: 1420 / Mem: 890 / PL: -W | Core: 1420 (需按Ctrl+F锁频) / Mem: +890 / PL: 默认 | `--lock-cclock 1420 --mclock +890` | 1.4% (2人) |
| **CLORE / NEOX** | Core: 1350 / Mem: 900 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1350 --mclock +900` | 8.3% (12人) |

### 🎮 Radeon RX 5700
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1450 / Mem: 1 / PL: -W | Core: 1450 (需按Ctrl+F锁频) / Mem: +1 / PL: 默认 | `--lock-cclock 1450 --mclock +1` | 2.3% (2人) |
| **ERG (Ergo)** | Core: 1300 / Mem: 900 / PL: -W | Core: 1300 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1300 --mclock +900` | 2.3% (2人) |
| **NEXA (Nexa)** | Core: 1375 / Mem: 825 / PL: -W | Core: 1375 (需按Ctrl+F锁频) / Mem: +825 / PL: 默认 | `--lock-cclock 1375 --mclock +825` | 2.3% (2人) |
| **RXD (Radiant)** | Core: 1380 / Mem: 900 / PL: -W | Core: 1380 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1380 --mclock +900` | 3.4% (3人) |
| **CLORE / NEOX** | Core: 1450 / Mem: 1 / PL: -W | Core: 1450 (需按Ctrl+F锁频) / Mem: +1 / PL: 默认 | `--lock-cclock 1450 --mclock +1` | 2.3% (2人) |

### 🎮 Radeon VII
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 860 / Mem: 480 / PL: -W | Core: 860 (需按Ctrl+F锁频) / Mem: +480 / PL: 默认 | `--lock-cclock 860 --mclock +480` | 6.7% (8人) |
| **CLORE / NEOX** | Core: 860 / Mem: 480 / PL: -W | Core: 860 (需按Ctrl+F锁频) / Mem: +480 / PL: 默认 | `--lock-cclock 860 --mclock +480` | 6.7% (8人) |

### 🎮 Radeon RX 6900 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1250 / Mem: 1000 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1000 / PL: 默认 | `--lock-cclock 1250 --mclock +1000` | 1.6% (1人) |
| **CLORE / NEOX** | Core: 1250 / Mem: 1000 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1000 / PL: 默认 | `--lock-cclock 1250 --mclock +1000` | 1.6% (1人) |

### 🎮 Radeon RX 6700
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1570 / Mem: 1010 / PL: -W | Core: 1570 (需按Ctrl+F锁频) / Mem: +1010 / PL: 默认 | `--lock-cclock 1570 --mclock +1010` | 1.3% (1人) |
| **ERG (Ergo)** | Core: 1600 / Mem: 1050 / PL: -W | Core: 1600 (需按Ctrl+F锁频) / Mem: +1050 / PL: 默认 | `--lock-cclock 1600 --mclock +1050` | 11.5% (9人) |
| **CLORE / NEOX** | Core: 1570 / Mem: 1010 / PL: -W | Core: 1570 (需按Ctrl+F锁频) / Mem: +1010 / PL: 默认 | `--lock-cclock 1570 --mclock +1010` | 1.3% (1人) |

### 🎮 Radeon RX 480
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ETC (Ethereum Classic)** | Core: 1150 / Mem: 1950 / PL: -W | Core: 1150 (需按Ctrl+F锁频) / Mem: +1950 / PL: 默认 | `--lock-cclock 1150 --mclock +1950` | 4.8% (2人) |
| **RVN (Ravencoin)** | Core: 850 / Mem: 1970 / PL: -W | Core: 850 (需按Ctrl+F锁频) / Mem: +1970 / PL: 默认 | `--lock-cclock 850 --mclock +1970` | 25.0% (3人) |
| **DNX (Dynex)** | Core: 950 / Mem: 2000 / PL: -W | Core: 950 (需按Ctrl+F锁频) / Mem: +2000 / PL: 默认 | `--lock-cclock 950 --mclock +2000` | 100.0% (1人) |
| **CLORE / NEOX** | Core: 850 / Mem: 1970 / PL: -W | Core: 850 (需按Ctrl+F锁频) / Mem: +1970 / PL: 默认 | `--lock-cclock 850 --mclock +1970` | 25.0% (3人) |

### 🎮 Radeon RX 5500 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 0 / Mem: 790 / PL: -W | Core: +0 / Mem: +790 / PL: 默认 | `--mclock +790` | 6.2% (2人) |
| **ERG (Ergo)** | Core: 1400 / Mem: 930 / PL: -W | Core: 1400 (需按Ctrl+F锁频) / Mem: +930 / PL: 默认 | `--lock-cclock 1400 --mclock +930` | 6.2% (2人) |
| **CLORE / NEOX** | Core: 0 / Mem: 790 / PL: -W | Core: +0 / Mem: +790 / PL: 默认 | `--mclock +790` | 6.2% (2人) |

### 🎮 Radeon RX Vega 64
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1220 / Mem: 945 / PL: -W | Core: 1220 (需按Ctrl+F锁频) / Mem: +945 / PL: 默认 | `--lock-cclock 1220 --mclock +945` | 23.3% (7人) |
| **ERG (Ergo)** | Core: 1300 / Mem: 900 / PL: -W | Core: 1300 (需按Ctrl+F锁频) / Mem: +900 / PL: 默认 | `--lock-cclock 1300 --mclock +900` | 16.7% (5人) |
| **CFX (Conflux)** | Core: 1225 / Mem: - / PL: -W | Core: 1225 (需按Ctrl+F锁频) / Mem: +0 / PL: 默认 | `--lock-cclock 1225` | 3.3% (1人) |
| **CLORE / NEOX** | Core: 1220 / Mem: 945 / PL: -W | Core: 1220 (需按Ctrl+F锁频) / Mem: +945 / PL: 默认 | `--lock-cclock 1220 --mclock +945` | 23.3% (7人) |

### 🎮 Radeon RX 590
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1450 / Mem: - / PL: -W | Core: 1450 (需按Ctrl+F锁频) / Mem: +0 / PL: 默认 | `--lock-cclock 1450` | 4.8% (1人) |
| **CLORE / NEOX** | Core: 1450 / Mem: - / PL: -W | Core: 1450 (需按Ctrl+F锁频) / Mem: +0 / PL: 默认 | `--lock-cclock 1450` | 4.8% (1人) |

### 🎮 Radeon RX 470/480
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1200 / Mem: 1200 / PL: -W | Core: 1200 (需按Ctrl+F锁频) / Mem: +1200 / PL: 默认 | `--lock-cclock 1200 --mclock +1200` | 100.0% (1人) |
| **CLORE / NEOX** | Core: 1200 / Mem: 1200 / PL: -W | Core: 1200 (需按Ctrl+F锁频) / Mem: +1200 / PL: 默认 | `--lock-cclock 1200 --mclock +1200` | 100.0% (1人) |

### 🎮 Radeon RX 6900 XTX
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **ERG (Ergo)** | Core: 1900 / Mem: 1050 / PL: -W | Core: 1900 (需按Ctrl+F锁频) / Mem: +1050 / PL: 默认 | `--lock-cclock 1900 --mclock +1050` | 27.8% (5人) |

### 🎮 Radeon RX 6650 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1350 / Mem: 1175 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +1175 / PL: 默认 | `--lock-cclock 1350 --mclock +1175` | 7.7% (1人) |
| **CLORE / NEOX** | Core: 1350 / Mem: 1175 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +1175 / PL: 默认 | `--lock-cclock 1350 --mclock +1175` | 7.7% (1人) |

### 🎮 Radeon RX 6750 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1350 / Mem: 1150 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +1150 / PL: 默认 | `--lock-cclock 1350 --mclock +1150` | 33.3% (1人) |
| **CLORE / NEOX** | Core: 1350 / Mem: 1150 / PL: -W | Core: 1350 (需按Ctrl+F锁频) / Mem: +1150 / PL: 默认 | `--lock-cclock 1350 --mclock +1150` | 33.3% (1人) |

### 🎮 Radeon RX 6500 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1400 / Mem: 1100 / PL: -W | Core: 1400 (需按Ctrl+F锁频) / Mem: +1100 / PL: 默认 | `--lock-cclock 1400 --mclock +1100` | 100.0% (2人) |
| **CLORE / NEOX** | Core: 1400 / Mem: 1100 / PL: -W | Core: 1400 (需按Ctrl+F锁频) / Mem: +1100 / PL: 默认 | `--lock-cclock 1400 --mclock +1100` | 100.0% (2人) |

### 🎮 Radeon RX 7600
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1250 / Mem: 1100 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1100 / PL: 默认 | `--lock-cclock 1250 --mclock +1100` | 50.0% (1人) |
| **CLORE / NEOX** | Core: 1250 / Mem: 1100 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +1100 / PL: 默认 | `--lock-cclock 1250 --mclock +1100` | 50.0% (1人) |

### 🎮 Radeon RX 7800 XT
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 0 / Mem: 0 / PL: -W | Core: +0 / Mem: +0 / PL: 默认 | 默认 | 100.0% (1人) |
| **CLORE / NEOX** | Core: 0 / Mem: 0 / PL: -W | Core: +0 / Mem: +0 / PL: 默认 | 默认 | 100.0% (1人) |

### 🎮 Radeon RX 6600 series
| 币种 / 算法 | HiveOS (Linux) 参数 | Windows (小飞机) 设置 | Windows 内核 .bat 复制参数 | 矿工推荐度 |
| :--- | :--- | :--- | :--- | :--- |
| **RVN (Ravencoin)** | Core: 1250 / Mem: 950 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +950 / PL: 默认 | `--lock-cclock 1250 --mclock +950` | 33.3% (1人) |
| **CLORE / NEOX** | Core: 1250 / Mem: 950 / PL: -W | Core: 1250 (需按Ctrl+F锁频) / Mem: +950 / PL: 默认 | `--lock-cclock 1250 --mclock +950` | 33.3% (1人) |

## 📦 CDN 免密调用方式
在任意项目、脚本或挖矿客户端中，可直接通过 jsDelivr CDN 免密拉取对应显卡的独立 JSON：
```bash
# 获取单张显卡 JSON (示例)
curl https://cdn.jsdelivr.net/gh/<你的GitHub用户名>/<你的仓库名>@main/presets/nvidia/GeForce_RTX_3070.json
```