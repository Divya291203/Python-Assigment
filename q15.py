# Write a program that reads data from a CSV file and prints it to the console.

import csv
def read_csv_file():
    file_name = input("Enter the name of the CSV file (with .csv extension): ")
    try:
        with open(file_name, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(', '.join(row))
    except FileNotFoundError:
        print("File not found. Please ensure the file exists.")

read_csv_file()
