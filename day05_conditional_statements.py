# Day 5 - Conditional Statements

print("=== Student Result Checker ===")

name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Result ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)

if marks >= 50:
    print("Status: Passed")
else:
    print("Status: Failed")