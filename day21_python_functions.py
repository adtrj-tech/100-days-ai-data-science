# Day 21 - Python Functions

# Function to calculate average marks
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


# Function to determine grade
def find_grade(average):
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


# Taking input from the user
marks = []

for i in range(5):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)


# Calling functions
average = calculate_average(marks)
grade = find_grade(average)


# Displaying result
print("\n--- Student Result ---")
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)