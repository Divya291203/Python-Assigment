#  Write a python program that counts the occurrences of a specific element in a list.

def count_occurrences():
    elements = input("Enter a list of elements separated by spaces: ").split()
    target = input("Enter the element to count: ")
    print(f"The element '{target}' occurs {elements.count(target)} times in the list.")

count_occurrences()
