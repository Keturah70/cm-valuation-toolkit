"""
PYTHON CASE STUDY - CM VALUATION TOOLKIT
Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
Unified Framework: Bitcoin + Oil + Water
"""

# Import CM Functions
from bitcoin_cm import bitcoin_cm
from resource_cm import resource_cm
from compare_cm import compare_cm

# ===== BITCOIN ANALYSIS (2024 DATA) =====
print("=== BITCOIN CM ANALYSIS ===")
btc_cm = bitcoin_cm(current_supply=19.5e6, hashrate_EH=500, block_reward=6.25, market_cap_usd=1.2e12)

# ===== OIL ANALYSIS (GLOBAL RESERVES) =====
print("\n=== OIL CM ANALYSIS ===")
oil_cm = resource_cm(type='oil', reserves=1.5e12, extraction_rate=35e9, price_usd=80, extraction_cost_usd=40)

# ===== WATER ANALYSIS (GLOBAL FRESHWATER) =====
print("\n=== WATER CM ANALYSIS ===")
water_cm = resource_cm(type='water', reserves=1.4e18, extraction_rate=4e15, price_usd=0.005, extraction_cost_usd=0.002)

# ===== SYSTEM COMPARISON =====
print("\n=== CM SYSTEM COMPARISON ===")
compare_cm(btc_cm, oil_cm, water_cm)

# ===== INTERPRETATION GUIDE =====
print("\n=== INTERPRETATION GUIDE ===")
print("1. High CM Value: Strong monetary properties")
print("2. Low Risk Score: Stable, sustainable system")
print("3. Trade-offs: Balance value vs stability")
print("4. Sustainability: Long-term viability indicator")