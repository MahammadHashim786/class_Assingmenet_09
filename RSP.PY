# Rock, Scissors, Paper

import random

print("wellcome to the Rock, Paper, Scissors Game.")
print("You will play against the computer, Lets begin!")

choice = ["rock","paper","scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors or 'Quit' to step:)").lower()

    if user_choice == 'Quit':
        print("Thanks for playing! Goodbye!")
        break
    if user_choice not in choice:
        print("Invalid choice. please chose rock, paper, or scissors")
        continue
    
    computer_choice = random.choice(choice)
    print(f"Computer choice: {computer_choice} ")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "scissors" and computer_choice == "paper") or \
    (user_choice == "paper" and computer_choice == "rock"):
        print("You win")

    else:
        print("Computer Win!")

    