function [cm_value, sustainability] = resource_cm(type, reserves, extraction_rate, price_usd, extraction_cost_usd)
    % OIL/WATER COMMODITY MONEY MODEL
    % Pioneered by Okikiola L Eniola (kiki@aidreamfusion.com)
    % Unified CM Framework: Bitcoin + Oil + Water
    
    % ===== CORE METRICS =====
    % Net Value per Unit (Market Price - Extraction Cost)
    net_value_per_unit = price_usd - extraction_cost_usd;
    
    % Total Net Value (Reserve-Based Wealth)
    total_net_value = reserves * net_value_per_unit;
    
    % Depletion Timeline (Years to Exhaustion)
    depletion_years = reserves / extraction_rate;
    
    % CM Value Calculation (Net Value × Scarcity Factor)
    scarcity_factor = 1 / (extraction_rate / reserves); % Inverse extraction ratio
    cm_value = total_net_value * scarcity_factor / 1e12; % Scaled to trillions
    
    % ===== SUSTAINABILITY ASSESSMENT =====
    if depletion_years > 100
        sustainability = 90; % Highly Sustainable
    elseif depletion_years > 50
        sustainability = 70; % Sustainable
    elseif depletion_years > 20
        sustainability = 50; % Moderate
    else
        sustainability = 30; % Unsustainable
    end
    
    % ===== VISUALIZATION =====
    figure('Name', [upper(type) ' CM Analysis'], 'Position', [100, 100, 800, 600]);
    
    % CM Metrics Bar Chart
    subplot(2,1,1);
    bar_data = [total_net_value/1e12, cm_value];
    bar(bar_data, 'FaceColor', [0.6 0.3 0.1; 0.2 0.6 0.8]);
    set(gca, 'XTickLabel', {'Total Net Value (T$)', 'CM Value Index'});
    title([upper(type) ' CM Metrics - Eniola Framework']);
    ylabel('Trillion USD');
    grid on;
    
    % Sustainability Gauge
    subplot(2,1,2);
    gauge_plot(sustainability);
    title('Sustainability Index');
    
    % ===== CONSOLE OUTPUT =====
    fprintf('\n=== %s CM ANALYSIS (Eniola Framework) ===\n', upper(type));
    fprintf('Total Net Value: $%.2f trillion\n', total_net_value/1e12);
    fprintf('CM Value Index: %.2f\n', cm_value);
    fprintf('Years to Depletion: %.1f\n', depletion_years);
    fprintf('Sustainability: %.0f/100\n', sustainability);
    fprintf('Interpretation: ');
    
    if sustainability > 70
        fprintf('Sustainable Resource - Stable CM System\n');
    elseif sustainability > 40
        fprintf('Moderate Sustainability - Monitor Extraction\n');
    else
        fprintf('Unsustainable - High Depletion Risk\n');
    end
end

% ===== HELPER FUNCTION: GAUGE PLOT =====
function gauge_plot(value)
    % Create Sustainability Gauge Visualization
    theta = linspace(0, pi, 100);
    r = 1;
    x = r * cos(theta);
    y = r * sin(theta);
    
    % Color Zones (Red=High Risk, Yellow=Moderate, Green=Low Risk)
    red_zone = [0, 0.3*pi];
    yellow_zone = [0.3*pi, 0.7*pi];
    green_zone = [0.7*pi, pi];
    
    % Plot Gauge Background
    fill([x(1:30), 0], [y(1:30), 0], [1 0.4 0.4]); hold on;
    fill([x(30:70), 0], [y(30:70), 0], [1 0.8 0.2]);
    fill([x(70:end), 0], [y(70:end), 0], [0.4 0.8 0.4]);
    
    % Plot Needle
    needle_angle = (value/100) * pi;
    plot([0, cos(needle_angle)], [0, sin(needle_angle)], 'k-', 'LineWidth', 3);
    plot(0,0,'ko','MarkerSize',10,'MarkerFaceColor','k');
    
    axis equal; hold off;
end