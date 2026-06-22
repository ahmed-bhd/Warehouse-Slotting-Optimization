"""
This script will read the dimensions from your warehouse.yaml 
and generate a collection of Location objects 
based on your base_types.py schema.

This module generates the physical layout of the warehouse based on 
dimensions provided in warehouse.yaml. It calculates the Manhattan 
distance for each location from the shipping dock.
"""
# src/data/warehouse_generator.py
import yaml
import os
from pathlib import Path
from src.schemas.base_types import Location, WarehouseLayout


def load_config():
    # Direct path resolution as requested
    root_dir = Path(__file__).resolve().parent.parent.parent
    with open(root_dir / "config" / "warehouse.yaml", 'r') as file:
        return yaml.safe_load(file)

def generate_warehouse_layout() -> WarehouseLayout:
    config = load_config()
    rows = config['warehouse']['rows']
    cols = config['warehouse']['cols']
    dock_r, dock_c = config['warehouse']['dock_position']
    
    locations = []
    loc_id = 0
    
    for r in range(rows):
        for c in range(cols):
            # Calculate Manhattan Distance
            dist = abs(r - dock_r) + abs(c - dock_c)
            
            locations.append(Location(id=loc_id,
                                      row=r,
                                      col=c,
                                      distance_to_dock=float(dist)
                                      ))
            loc_id += 1
            
    return WarehouseLayout(rows=rows, cols=cols, locations=locations)

if __name__ == "__main__":
    layout = generate_warehouse_layout()
    print(f"\nGenerated {len(layout.locations)} locations in a {layout.rows}x{layout.cols} grid.")