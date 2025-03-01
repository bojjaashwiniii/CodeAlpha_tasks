import random

# List of words for the game
word_list = ['python', 'hangman', 'developer', 'computer', 'programming', 'challenge', 'artificial']

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function
def play_hangman():
    word = choose_word()  # Choose a random word
    guessed_letters = []  # List to keep track of guessed letters
    incorrect_guesses = 0  # To count the number of incorrect guesses
    max_incorrect_guesses = 6  # Limit on the number of incorrect guesses
    word_guessed = False

    print("Welcome to Hangman!")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses and not word_guessed:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue
        
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, the letter '{guess}' is not in the word.")
        
        # Check if the word has been fully guessed
        if all(letter in guessed_letters for letter in word):
            word_guessed = True
            print(f"\nCongratulations! You've guessed the word: {word}")
    
    # If the game ends due to exceeding incorrect guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nSorry, you've exceeded the maximum number of incorrect guesses. The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
