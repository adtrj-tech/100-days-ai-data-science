# Day 11 - Lists in Python

print("=== Python Lists ===")

# Creating a list
marks = [78, 85, 92, 67, 74]

print("Marks:", marks)

# Accessing elements
print("\n--- Accessing Elements ---")
print("First mark:", marks[0])
print("Last mark:", marks[-1])

# Adding an element
marks.append(88)
print("\nAfter adding a mark:", marks)

# Removing an element
marks.remove(67)
print("After removing 67:", marks)

# Sorting the list
marks.sort()
print("Sorted marks:", marks)

# Finding basic information
print("\n--- List Analysis ---")
print("Number of marks:", len(marks))
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Total marks:", sum(marks))

# Calculating average
average = sum(marks) / len(marks)
print("Average:", average)

# Processing the list with a loop
print("\n--- Marks using a loop ---")

for mark in marks:
    print(mark)