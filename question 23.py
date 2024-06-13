# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def temperature_conversion():
    choice = input("Choose conversion: (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius: ")
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius * 9/5 + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please choose 1 or 2.")

temperature_conversion()
