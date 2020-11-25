name = input("What is your name? ")
age = input("What is you age? ")
try:
    age_in_five_years = int(age) + 5
except ValueError:
    print("Please enter age as a whole number (integer)")
else:
    print("In five years ", name, "will be", age_in_five_years, "years old.")
finally:
    print("Thanks for using this program")