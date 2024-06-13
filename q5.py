#  Write a program that takes a string input from the user and writes it to a text file.

def write_to_file():
    user_input = input("Enter a string to write to a file: ")
    with open("output.txt", "w") as file:
        file.write(user_input)
    print("The string has been written to output.txt")

write_to_file()
