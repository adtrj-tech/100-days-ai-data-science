# Day 16 - Functions with Lists & Dictionaries
# Processing structured data using functions


students = [
    {
        "name": "Adith",
        "marks": [85, 78, 92]
    },
    {
        "name": "Rahul",
        "marks": [72, 81, 69]
    },
    {
        "name": "Anu",
        "marks": [91, 88, 95]
    }
]


# Function to calculate average
def calculate_average(marks):
    return sum(marks) / len(marks)


# Function to determine grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


# Function to display student information
def display_student(student):
    name = student["name"]
    marks = student["marks"]

    total = sum(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\nName:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


print("=== Student Performance Analyzer ===")

for student in students:
    display_student(student)