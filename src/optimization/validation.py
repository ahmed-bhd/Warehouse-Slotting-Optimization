"""

"""

def validate_assignments(product_indices, location_indices):
    """
    Ensures that every product is assigned to a unique location 
    and that the assignment count is consistent.
    """
    # Check for structural integrity
    if len(product_indices) != len(location_indices):
        return False, "Count mismatch between products and locations."
    
    # Check for logic integrity (ensure no two products occupy the same slot)
    if len(set(location_indices)) != len(location_indices):
        return False, "Duplicate location assignment detected."
        
    return True, "Assignment is valid."