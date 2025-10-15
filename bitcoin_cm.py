"""
BITCOIN COMMODITY MONEY MODEL
Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
Unified CM Framework: Bitcoin + Oil + Water
"""

import numpy as np
import matplotlib.pyplot as plt

def bitcoin_cm(current_supply, hashrate_EH, block_reward, market_cap_usd):
    """
    Bitcoin Commodity Money Analysis
    
    Parameters:
        current_supply (float): BTC in circulation (e.g., 19.5e6)
        hashrate_EH (float): Network hashrate in EH/s (e.g., 500)
        block_reward (float): BTC per block (e.g., 6.25)
        market_cap_usd (float): Total market cap in USD (e.g., 1.2e12)
    
    Returns:
        tuple: (cm_value, risk_score)
    """
    
    # ===== CORE METRICS =====
    # Stock-to-Flow Ratio (CM Foundation)
    annual_inflation = block_reward * 144 * 365  # BTC/year
    stf_ratio = current_supply / annual_inflation
    
    # Energy-Security Index (Hashrate as Trust Proxy)
    energy_security = hashrate_EH / 100  # Scaled factor
    
    # CM Value Calculation (S/F × Energy Security × Market Weight)
    cm_value = stf_ratio * energy_security * (market_cap_usd / 1e12)
    
    # ===== RISK ASSESSMENT =====
    # Depletion Risk (Algorithmic Scarcity)
    depletion_risk = (current_supply / 21e6) * 40  # % of total supply mined
    
    # Inflation Risk (Halving-Driven Volatility)
    inflation_risk = (annual_inflation / current_supply) * 100 * 30  # Annual inflation %
    
    # Centralization Risk (Hashrate Distribution)
    centralization_risk = (1 - (hashrate_EH / 1000)) * 30  # Hashrate concentration proxy
    
    # Composite Risk Score (0-100)
    risk_score = depletion_risk + inflation_risk + centralization_risk
    
    # ===== VISUALIZATION =====
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle('Bitcoin CM Analysis - Eniola Framework', fontsize=16, fontweight='bold')
    
    # CM Metrics Bar Chart
    ax1.bar(['S/F Ratio', 'Energy Security', 'CM Value'], 
            [stf_ratio, energy_security, cm_value], 
            color=['#1f77b4', '#2ca02c', '#ff7f0e'])
    ax1.set_title('Bitcoin CM Metrics')
    ax1.set_ylabel('Index Value')
    ax1.grid(True, alpha=0.3)
    
    # Risk Breakdown Pie Chart
    ax2.pie([depletion_risk, inflation_risk, centralization_risk, 100-risk_score],
            labels=['Depletion', 'Inflation', 'Centralization', 'Stable'],
            colors=['#ff6b6b', '#ffd93d', '#6c5ce7', '#6bcf7f'],
            autopct='%1.1f%%')
    ax2.set_title('CM Risk Breakdown')
    
    plt.tight_layout()
    plt.show()
    
    # ===== CONSOLE OUTPUT =====
    print(f"\n=== BITCOIN CM ANALYSIS (Eniola Framework) ===")
    print(f"Stock-to-Flow Ratio: {stf_ratio:.2f}")
    print(f"CM Value Index: {cm_value:.2f}")
    print(f"Risk Score: {risk_score:.1f}/100")
    
    # Interpretation
    if risk_score < 30:
        print("Interpretation: Low Risk - Stable CM System")
    elif risk_score < 60:
        print("Interpretation: Moderate Risk - Monitor Volatility")
    else:
        print("Interpretation: High Risk - Significant Uncertainty")
    
    return cm_value, risk_score