# The program asks the user for a number and prints out a list of all the 
# divisors of that number

# ask the user input a number
num = int(input('Please enter a number: '))

# define a range
x = range(1, num+1)

# create a placeholder for divisors
y = []

# create a for loop to print out divisors of num
for i in x:
    if num % i == 0:
        y.append(i)
    else:
        pass

for i in y:
    print(i)
