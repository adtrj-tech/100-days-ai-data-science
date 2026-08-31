# Day 22 - Python Comprehensions

# 1. List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]

print("Numbers:", numbers)
print("Squares:", squares)


# 2. List comprehension with condition
even_numbers = [number for number in numbers if number % 2 == 0]

print("\nEven Numbers:", even_numbers)


# 3. Dictionary comprehension
student_marks = {
    "Adith": 85,
    "Rahul": 72,
    "Anu": 91,
    "Arjun": 68
}

passed_students = {
    name: marks
    for name, marks in student_marks.items()
    if marks >= 70
}

print("\nStudent Marks:", student_marks)
print("Passed Students:", passed_students)


# 4. Set comprehension
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 6]

unique_squares = {
    number ** 2
    for number in numbers_with_duplicates
}

print("\nOriginal Numbers:", numbers_with_duplicates)
print("Unique Squares:", unique_squares)