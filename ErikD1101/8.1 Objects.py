"""
persons = []

persons.append({"name": "Dieter", "gender": "male", "age": 34})
persons.append({"name": "Pieter", "gender": "male", "age": 24})
persons.append({"name": "Sofie", "gender": "female", "age": 30})
"""


class Person:

    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
        self.age_in_ten_years = self.celc_age_in_ten_years()

    def celc_age_in_ten_years(self):
        age_new = self.age + 10
        return age_new


D=Person("Dieter","male",34)
P=Person("Pieter","male",24)
S=Person("Sofie","female",30)
persons_list=[D,P,S]


for i in range(len(persons_list)):
    if persons_list[i].gender=="male":
        print(persons_list[i].name+" is male")
    else:
        pass

def age_in_ten_years(age):
    age_new=age+10
    return age_new

for i in range(len(persons_list)):
    print(age_in_ten_years(persons_list[i].age))

