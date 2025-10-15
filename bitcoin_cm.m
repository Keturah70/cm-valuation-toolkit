function [cm_value, risk_score] = bitcoin_cm(current_supply, hashrate_EH, block_reward, market_cap_usd)
    % BITCOIN COMMODITY MONEY MODEL
    % Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
    % Unified CM Framework: Bitcoin + Oil + Water
    
    % ===== CORE METRICS =====
    % Stock-to-Flow Ratio (CM Foundation)
    annual_inflation = block_reward * 144 * 365; % BTC/year
    stf_ratio = current_supply / annual_inflation;
    
    % Energy-Security Index (Hashrate as Trust Proxy)
    energy_security = hashrate_EH / 100; % Scaled factor
    
    % CM Value Calculation (S/F × Energy Security × Market Weight)
    cm_value = stf_ratio * energy_security * (market_cap_usd / 1e12);
    
    % ===== RISK ASSESSMENT =====
    % Depletion Risk (Algorithmic Scarcity)
    depletion_risk = (current_supply / 21e6) * 40; % % of total supply mined
    
    % Inflation Risk (Halving-Driven Volatility)
    inflation_risk = (annual_inflation / current_supply) * 100 * 30; % Annual inflation %
    
    % Centralization Risk (Hashrate Distribution)
    centralization_risk = (1 - (hashrate_EH / 1000)) * 30; % Hashrate concentration proxy
    
    % Composite Risk Score (0-100)
    risk_score = depletion_risk + inflation_risk + centralization_risk;
    
    % ===== VISUALIZATION =====
    figure('Name', 'Bitcoin CM Analysis', 'Position', [100, 100, 800, 600]);
    
    % CM Metrics Bar Chart
    subplot(2,1,1);
    bar_data = [stf_ratio, energy_security, cm_value];
    bar(bar_data, 'FaceColor', [0.2 0.4 0.8; 0.3 0.7 0.3; 0.9 0.7 0.2]);
    set(gca, 'XTickLabel', {'S/F Ratio', 'Energy Security', 'CM Value'});
    title('Bitcoin CM Metrics - Eniola Framework');
    ylabel('Index Value');
    grid on;
    
    % Risk Breakdown Pie Chart
    subplot(2,1,2);
    pie_data = [depletion_risk, inflation_risk, centralization_risk, 100-risk_score];
    pie_labels = {'Depletion', 'Inflation', 'Centralization', 'Stable'};
    pie(pie_data, pie_labels);
    title('CM Risk Breakdown');
    colormap([1 0.4 0.4; 1 0.8 0.2; 0.6 0.4 0.8; 0.4 0.8 0.4]);
    
    % ===== CONSOLE OUTPUT =====
    fprintf('\n=== BITCOIN CM ANALYSIS (Eniola Framework) ===\n');
    fprintf('Stock-to-Flow Ratio: %.2f\n', stf_ratio);
    fprintf('CM Value Index: %.2f\n', cm_value);
    fprintf('Risk Score: %.1f/100\n', risk_score);
    fprintf('Interpretation: ');
    
    if risk_score < 30
        fprintf('Low Risk - Stable CM System\n');
    elseif risk_score < 60
        fprintf('Moderate Risk - Monitor Volatility\n');
    else
        fprintf('High Risk - Significant Uncertainty\n');
    end
end