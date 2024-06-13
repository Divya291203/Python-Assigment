#  Write a program in python that converts a string into a list of its characters.

def string_to_char_list():
    user_input = input("Enter a string: ")
    char_list = list(user_input)
    print(f"The list of characters is: {char_list}")

string_to_char_list()
