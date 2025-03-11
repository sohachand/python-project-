import random
import csv

# Function to load word lists from a CSV file
def load_word_lists(filename):
    word_lists = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            genre, word = row
            if genre not in word_lists:
                word_lists[genre] = []
            word_lists[genre].append(word)
    return word_lists

# Function to choose a genre
def choose_genre(word_lists):
    print("Choose a genre:")
    for genre in word_lists.keys():
        print(f"- {genre}")
    while True:
        genre = input("Enter the genre: ").lower()
        if genre in word_lists:
            return genre
        else:
            print("Invalid genre. Please choose from the list.")

# Function to choose a random word from the selected genre
def choose_word(genre, word_lists):
    return random.choice(word_lists[genre])

# Function to initialize the game
def initialize_game(word_lists):
    genre = choose_genre(word_lists)
    word = choose_word(genre, word_lists)
    guessed_word = ["_"] * len(word)
    guessed_letters = []
    attempts = 6
    return word, guessed_word, guessed_letters, attempts

# Function to display the game state
def display_game_state(guessed_word, attempts, guessed_letters):
    print(" ".join(guessed_word))
    print(f"Attempts left: {attempts}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

# Function to get the player's guess
def get_player_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        else:
            return guess

# Function to update the game state
def update_game_state(word, guessed_word, guessed_letters, guess, attempts):
    if guess in word:
        print("Good guess!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1
    guessed_letters.append(guess)
    return guessed_word, attempts

# Function to check for win or loss
def check_win_or_loss(word, guessed_word, attempts):
    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
        return True
    elif attempts == 0:
        print(f"You lost! The word was: {word}")
        return True
    return False

# Main game loop
def hangman():
    word_lists = load_word_lists("words.csv")  # Load the dataset
    word, guessed_word, guessed_letters, attempts = initialize_game(word_lists)
    print("Welcome to Hangman!")
    
    while True:
        display_game_state(guessed_word, attempts, guessed_letters)
        guess = get_player_guess(guessed_letters)
        guessed_word, attempts = update_game_state(word, guessed_word, guessed_letters, guess, attempts)
        
        if check_win_or_loss(word, guessed_word, attempts):
            break


hangman()
