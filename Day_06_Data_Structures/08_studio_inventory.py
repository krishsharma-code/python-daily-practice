# 08_studio_inventory.py
# Concept: Real-world dictionary application (VS Gaming Studio)

# Managing studio assets using a dictionary of dictionaries
inventory = {
    "PC_001": {"type": "Gaming Rig", "status": "Available", "specs": "RTX 4090, 64GB RAM"},
    "VR_001": {"type": "Meta Quest 3", "status": "In Use", "specs": "128GB"},
    "CON_001": {"type": "PS5", "status": "Available", "specs": "1TB Disc Edition"},
    "PC_002": {"type": "Streaming PC", "status": "Maintenance", "specs": "RTX 3080, 32GB RAM"}
}

def display_inventory(inv):
    print("\n--- VS Gaming Studio Asset Inventory ---")
    print(f"{'Asset ID':<10} | {'Type':<15} | {'Status':<12} | {'Specs'}")
    print("-" * 65)
    for asset_id, details in inv.items():
        print(f"{asset_id:<10} | {details['type']:<15} | {details['status']:<12} | {details['specs']}")

def update_asset_status(inv, asset_id, new_status):
    if asset_id in inv:
        inv[asset_id]['status'] = new_status
        print(f"\n[UPDATE] {asset_id} status changed to {new_status}")
    else:
        print(f"\n[ERROR] Asset {asset_id} not found!")

# Run operations
display_inventory(inventory)
update_asset_status(inventory, "PC_001", "In Use")
update_asset_status(inventory, "CON_001", "Maintenance")
display_inventory(inventory)
