# password generator
# import random
# import string

# length = int(input("enter the length of password "))
# characters = string.ascii_letters+string.digits +string.punctuation
# password = ""
# for i in range(length):
#     password += random.choice(characters)

# print("generated password",password)

import random
import string


length = int(input ("enter the string length"))
use_uppercase = input("enter yes or no to used uppercae in password")
use_lowercase  = input("enter yes or no to used lowercase in password")
use_digits = input("enter yes or no to used digits in password")
use_symbols   = input("enter yes or no to used symbols in password")

characters = ""
if use_uppercase == "yes":
    characters += string.ascii_uppercase
if use_lowercase == "yes":
    characters += string.ascii_lowercase
if use_digits == "yes":
    characters += string.digits
if use_symbols == "yes":
    characters += string.punctuation

if characters == "":
    print("error")
else:
    password = "".join(random.choice(characters) for i in range(length))
    print("generated password",password)