# password Generate python project 

import random
import string

print("wellcome to the password Generator")
print("Generate a string, random password,\n")

try:
    password_lenght = int(input("Enter the desired password lenght (minimum 6 characters): "))
    if password_lenght < 6:
        print("password lenght must be least 6 characters.")
        exit()
except ValueError:
    print("Invalid input: please enter a valid number.")
    exit()

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

password = "".join(random.choice(all_characters) for _ in range(password_lenght))
print(f"\n Your random password is: {password}")
print("keep it safe")
