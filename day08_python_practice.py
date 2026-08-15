# Day 8 - Python Fundamentals in Practice

print("=== Student Performance Analyzer ===")

# Taking input
name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / len(marks)

# Determine grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Display result
print("\n=== Performance Report ===")
print("Name:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)

if average >= 50:
    print("Status: Passed")
else:
    print("Status: Failed")