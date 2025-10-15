"""
OIL/WATER COMMODITY MONEY MODEL
Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
Unified CM Framework: Bitcoin + Oil + Water
"""

import numpy as np
import matplotlib.pyplot as plt

def resource_cm(type, reserves, extraction_rate, price_usd, extraction_cost_usd):
    """
    Oil/Water Commodity Money Analysis
    
    Parameters:
        type (str): 'oil' or 'water'
        reserves (float): Total reserves (barrels for oil, liters for water)
        extraction_rate (float): Annual extraction volume
        price_usd (float): Market price per unit
        extraction_cost_usd (float): Cost to extract per unit
    
    Returns:
        tuple: (cm_value, sustainability)
    """
    
    # ===== CORE METRICS =====
    # Net Value per Unit (Market Price - Extraction Cost)
    net_value_per_unit = price_usd - extraction_cost_usd
    
    # Total Net Value (Reserve-Based Wealth)
    total_net_value = reserves * net_value_per_unit
    
    # Depletion Timeline (Years to Exhaustion)
    depletion_years = reserves / extraction_rate
    
    # CM Value Calculation (Net Value × Scarcity Factor)
    scarcity_factor = 1 / (extraction_rate / reserves)  # Inverse extraction ratio
    cm_value = total_net_value * scarcity_factor / 1e12  # Scaled to trillions
    
    # ===== SUSTAINABILITY ASSESSMENT =====
    if depletion_years > 100:
        sustainability = 90  # Highly Sustainable
    elif depletion_years > 50:
        sustainability = 70  # Sustainable
    elif depletion_years > 20:
        sustainability = 50  # Moderate
    else:
        sustainability = 30  # Unsustainable
    
    # ===== VISUALIZATION =====
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(f'{type.upper()} CM Analysis - Eniola Framework', fontsize=16, fontweight='bold')
    
    # CM Metrics Bar Chart
    ax1.bar(['Total Net Value (T$)', 'CM Value Index'], 
            [total_net_value/1e12, cm_value], 
            color=['#8b4513', '#1e90ff'])
    ax1.set_title(f'{type.upper()} CM Metrics')
    ax1.set_ylabel('Trillion USD')
    ax1.grid(True, alpha=0.3)
    
    # Sustainability Gauge
    ax2.clear()
    theta = np.linspace(0, np.pi, 100)
    r = 1
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Color Zones (Red=High Risk, Yellow=Moderate, Green=Low Risk)
    ax2.fill_between(x[0:30], 0, y[0:30], color='#ff6b6b', alpha=0.7)
    ax2.fill_between(x[30:70], 0, y[30:70], color='#ffd93d', alpha=0.7)
    ax2.fill_between(x[70:], 0, y[70:], color='#6bcf7f', alpha=0.7)
    
    # Needle
    needle_angle = (sustainability/100) * np.pi
    ax2.plot([0, np.cos(needle_angle)], [0, np.sin(needle_angle)], 'k-', lw=3)
    ax2.plot(0, 0, 'ko', markersize=10)
    ax2.set_aspect('equal')
    ax2.set_title('Sustainability Index')
    
    plt.tight_layout()
    plt.show()
    
    # ===== CONSOLE OUTPUT =====
    print(f"\n=== {type.upper()} CM ANALYSIS (Eniola Framework) ===")
    print(f"Total Net Value: ${total_net_value/1e12:.2f} trillion")
    print(f"CM Value Index: {cm_value:.2f}")
    print(f"Years to Depletion: {depletion_years:.1f}")
    print(f"Sustainability: {sustainability:.0f}/100")
    
    # Interpretation
    if sustainability > 70:
        print("Interpretation: Sustainable Resource - Stable CM System")
    elif sustainability > 40:
        print("Interpretation: Moderate Sustainability - Monitor Extraction")
    else:
        print("Interpretation: Unsustainable - High Depletion Risk")
    
    return cm_value, sustainability