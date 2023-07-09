# OOP stands for Object-Oriented Programming.
# It is a programming paradigm that focuses on organizing code into objects that represent real-world entities or concepts.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary

prince = Employee("Prince", "200000")
print(prince.salary)
print(prince.name)