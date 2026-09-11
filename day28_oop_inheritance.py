# Day 28 - OOP Inheritance

# Parent class
class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


# Child class
class Employee(Person):

    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display_employee(self):
        print("Employee ID:", self.employee_id)


# Child class of Employee
class Manager(Employee):

    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_manager(self):
        print("Department:", self.department)


# Creating Manager object
manager = Manager(
    "Adith",
    "EMP101",
    "Artificial Intelligence"
)


# Calling inherited and own methods
manager.display_name()
manager.display_employee()
manager.display_manager()