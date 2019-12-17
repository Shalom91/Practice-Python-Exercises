# Write a one-line program that takes a list and makes a new list of only even elements

# Given the following list:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create empty list as placeholder
b = []

# List comprehenhion of the program
b = [num for num in a if num % 2 == 0]

# Print new list
print(b)

