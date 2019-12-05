# Write a program that prints out all the elements 
# in a list that are less than 5

# Pre-defined list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Create empty list
b = []

# Create for loop to append numbers < 5 to b
for i in a:
    if i < 5:
        b.append(i)
    else:
        pass

# Create for loop that prints elements in b
for i in b:
    print(i)