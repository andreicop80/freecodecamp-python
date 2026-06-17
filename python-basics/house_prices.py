def house_price(num_bedrooms,num_bathrooms,area):
    price = (num_bedrooms * 50000) + (num_bathrooms * 30000) + (area * 200)
    return price
price = house_price(3, 2, 1500)
print(f"The price of the house is: ${price:.2f}")   
#def house_price(num_bedrooms,num_bathrooms,area) --- IGNORE ---
option1 = house_price(3, 2, 1500)
option2 = house_price(4, 3, 2000)
print(f"Option 1: ${option1:.2f}")
print(f"Option 2: ${option2:.2f}")
