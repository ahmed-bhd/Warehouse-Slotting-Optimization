"""

"""

from scipy.optimize import linear_sum_assignment
import numpy as np

def solve_slotting(cost_matrix: np.ndarray):
    """
    Finds the optimal assignment of products to locations.
    Returns: row_ind (product indices), col_ind (location indices)
    """
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return row_ind, col_ind




if __name__ == "__main__":
    from src.data.warehouse_generator import generate_warehouse_layout
    from src.data.product_generator import generate_products
    from src.models.warehouse import WarehouseModel
    from src.optimization.cost_matrix import build_cost_matrix
    
    # 1. Prepare Data
    model = WarehouseModel(generate_warehouse_layout(), generate_products())
    
    # 2. Build Cost Matrix
    matrix = build_cost_matrix(model)
    
    # 3. Solve
    product_indices, location_indices = solve_slotting(matrix)
    
    # 4. Display Results
    products = model.get_products_sorted_by_frequency()
    locations = model.get_locations_sorted_by_distance()
    
    print(f"--- Optimal Slotting Plan ---")
    for p_idx, l_idx in zip(product_indices, location_indices):
        prod = products[p_idx]
        loc = locations[l_idx]
        print(f"Assigning {prod.sku} (Picks: {prod.pick_frequency}) to Loc ({loc.row}, {loc.col}) (Dist: {loc.distance_to_dock})")