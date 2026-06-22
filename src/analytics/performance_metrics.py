# src/analytics/performance_metrics.py

"""
        Calculates the percentage improvement of the optimized solution 
        over the average random baseline.

Why this is the "Analytics" layer:
Quantification: You move from saying "It's faster" to "It's X% more efficient."

Sensitivity: In the future, you can use this same module to test how your efficiency changes 
if you increase the number of products or change the warehouse layout (Sensitivity Analysis).

Reporting: This provides the exact number you would put into a business slide deck to justify 
why your algorithm should be used in production.
"""

import numpy as np

class PerformanceReport:
    @staticmethod
    def calculate_efficiency_gain(optimized_cost: float, baseline_costs: list) -> dict:
        """
        Calculates the percentage improvement of the optimized solution 
        over the average random baseline.
        """
        avg_baseline = np.mean(baseline_costs)
        gain = ((avg_baseline - optimized_cost) / avg_baseline) * 100
        
        return {
            "average_baseline": avg_baseline,
            "optimized_cost": optimized_cost,
            "efficiency_gain_pct": gain
        }

if __name__ == "__main__":
    # Test this with a known optimized cost
    # Replace 50000 with the actual output of your hungarian_solver.py
    report = PerformanceReport.calculate_efficiency_gain(50000, [406154.86]) 
    print(f"Optimization Efficiency Gain: {report['efficiency_gain_pct']:.2f}%")