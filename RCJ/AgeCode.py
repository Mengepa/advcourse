name = input("What is your name? ")
age = input("What is you age? ")
try:
    age_in_five_years = int(age) + 5
except ValueError as ve:
    print('The input is not an integer. \nPlease define age as integer')
else:
    print("In five years ", name, "will be", age_in_five_years, "years old.")