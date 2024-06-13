#  Write a program that reads the content of a text file and prints it to the console.

def read_from_file():
    try:
        with open("output.txt", "r") as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure 'output.txt' exists.")

read_from_file()
