# Commodity Money (CM) Valuation Toolkit v1.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MATLAB](https://img.shields.io/badge/MATLAB-Compatible-blue)](https://mathworks.com/)
[![Python](https://img.shields.io/badge/Python-Compatible-green)](https://python.org/)

> **The world's first unified computational framework for comparing Bitcoin, oil, and water as Commodity Money systems**

## 🎯 What This Toolkit Does

This toolkit provides transparent, computational models to analyze and compare three Commodity Money systems:

| **System** | **Commodity** | **Value Basis** | **Scarcity Mechanism** |
|------------|---------------|-----------------|------------------------|
| Bitcoin    | Digital Asset | Trust/Scarcity | Algorithmic (21M cap) |
| Oil        | Fossil Fuel  | Energy Utility | Geological Reserves |
| Water      | Natural Resource | Survival Utility | Hydrological Cycle |

## 🚀 Quick Start

### MATLAB
```matlab
% Bitcoin Analysis
btc_cm = bitcoin_cm(19.5e6, 500, 6.25, 1.2e12);

% Oil Analysis
oil_cm = resource_cm('oil', 1.5e12, 35e9, 80, 40);

% Water Analysis
water_cm = resource_cm('water', 1.4e18, 4e15, 0.005, 0.002);

% Compare Systems
compare_cm(btc_cm, oil_cm, water_cm);
