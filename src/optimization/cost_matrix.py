"""

"""

import numpy as np
from src.models.warehouse import WarehouseModel

def build_cost_matrix(model: WarehouseModel) -> np.ndarray:
    """
    Creates a cost matrix where C[i, j] is the 'travel cost' of
    placing product i at location j.
    """
    products = model.get_products_sorted_by_frequency()
    locations = model.get_locations_sorted_by_distance()
    
    num_prods = len(products)
    num_locs = len(locations)
    
    # Cost = Frequency * Distance
    # Minimizing this product ensures high-frequency items get low-distance spots
    matrix = np.zeros((num_prods, num_locs))
    
    for i, prod in enumerate(products):
        for j, loc in enumerate(locations):
            matrix[i, j] = prod.pick_frequency * loc.distance_to_dock
            
    return matrix



if __name__ == "__main__":
    from src.data.warehouse_generator import generate_warehouse_layout
    from src.data.product_generator import generate_products
    from src.models.warehouse import WarehouseModel
    
    # 1. Prepare minimal model
    model = WarehouseModel(generate_warehouse_layout(), generate_products())
    
    # 2. Build the matrix
    matrix = build_cost_matrix(model)
    
    # 3. Verify
    print(f"Matrix shape: {matrix.shape}")
    print(f"Cost of placing highest freq product in closest location: {matrix[0, 0]:.2f}")
    print(f"Cost of placing highest freq product in furthest location: {matrix[0, -1]:.2f}")
    
    # Visual check: The first row (highest freq) should show increasing costs as columns (distance) increase
    print("\nSample cost row for top product (first 5 locations):")
    print(matrix[0, :5])