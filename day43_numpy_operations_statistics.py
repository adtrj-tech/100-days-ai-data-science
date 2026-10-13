# Day 43: NumPy Operations & Statistics
# #100DaysOfAIwithAdhi

import numpy as np

# Sample dataset: marks of 10 students
marks = np.array([78, 85, 92, 67, 88, 95, 73, 81, 90, 76])

print("Student Marks:", marks)

# 1. Basic statistical calculations
print("\n--- Basic Statistics ---")
print("Total Marks:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Standard Deviation:", round(np.std(marks), 2))
print("Variance:", round(np.var(marks), 2))

# 2. Sort the marks
print("\n--- Sorting ---")
print("Sorted Marks:", np.sort(marks))

# 3. Apply mathematical operations
print("\n--- Mathematical Operations ---")
print("Marks + 5:", marks + 5)
print("Marks - 5:", marks - 5)
print("Marks * 2:", marks * 2)

# 4. Filter marks using conditions
print("\n--- Filtering ---")
print("Marks above 80:", marks[marks > 80])
print("Marks below 75:", marks[marks < 75])

# 5. Count students meeting a condition
passed_students = np.sum(marks >= 40)
high_scorers = np.sum(marks >= 85)

print("\n--- Student Analysis ---")
print("Students scoring at least 40:", passed_students)
print("Students scoring 85 or above:", high_scorers)

# 6. Normalize marks using min-max scaling
normalized_marks = (
    (marks - np.min(marks)) /
    (np.max(marks) - np.min(marks))
)

print("\n--- Normalization ---")
print("Normalized Marks:", np.round(normalized_marks, 2))

# 7. Analyze marks by subject
scores = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [73, 81, 90],
    [90, 93, 87]
])

print("\n--- Subject-wise Analysis ---")
print("Subject Averages:", np.mean(scores, axis=0))
print("Student Averages:", np.mean(scores, axis=1))