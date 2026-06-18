import random

# Initialize the score counters OUTSIDE the loop so they persist
wins = 0
losses = 0

while True:
    print("\n=======================================")
    print("Welcome to the Number Guessing Game!")
    print("=======================================")
    print(f"Current Score | Wins: {wins} | Losses: {losses}")
    print("---------------------------------------")
    print("Choose a difficulty level: Easy, Medium, or Hard")
    difficulty = input("Enter difficulty (easy/medium/hard): ").strip().lower()

    if difficulty == "easy":
        max_number = 50
    elif difficulty == "hard":
        max_number = 200
    else:
        max_number = 100

    secret_number = random.randint(1, max_number)
    attempts = 5
    

    print(f"\nI have selected a secret number between 1 and {max_number}.")
    print(f"Can you guess it? You have {attempts} attempts.")

    # Track if the player won this specific round
    round_won = False

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
            round_won = True
            wins += 1  # Add a win!
            break
    else:
        print(f"\nGame over! The correct number was {secret_number}.")
        losses += 1  # Add a loss!

    # Ask to play again
    print("\n---------------------------------------")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    
    if play_again not in ["yes", "y"]:
        break

# --- FINAL SUMMARY PRINTED AT THE END ---
total_games = wins + losses

print("\n=======================================")
print("             GAME SUMMARY              ")
print("=======================================")
print(f" Total Games Played: {total_games}")
print(f" Wins              : {wins}")
print(f" Losses            : {losses}")

# Calculate win rate percentage safely (avoid division by zero just in case)
if total_games > 0:
    win_rate = (wins / total_games) * 100
    print(f" Win Rate          : {win_rate:.1f}%")
else:
    print(" Win Rate          : 0.0%")

print("\nThanks for playing! Goodbye! 👋")
print("=======================================")    
