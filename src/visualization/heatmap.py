"""
In the context of your warehouse optimization, we plot a heatmap because it transforms abstract 
numerical data into a spatial map that mirrors your physical environment. 
It is the most effective tool to verify that your mathematical model aligns with your operational reality.

Why we plot a Heatmap:
1. Spatial Verification: You can instantly confirm if your high-velocity SKUs (your "Top Movers") 
are actually located where they should be (near the dock).

2. Density Awareness: It highlights "hot spots" (high pick activity) and "cold spots" (low activity/dead stock).

3. Constraint Identification: It reveals if your constraints are working correctly. 
For example, if you see high-frequency items clustered in a far corner, you know your ConstraintEngine 
or CostMatrix logic has a flaw.

4. Communication: Heatmaps are the industry standard for reporting to warehouse managers. 
They communicate complex optimization logic (like the Hungarian algorithm) at a single glance.
"""


# src/visualization/heatmap.py
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_warehouse_heatmap(model, product_indices, location_indices, save_path="outputs/warehouse_heatmap.png"):
    """
    Creates a visual representation of the warehouse slotting and saves it.
    """
    # 1. Ensure output directory exists
    output_dir = os.path.dirname(save_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Initialize a grid (assuming 10x10 based on your previous logs)
    grid = np.zeros((10, 10))
    
    products = model.get_products_sorted_by_frequency()
    locations = model.get_locations_sorted_by_distance()
    
    # Fill the grid with frequency data
    for p_idx, l_idx in zip(product_indices, location_indices):
        loc = locations[l_idx]
        grid[loc.row, loc.col] = products[p_idx].pick_frequency
        
    # Generate the heatmap
    plt.figure(figsize=(7, 5))
    heatmap = plt.imshow(grid, cmap='YlOrRd', interpolation='nearest')
    plt.colorbar(heatmap, label='Pick Frequency')
    plt.title("Warehouse Slotting Intensity Heatmap")
    plt.xlabel("Warehouse Column")
    plt.ylabel("Warehouse Row")
    
    # 2. Save the plot
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {save_path}")
    
    #plt.show()



if __name__ == "__main__":
    # Integration test: Run this to see the plot
    from src.data.warehouse_generator import generate_warehouse_layout
    from src.data.product_generator import generate_products
    from src.models.warehouse import WarehouseModel
    from src.optimization.cost_matrix import build_cost_matrix
    from src.optimization.hungarian_solver import solve_slotting
    
    model = WarehouseModel(generate_warehouse_layout(), generate_products())
    matrix = build_cost_matrix(model)
    p_idx, l_idx = solve_slotting(matrix)
    
    plot_warehouse_heatmap(model, p_idx, l_idx)