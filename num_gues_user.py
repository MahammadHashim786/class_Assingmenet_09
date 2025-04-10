# Number Guessing Game user 

import random

number = random.randint(1, 100)
guesses = 0

while True:

    user_guess = input("Enter your guess: ")

    try:
        user_guess = int(user_guess)
        guesses += 1

        if user_guess < number:
            print("Too low! Try again")
        elif user_guess > number:
            print("Too hight! Try again")
        else:
            print(f"Congratulations! you guessed the number in {guesses} tries.")
            break
    except ValueError:
        print("please enter a valid number")