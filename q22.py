# Write a python program that returns the minimum and maximum values in a list of numbers.

def min_max_values():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(number) for number in numbers]
    print(f"The minimum value is {min(numbers)} and the maximum value is {max(numbers)}")

min_max_values()
