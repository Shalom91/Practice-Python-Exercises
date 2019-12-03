# The program asks users to enter name and age and returns 
# the year they will be 100 years

# ask user to input their name and age
name = input("Please type in your name: ")
age = int(input("Now enter your age: "))

# import datetime module and define current year
import datetime
year = datetime.datetime.today().year

# calculate when the user will tyrn 100
year_100 = (100-age) + year

# print message
print(name + " " + "you will be 100 years old in: " + str(year_100))