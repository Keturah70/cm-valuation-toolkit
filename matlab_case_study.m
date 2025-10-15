% MATLAB CASE STUDY - CM VALUATION TOOLKIT
% Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
% Unified Framework: Bitcoin + Oil + Water

% ===== BITCOIN ANALYSIS (2024 DATA) =====
fprintf('=== BITCOIN CM ANALYSIS ===\n');
btc_cm = bitcoin_cm(19.5e6, 500, 6.25, 1.2e12);

% ===== OIL ANALYSIS (GLOBAL RESERVES) =====
fprintf('\n=== OIL CM ANALYSIS ===\n');
oil_cm = resource_cm('oil', 1.5e12, 35e9, 80, 40);

% ===== WATER ANALYSIS (GLOBAL FRESHWATER) =====
fprintf('\n=== WATER CM ANALYSIS ===\n');
water_cm = resource_cm('water', 1.4e18, 4e15, 0.005, 0.002);

% ===== SYSTEM COMPARISON =====
fprintf('\n=== CM SYSTEM COMPARISON ===\n');
compare_cm(btc_cm, oil_cm, water_cm);

% ===== INTERPRETATION GUIDE =====
fprintf('\n=== INTERPRETATION GUIDE ===\n');
fprintf('1. High CM Value: Strong monetary properties\n');
fprintf('2. Low Risk Score: Stable, sustainable system\n');
fprintf('3. Trade-offs: Balance value vs stability\n');
fprintf('4. Sustainability: Long-term viability indicator\n');