from src.data.warehouse_generator import generate_warehouse_layout
from src.data.product_generator import generate_products
from src.models.warehouse import WarehouseModel
from src.optimization.cost_matrix import build_cost_matrix
from src.optimization.hungarian_solver import solve_slotting
from src.optimization.validation import validate_assignments 
from src.simulation.random_baseline import run_monte_carlo
from src.analytics.performance_metrics import PerformanceReport
from src.visualization.heatmap import plot_warehouse_heatmap
import pandas as pd
import os

class SlottingPipeline:
    def __init__(self):
        self.model = None

    def run_full_analysis(self):
        print("--- Starting Optimization Pipeline ---")
        
        # 1. Setup
        layout = generate_warehouse_layout()
        products = generate_products()
        self.model = WarehouseModel(layout, products)
        
        # 2. Optimization
        matrix = build_cost_matrix(self.model)
        p_idx, l_idx = solve_slotting(matrix)
        
        # Validation Step
        is_valid, msg = validate_assignments(p_idx, l_idx)
        if not is_valid:
            raise ValueError(f"Constraint Violation: {msg}")
            
        optimized_cost = self.model.calculate_total_travel_cost(p_idx, l_idx)
        
        # 3. Simulation & Analytics
        baseline_costs = run_monte_carlo(self.model, iterations=500)
        report = PerformanceReport.calculate_efficiency_gain(optimized_cost, baseline_costs)
        
        # Save Quantitative Report
        os.makedirs('outputs', exist_ok=True)
        perf_data = {
            "Metric": ["Baseline Avg", "Optimized Avg", "Efficiency Gain"],
            "Value": [sum(baseline_costs)/len(baseline_costs), optimized_cost, f"{report['efficiency_gain_pct']:.2f}%"]
        }
        pd.DataFrame(perf_data).to_csv('outputs/quantitative_performance.csv', index=False)
        
        # 4. Visualization
        plot_warehouse_heatmap(self.model, p_idx, l_idx)
        
        print(f"Pipeline Complete.")
        print(f"Efficiency Gain: {report['efficiency_gain_pct']:.2f}%")
        return report

if __name__ == "__main__":
    pipeline = SlottingPipeline()
    pipeline.run_full_analysis()