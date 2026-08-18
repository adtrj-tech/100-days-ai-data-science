# Day 12 - List Methods & List Comprehension

print("=== List Methods & Processing ===")

marks = [78, 45, 92, 67, 85, 55, 91]

print("Original marks:", marks)

# Add an element
marks.append(88)
print("\nAfter append:", marks)

# Insert an element
marks.insert(2, 75)
print("After insert:", marks)

# Remove an element
marks.remove(45)
print("After remove:", marks)

# Sort the list
marks.sort()
print("Sorted marks:", marks)

# Reverse the list
marks.reverse()
print("Reversed marks:", marks)

# Check whether a value exists
print("\nIs 85 present?", 85 in marks)

# Create a list of students who passed
passed_marks = [mark for mark in marks if mark >= 50]

print("\nPassed marks:", passed_marks)

# Create a list of marks above 80
high_marks = [mark for mark in marks if mark > 80]

print("Marks above 80:", high_marks)

# Calculate average
average = sum(marks) / len(marks)

print("\nTotal marks:", sum(marks))
print("Average marks:", average)