# Write a python program that checks whether a given number is even or odd.

def check_even_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


check_even_odd()