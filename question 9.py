# Write a python program that checks if a substring is present in a given string.

def check_substring():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring: ")
    if substring in main_string:
        print(f"'{substring}' is present in the main string.")
    else:
        print(f"'{substring}' is not present in the main string.")

check_substring()
