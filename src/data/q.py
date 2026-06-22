import os
path = "config/warehouse.yaml"
print(f"Checking path: {os.path.abspath(path)}")
print(f"File exists: {os.path.exists(path)}")