import random

# This loop keeps the whole game running
while True:
    print("\n=======================================")
    print("Welcome to the Number Guessing Game!")
    print("=======================================")
    print("Choose a difficulty level: Easy, Medium, or Hard")
    difficulty = input("Enter difficulty (easy/medium/hard): ").strip().lower()

    # Set the maximum number based on difficulty
    if difficulty == "easy":
        max_number = 50
    elif difficulty == "hard":
        max_number = 200
    else:
        # Default to medium (1-100)
        max_number = 100

    secret_number = random.randint(1, max_number)
    attempts = 3

    print(f"\nI have selected a secret number between 1 and {max_number}.")
    print(f"Can you guess it? You have {attempts} attempts.")

    # The Game Loop
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid round number!")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number}!")
            break
    else:
        print(f"\nGame over! The correct number was {secret_number}.")

    # --- PLAY AGAIN VARIANT ---
    print("\n---------------------------------------")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    
    # If the user types 'no', 'n', or anything that isn't 'yes'/'y', we break the loop
    if play_again not in ["yes", "y"]:
        print("\nThanks for playing! Goodbye! 👋")
        break  # This exits the outer 'while True' loop and closes the game      
