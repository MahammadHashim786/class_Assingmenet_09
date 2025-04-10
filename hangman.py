# Hangman

import random

word = ["python","programming","hangman","computer","laptop","devoloper"]

secret_word = random.choice(word)
guessed_word = ["_"] * len(secret_word)
attempts = 6
guessed_letters = []

print("wellcome to the Hangman Game!")
print("Guess the secret word letter by letter.")
print(f"The word has {len(secret_word)} letters.")
print("You have 6 chance. Good Luck\n")

while attempts > 0:
    print("word:","".join(guessed_word))
    print(f"Guessed letters: {','.join(guessed_letters)}")
    print(f"Remaining attempts: {attempts}")

    guess = input("Guess'a letter:").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("Invalide input! please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter! Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(f"Good job! {guess} is in the words.\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        print(f"Oops! {guess} in not in the word.\n")
        attempts -= 1

        if "_" not in guessed_word:
            print("Congratulation! you guessed the word:",secret_word)
            break

        if attempts == 0:
            print("Guess over! you run out of the attempts.\n")
            print(f"The secret word was: {secret_word}")