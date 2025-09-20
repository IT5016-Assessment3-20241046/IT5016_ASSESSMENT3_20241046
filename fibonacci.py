# practice_guessing_game.py
# Practice code inspired by tutorials
# Demonstrates modularity, loops, conditionals, and error handling

import random

# Function to get a valid integer input
def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-50): "))
            if 1 <= guess <= 50:
                return guess
            else:
                print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input! Enter a number.")

# Function to play the guessing game
def play_game():
    number = random.randint(1, 50)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    
    while True:
        guess = get_guess()
        attempts += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
play_game()
