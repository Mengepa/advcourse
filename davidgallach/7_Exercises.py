# Exceptions exercise 1

name = input("What is your name? ")
age = input("What is you age? ")
try:
    age_in_five_years = int(age) + 5
except ValueError:
    print('The input is not an integer. Please introduce an integer.')
else:
    print("In five years", name, "will be", age_in_five_years, "years old.")