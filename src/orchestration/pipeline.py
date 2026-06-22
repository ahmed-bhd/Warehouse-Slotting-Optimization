# src/orchestration/pipeline.py
from src.data.warehouse_generator import generate_warehouse_layout
from src.data.product_generator import generate_products
from src.models.warehouse import WarehouseModel
from src.optimization.cost_matrix import build_cost_matrix
from src.optimization.hungarian_solver import solve_slotting
from src.simulation.random_baseline import run_monte_carlo
from src.analytics.performance_metrics import PerformanceReport
from src.visualization.heatmap import plot_warehouse_heatmap

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
        optimized_cost = self.model.calculate_total_travel_cost(p_idx, l_idx)
        
        # 3. Simulation & Analytics
        baseline_costs = run_monte_carlo(self.model, iterations=500)
        report = PerformanceReport.calculate_efficiency_gain(optimized_cost, baseline_costs)
        
        # 4. Visualization
        plot_warehouse_heatmap(self.model, p_idx, l_idx)
        
        print(f"Pipeline Complete.")
        print(f"Efficiency Gain: {report['efficiency_gain_pct']:.2f}%")
        return report

if __name__ == "__main__":
    pipeline = SlottingPipeline()
    pipeline.run_full_analysis()