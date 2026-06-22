from pydantic import BaseModel, Field
from typing import List

"""
This module serves as the foundational data layer for the project. 
It defines the Pydantic schemas used to enforce strict type checking and 
validation for warehouse physical locations and product characteristics 
before they are processed by the optimization engine.
"""

class Location(BaseModel):
    """Represents a discrete storage spot in the warehouse grid."""
    id: int
    row: int
    col: int
    distance_to_dock: float

class Product(BaseModel):
    """Represents an SKU with associated picking frequency."""
    sku: str
    pick_frequency: int = Field(..., gt=0)  # Ensures frequency is always positive
                                            # To prevent "Zero-Frequency" or "Negative-Frequency" errors from propagating into your cost matrix calculation.
    category: str = "general"

class WarehouseLayout(BaseModel):
    """Container for the full warehouse state."""
    rows: int
    cols: int
    locations: List[Location]