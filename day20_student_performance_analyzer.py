# Student Performance Analyzer

students = [
    {
        "name": "Adith",
        "marks": [85, 78, 92]
    },
    {
        "name": "Anaswara",
        "marks": [72, 81, 69]
    },
    {
        "name": "Avanthika",
        "marks": [91, 88, 95]
    },
    {
        "name": "Sayooj",
        "marks": [76, 84, 79]
    }
]


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def analyze_student(student):
    average = calculate_average(student["marks"])
    grade = calculate_grade(average)

    return average, grade


print("=== Student Performance Report ===")

top_student = ""
highest_average = 0

for student in students:
    average, grade = analyze_student(student)

    print("\nName:", student["name"])
    print("Marks:", student["marks"])
    print("Average:", round(average, 2))
    print("Grade:", grade)

    if average > highest_average:
        highest_average = average
        top_student = student["name"]


print("\n=== Top Performer ===")
print("Student:", top_student)
print("Average:", round(highest_average, 2))