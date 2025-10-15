function compare_cm(bitcoin_cm, oil_cm, water_cm)
    % CM SYSTEM COMPARISON TOOL
    % Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
    % Unified Framework: Bitcoin + Oil + Water
    
    % ===== DATA EXTRACTION =====
    % CM Value Indices
    indices = [bitcoin_cm.cm_value, oil_cm.cm_value, water_cm.cm_value];
    
    % Risk Scores (Convert Sustainability to Risk)
    risks = [bitcoin_cm.risk_score, 100-oil_cm.sustainability, 100-water_cm.sustainability];
    
    % ===== VISUALIZATION =====
    figure('Name', 'CM System Comparison', 'Position', [100, 100, 1000, 800]);
    
    % Value Comparison
    subplot(2,1,1);
    bar_data = indices;
    bar(bar_data, 'FaceColor', [0.9 0.5 0.2; 0.2 0.2 0.2; 0.2 0.4 0.8]);
    set(gca, 'XTickLabel', {'Bitcoin', 'Oil', 'Water'});
    title('CM Value Comparison - Eniola Framework');
    ylabel('Index Value');
    grid on;
    
    % Risk Comparison
    subplot(2,1,2);
    bar_data = risks;
    bar(bar_data, 'FaceColor', [0.8 0.2 0.2; 0.5 0.5 0.5; 0.2 0.2 0.6]);
    set(gca, 'XTickLabel', {'Bitcoin', 'Oil', 'Water'});
    title('Risk Comparison - Eniola Framework');
    ylabel('Risk Score (0-100)');
    grid on;
    
    % ===== ANALYSIS =====
    % Find Best and Worst Systems
    [~, max_idx] = max(indices);
    [~, min_risk_idx] = min(risks);
    
    % ===== CONSOLE OUTPUT =====
    fprintf('\n=== CM SYSTEM COMPARISON (Eniola Framework) ===\n');
    fprintf('Highest CM Value: %s\n', {'Bitcoin','Oil','Water'}{max_idx});
    fprintf('Lowest Risk: %s\n', {'Bitcoin','Oil','Water'}{min_risk_idx});
    
    if max_idx == min_risk_idx
        fprintf('CONCLUSION: %s dominates in both value AND stability.\n', ...
            {'Bitcoin','Oil','Water'}{max_idx});
    else
        fprintf('CONCLUSION: Trade-off detected - %s has higher value but %s is more stable.\n', ...
            {'Bitcoin','Oil','Water'}{max_idx}, {'Bitcoin','Oil','Water'}{min_risk_idx});
    end
    
    % ===== INVESTMENT INSIGHT =====
    fprintf('\nINVESTMENT INSIGHT:\n');
    fprintf('1. Bitcoin: Digital scarcity premium with volatility risk\n');
    fprintf('2. Oil: Energy wealth with geopolitical uncertainty\n');
    fprintf('3. Water: Essential utility with sustainability concerns\n');
end