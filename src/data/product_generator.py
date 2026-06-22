"""
This module will create a list of Product objects following a Pareto distribution 
(the 80/20 rule), which simulates a realistic warehouse environment where a few items 
drive most of the traffic.
"""

import numpy as np
import yaml
from pathlib import Path
from src.schemas.base_types import Product

def load_config():
    # Direct path resolution as requested
    root_dir = Path(__file__).resolve().parent.parent.parent
    with open(root_dir / "config" / "warehouse.yaml", 'r') as file:
        return yaml.safe_load(file)

def generate_products() -> list[Product]:
    config = load_config()
    n = config['simulation']['num_products']
    alpha = config['simulation']['frequency_distribution']['alpha']
    min_p = config['simulation']['frequency_distribution']['min_picks']
    max_p = config['simulation']['frequency_distribution']['max_picks']
    
    # Generate Pareto distributed frequencies
    # Pareto distribution models the 80/20 rule: few items have high frequency
    frequencies = np.random.pareto(alpha, n)
    
    # Normalize and scale to min/max picks defined in yaml
    normalized = (frequencies - frequencies.min()) / (frequencies.max() - frequencies.min())
    scaled = (normalized * (max_p - min_p) + min_p).astype(int)
    
    products = [
        Product(sku=f"SKU_{i:03d}", pick_frequency=int(f)) 
        for i, f in enumerate(scaled)
    ]
    return products


"""
if __name__ == "__main__":
    products = generate_products()
    print(f"Generated {len(products)} products.")
    print(f"Sample: {products[0].sku} with {products[0].pick_frequency} picks")
"""
if __name__ == "__main__":
    products = generate_products()
    
    # Sort by frequency descending to easily verify the Pareto distribution
    products.sort(key=lambda x: x.pick_frequency, reverse=True)
    
    print(f"--- Generated {len(products)} products (Sorted by Frequency) ---")
    
    # Print the full list of SKUs and their frequencies
    for i, prod in enumerate(products):
        print(f"Rank {i+1:03d} | SKU: {prod.sku} | Picks: {prod.pick_frequency:5d}")
        
    print("-" * 45)
    print(f"\nTop Mover: {products[0].sku} ({products[0].pick_frequency} picks)")
    print("\n")