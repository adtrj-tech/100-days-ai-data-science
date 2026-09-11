# Day 27 - Object-Oriented Programming
# 100 Days of AI & Data Science


# Creating a class
class Student:

    # Constructor
    def __init__(self, name, student_id, department, marks):
        self.name = name
        self.student_id = student_id
        self.department = department
        self.marks = marks

    # Method to calculate average
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    # Method to display student information
    def display_info(self):
        average = self.calculate_average()

        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Department:", self.department)
        print("Marks:", self.marks)
        print("Average:", average)


# Creating objects
student1 = Student(
    "Adith",
    "IT101",
    "Information Technology",
    [85, 78, 92, 88, 76]
)

student2 = Student(
    "Rahul",
    "IT102",
    "Information Technology",
    [72, 81, 69, 75, 80]
)


# Calling methods
student1.display_info()
student2.display_info()