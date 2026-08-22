# Day 15 - Lists + Dictionaries
# Working with Structured Data

print("=== Student Performance Data ===")

students = [
    {
        "name": "Adith",
        "marks": [85, 78, 92],
    },
    {
        "name": "Rahul",
        "marks": [72, 81, 69],
    },
    {
        "name": "Anu",
        "marks": [91, 88, 95],
    },
]

for student in students:
    name = student["name"]
    marks = student["marks"]

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "F"

    print("\nName:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)