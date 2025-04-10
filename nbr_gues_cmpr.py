# Guess The Number . Computer Guess

import random

print("wellcome to the guess the Number Game!")
print("Think of a number Between 1 and 100, and i will try to guess it.")
print("You can tell me if my guess is too high (H), too low (L), or correct (C).")

low = 1
high = 100
guesses = 0

while True:
    guess = random.randint(low, high)
    guesses += 1

    print(f"My guess is: {guesses}")
    user_input = input("Is my guess too high (H), too low (L), or correct (C)?").upper()

    if user_input == "H":
        high = guess - 1
    elif user_input == "L":
        low = guess + 1
    elif user_input == "C":
        print(f"Yay | I guessed your number is {guesses} tries!")
        break
    else:
        print("Invalid input. please enter H, L, or C.")