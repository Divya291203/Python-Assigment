#  Write a python program that calculates the sum of the digits of a given number.

def sum_of_digits():
    number = input("Enter a number: ")
    digit_sum = sum(int(digit) for digit in number)
    print(f"The sum of the digits of {number} is {digit_sum}")

sum_of_digits()
