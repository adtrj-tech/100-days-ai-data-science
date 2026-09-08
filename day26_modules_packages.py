# Day 26 - Modules & Packages
# 100 Days of AI & Data Science

import student_utils


marks = [85, 72, 91, 68, 78]

average = student_utils.calculate_average(marks)
grade = student_utils.find_grade(average)
highest = student_utils.find_highest_mark(marks)


print("--- Student Performance ---")
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)
print("Highest Mark:", highest)