car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

removed_value = car.pop("color", None)
print(f"Removed 'color': {removed_value}")


all_pairs = car.items()
print("All key-value pairs:", list(all_pairs))

key_to_check = "model"
exists = key_to_check in car
print(f"Does '{key_to_check}' exist?: {exists}")