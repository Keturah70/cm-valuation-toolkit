"""
CM SYSTEM COMPARISON TOOL
Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
Unified Framework: Bitcoin + Oil + Water
"""

import numpy as np
import matplotlib.pyplot as plt

def compare_cm(bitcoin_cm, oil_cm, water_cm):
    """
    Compare Bitcoin, Oil, and Water as Commodity Money Systems
    
    Parameters:
        bitcoin_cm (tuple): (cm_value, risk_score)
        oil_cm (tuple): (cm_value, sustainability)
        water_cm (tuple): (cm_value, sustainability)
    """
    
    # ===== DATA EXTRACTION =====
    # CM Value Indices
    indices = [bitcoin_cm[0], oil_cm[0], water_cm[0]]
    
    # Risk Scores (Convert Sustainability to Risk)
    risks = [bitcoin_cm[1], 100-oil_cm[1], 100-water_cm[1]]
    
    # ===== VISUALIZATION =====
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle('CM System Comparison - Eniola Framework', fontsize=16, fontweight='bold')
    
    # Value Comparison
    ax1.bar(['Bitcoin', 'Oil', 'Water'], indices, 
            color=['#ff7f0e', '#2f4f4f', '#1e90ff'])
    ax1.set_title('CM Value Comparison')
    ax1.set_ylabel('Index Value')
    ax1.grid(True, alpha=0.3)
    
    # Risk Comparison
    ax2.bar(['Bitcoin', 'Oil', 'Water'], risks, 
            color=['#ff6b6b', '#696969', '#483d8b'])
    ax2.set_title('Risk Comparison')
    ax2.set_ylabel('Risk Score (0-100)')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # ===== ANALYSIS =====
    # Find Best and Worst Systems
    max_idx = np.argmax(indices)
    min_risk_idx = np.argmin(risks)
    
    # ===== CONSOLE OUTPUT =====
    print(f"\n=== CM SYSTEM COMPARISON (Eniola Framework) ===")
    print(f"Highest CM Value: {['Bitcoin','Oil','Water'][max_idx]}")
    print(f"Lowest Risk: {['Bitcoin','Oil','Water'][min_risk_idx]}")
    
    if max_idx == min_risk_idx:
        print(f"CONCLUSION: {['Bitcoin','Oil','Water'][max_idx]} dominates in both value AND stability.")
    else:
        print(f"CONCLUSION: Trade-off detected - {['Bitcoin','Oil','Water'][max_idx]} has higher value but {['Bitcoin','Oil','Water'][min_risk_idx]} is more stable.")
    
    # ===== INVESTMENT INSIGHT =====
    print(f"\nINVESTMENT INSIGHT:")
    print("1. Bitcoin: Digital scarcity premium with volatility risk")
    print("2. Oil: Energy wealth with geopolitical uncertainty")
    print("3. Water: Essential utility with sustainability concerns")