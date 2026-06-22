"""
This is where we encapsulate the rules. If you ever need to add specific 
"storage constraints" (e.g., "SKU_001 cannot be placed in row 5 due to cooling 
requirements"), this is where that logic lives.
"""

from src.schemas.base_types import Product, Location

class ConstraintEngine:
    @staticmethod
    def is_valid_assignment(product: Product, location: Location) -> bool:
        """
        Check if a product can legally be placed in a specific location.
        Future-proofed for category or capacity restrictions.
        """
        # Example: Add logic for hazardous materials or temperature zones here
        if product.category == "hazmat" and location.row > 5:
            return False
        return True
    




if __name__ == "__main__":
    from src.schemas.base_types import Product, Location
    
    # Create test objects
    hazmat_prod = Product(sku="HAZ_001", pick_frequency=100, category="hazmat")
    safe_loc = Location(id=99, row=1, col=1, distance_to_dock=2.0)
    restricted_loc = Location(id=100, row=8, col=8, distance_to_dock=16.0)
    
    # Run tests
    print(f"Assignment allowed: {ConstraintEngine.is_valid_assignment(hazmat_prod, safe_loc)}") # Expected: True
    print(f"Assignment allowed: {ConstraintEngine.is_valid_assignment(hazmat_prod, restricted_loc)}") # Expected: False