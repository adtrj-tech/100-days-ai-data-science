# Day 42: NumPy Indexing, Slicing & Reshaping
# #100DaysOfAIwithAdhi

import numpy as np

# 1. Create a NumPy array
marks = np.array([78, 85, 92, 67, 88, 95])

print("Original Array:", marks)

# 2. Access individual elements
print("First Element:", marks[0])
print("Last Element:", marks[-1])

# 3. Slice the array
print("First Three Elements:", marks[:3])
print("Elements from Index 2 to 4:", marks[2:5])
print("Every Second Element:", marks[::2])

# 4. Update an element
marks[1] = 90
print("Updated Array:", marks)

# 5. Create a 2D array
scores = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [81, 76, 89],
    [90, 93, 87]
])

print("\nOriginal 2D Array:")
print(scores)

# 6. Access rows and individual elements
print("First Row:", scores[0])
print("Element at Row 2, Column 3:", scores[1, 2])

# 7. Slice rows and columns
print("First Two Rows:")
print(scores[:2])

print("First Column:")
print(scores[:, 0])

print("First Two Rows, First Two Columns:")
print(scores[:2, :2])

# 8. Reshape the array
numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)

print("\nOriginal Numbers:", numbers)
print("Reshaped Matrix:")
print(matrix)

# 9. Check array dimensions and shape
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Total Elements:", matrix.size)