# Write a python program that takes a list of numbers and returns their sum.

def sum_of_list():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(number) for number in numbers]
    print(f"The sum of the list is: {sum(numbers)}")

sum_of_list()
