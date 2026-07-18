# List of inventory 
inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

# Count for the restock
restock_count = 0

# Checking each item in the inventory for restock
for item in inventory:
    if item["stock"] < item["threshold"]:
        print(f"Restock alert: {item['item']} (stock: {item['stock']}, threshold: {item['threshold']})")
        restock_count += 1

# Displaying the total number of items that need restocking
print(f"\nTotal items needing restock: {restock_count}")