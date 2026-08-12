inventory = {"apples": 10, "bananas": 5, "oranges": 8}

# Clear all items while keeping the object in memory
inventory.clear()

print("Cleared Inventory:", inventory)
print("Dictionary ID (intact):", id(inventory))