class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + year


name1 = input()
last_name1 = input()
year = input()
new = Student(name1, last_name1, year)

print(new.id)
