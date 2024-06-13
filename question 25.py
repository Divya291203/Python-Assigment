# Write a program that copies the contents of one text file to another.

def copy_file():
    source_file = input("Enter the name of the source file (with extension): ")
    destination_file = input("Enter the name of the destination file (with extension): ")
    
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Contents copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print("Source file not found. Please ensure the file exists.")

copy_file()
