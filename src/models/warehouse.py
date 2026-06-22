"""
This module acts as a wrapper for your WarehouseLayout and Product collections, 
providing helper methods to query the warehouse state and calculate performance.
"""

from src.schemas.base_types import WarehouseLayout, Product
from typing import List

class WarehouseModel:
    def __init__(self, layout: WarehouseLayout, products: List[Product]):
        self.layout = layout
        self.products = products

    def get_locations_sorted_by_distance(self):
        """Returns locations closest to the dock first."""
        return sorted(self.layout.locations, key=lambda x: x.distance_to_dock)

    def get_products_sorted_by_frequency(self):
        """Returns products from highest to lowest velocity."""
        return sorted(self.products, key=lambda x: x.pick_frequency, reverse=True)

    def calculate_total_travel_cost(self, product_indices, location_indices):
        """
        Calculates the total travel cost for a given set of assignments.
        Cost = Sum of (Product Pick Frequency * Location Distance)
        """
        products = self.get_products_sorted_by_frequency()
        locations = self.get_locations_sorted_by_distance()
        
        total_cost = 0
        for p_idx, l_idx in zip(product_indices, location_indices):
            freq = products[p_idx].pick_frequency
            dist = locations[l_idx].distance_to_dock
            total_cost += (freq * dist)
        return total_cost

if __name__ == "__main__":
    from src.data.warehouse_generator import generate_warehouse_layout
    from src.data.product_generator import generate_products
    
    # 1. Setup Data
    layout = generate_warehouse_layout()
    products = generate_products()
    
    # 2. Instantiate Model
    model = WarehouseModel(layout=layout, products=products)
    
    # 3. Verify Logic
    sorted_locs = model.get_locations_sorted_by_distance()
    sorted_prods = model.get_products_sorted_by_frequency()
    
    print(f"Warehouse Model Loaded.")
    print(f"Closest location to dock: {sorted_locs[0].row}, {sorted_locs[0].col} (Dist: {sorted_locs[0].distance_to_dock})")
    print(f"Highest velocity product: {sorted_prods[0].sku} (Freq: {sorted_prods[0].pick_frequency})")