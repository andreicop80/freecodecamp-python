def inventory_check(item, inventory, location):
    if item in inventory:
        return f"{item} is in the inventory at {location}."
    else:
        return f"{item} is not in the inventory at {location}."
# Example usage:
inventory = ["laptop", "mouse", "keyboard", "monitor", "desk", "chair", "printer", "scanner"]
item = "mouse"
item_not_in_inventory = "printer"
inventory_location = "Warehouse B"
result_in_inventory = inventory_check(item, inventory, inventory_location)
result_not_in_inventory = inventory_check(item_not_in_inventory, inventory, inventory_location)
print(result_in_inventory)
print(result_not_in_inventory)
inventory_location_2 = "Warehouse A"
result = inventory_check(item, inventory, inventory_location_2)
print(result)   