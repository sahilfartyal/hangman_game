import random

# A list of words to choose from
words = ["python", "hangman", "programming", "developer", "openai"]
print(words)

# Function to choose a random word
def get_random_word(word_list):
    return random.choice(word_list)
# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Hangman game function
def hangman():
    word = get_random_word(words)
    guessed_letters = set()
    attempts = 8  # Number of attempts
    word_guessed = False

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while not word_guessed and attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word. You have {attempts} attempts left.")

        current_display = display_word(word, guessed_letters)
        print("\nCurrent word: ", current_display)

        if "_" not in current_display:
            word_guessed = True

    if word_guessed:
        print(f"\nCongratulations! You guessed the word '{word}'.")
    else:
        print(f"\nGame over! The word was '{word}'.")

# Run the game
hangman()
