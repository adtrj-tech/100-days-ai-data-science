# Day 41: NumPy Fundamentals

import numpy as np

# 1. Create a NumPy array
marks = np.array([85, 90, 78, 92, 88])

print("Student Marks:", marks)

# 2. Basic array operations
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# 3. Filter marks greater than 85
high_marks = marks[marks > 85]
print("Marks Greater Than 85:", high_marks)

# 4. Perform operations on every element
bonus_marks = marks + 5
print("Marks After Bonus:", bonus_marks)

# 5. Create a 2D array
student_marks = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [75, 80, 82]
])

print("\nStudent Marks Table:")
print(student_marks)

# 6. Calculate subject-wise averages
print("Subject-wise Averages:", np.mean(student_marks, axis=0))

# 7. Calculate student-wise averages
print("Student-wise Averages:", np.mean(student_marks, axis=1))