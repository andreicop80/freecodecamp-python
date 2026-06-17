def cost_paint(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    gallons_needed = (sqft_walls + sqft_ceiling) / sqft_per_gallon
    total_cost = gallons_needed * cost_per_gallon
    return total_cost
# Example usage:
sqft_walls = 300
sqft_ceiling = 150
sqft_per_gallon = 350
cost_per_gallon = 25
total_cost = cost_paint(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon)
print(f"The total cost of painting is: ${total_cost:.2f}")