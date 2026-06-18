import random

# A list of words for the game
WORDS = ["python", "developer", "computer", "algorithm", "software", "jupiter"]

# Visual representation of the hangman gallows
HANGMAN_STAGES = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
      ---
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / 
      ---
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |      
      ---
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |      
      ---
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |      
      ---
    """,
    """
       --------
       |      |
       |      O
       |    
       |    
       |      
      ---
    """,
    """
       --------
       |      |
       |      
       |    
       |    
       |      
      ---
    """
]

def play_hangman():
    word = random.choice(WORDS).lower()
    guessed_letters = set()
    tries = 6  # Number of allowed wrong guesses
    
    print("Welcome to Hangman!")
    
    while tries > 0:
        # Print the current state of the gallows
        print(HANGMAN_STAGES[tries])
        
        # Display the word with underscores for unguessed letters
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word to guess: " + " ".join(display_word))
        print(f"Remaining lives: {tries}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}\n")
        
        # Check if the player won
        if "_" not in display_word:
            print(f"🎉 Congratulations! You guessed the word: {word}")
            break
            
        # Get player input
        guess = input("Guess a letter: ").lower().strip()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue
            
        # Add to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            tries -= 1
            
    else:
        # This executes if the while loop completes without a 'break' (player ran out of tries)
        print(HANGMAN_STAGES[0])
        print(f"💀 Game Over! You ran out of lives. The word was: {word}")

if __name__ == "__main__":
    play_hangman()