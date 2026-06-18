import random

# A list of random words for the game
WORD_BANK = [
    "python", "developer", "database", "programming", "terminal",
    "jupiter", "keyboard", "software", "network", "security",
    "function", "variable", "computer", "matrix", "algorithm"
]

# The visual stages of the hangman (0 mistakes to 6 mistakes)
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
     =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
     =========
    """
]

def play_hangman():
    # Pick a random word from our bank
    secret_word = random.choice(WORD_BANK).lower()
    
    # Track the letters the player has guessed
    guessed_letters = set()
    
    # Maximum allowed mistakes is 6 (matching our hangman stages)
    max_mistakes = 6
    mistakes = 0

    print("=======================================")
    print("      Welcome to Python Hangman!       ")
    print("=======================================")

    while mistakes < max_mistakes:
        # 1. Print the current hangman state
        print(HANGMAN_STAGES[mistakes])
        
        # 2. Display the hidden word (e.g., "p _ t h _ n")
        displayed_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word: " + " ".join(displayed_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining lives: {max_mistakes - mistakes}")
        print("---------------------------------------")

        # Check if the player won
        if "_" not in displayed_word:
            print(f"🎉 Congratulations! You guessed the word: {secret_word.upper()}!")
            break

        # 3. Get player input
        guess = input("Guess a letter: ").strip().lower()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter.")
            continue
        if guess in guessed_letters:
            print(f"❌ You already guessed '{guess}'. Try a different letter.")
            continue

        # Add the letter to our guessed tracker
        guessed_letters.add(guess)

        # 4. Check if the guess is right or wrong
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Incorrect! '{guess}' is not in the word.")
            mistakes += 1

    # If the loop finished because the player ran out of lives
    else:
        print(HANGMAN_STAGES[mistakes])
        print("Game Over! 💀")
        print(f"The secret word was: {secret_word.upper()}")

# Run the game
if __name__ == "__main__":
    while True:
        play_hangman()
        print("---------------------------------------")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Goodbye! 👋")
            break