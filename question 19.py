# TWrite a python program that removes all punctuation from a given string.

import string

def remove_punctuation():
    user_input = input("Enter a string: ")
    cleaned_string = user_input.translate(str.maketrans('', '', string.punctuation))
    print(f"The string without punctuation is: {cleaned_string}")

remove_punctuation()
