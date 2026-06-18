 # You can change this value to test different conditions
 # ("sunny", "rainy", "cold", etc.)
weather = "rainy"
if weather =="sunny":
    print("Wear sunscreen!")
elif weather == "rainy":
    print("Take an umbrella!")
elif weather == "cold":
    print("Wear a coat!")
else:
    print("Check the weather forecast!")

# Using input() to get user input
answer = input("What is the weather like today? ")
if answer == "sunny":
    print("Wear sunscreen!")
elif answer == "rainy":
    print("Take an umbrella!")
elif answer == "cold":
    print("Wear a coat!")
else:
    print("Check the weather forecast!")