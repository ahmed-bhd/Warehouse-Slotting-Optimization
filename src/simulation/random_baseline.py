# src/simulation/random_baseline.py
import numpy as np
import random
from src.models.warehouse import WarehouseModel

def run_monte_carlo(model: WarehouseModel, iterations: int = 1000) -> list:
    """
    Simulates random warehouse slotting assignments to determine 
    the baseline distribution of travel costs.
    """
    costs = []
    products = model.get_products_sorted_by_frequency()
    locations = model.layout.locations
    
    # Pre-calculate frequency and distance arrays for speed
    freqs = np.array([p.pick_frequency for p in products])
    
    for _ in range(iterations):
        # Shuffle locations to create a random assignment
        shuffled_locs = list(locations)
        random.shuffle(shuffled_locs)
        dists = np.array([l.distance_to_dock for l in shuffled_locs])
        
        # Calculate total cost for this random configuration
        total_cost = np.sum(freqs * dists)
        costs.append(total_cost)
        
    return costs

if __name__ == "__main__":
    from src.data.warehouse_generator import generate_warehouse_layout
    from src.data.product_generator import generate_products
    
    model = WarehouseModel(generate_warehouse_layout(), generate_products())
    baseline_costs = run_monte_carlo(model)
    
    print(f"Monte Carlo Simulation (1000 trials)")
    print(f"Average Random Cost: {np.mean(baseline_costs):,.2f}")
    print(f"Best Random Cost:    {min(baseline_costs):,.2f}")