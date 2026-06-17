import random

secret_number = random.randint(1, 100)
attempts = 0  

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try higher.")
    elif guess > secret_number:
        
        print("Too high! Try lower.")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break