# Day 13 - Tuples and Sets

print("=== Tuples ===")

# A tuple is ordered and cannot be changed after creation
student = ("Adith Raj", 22, "AI & Data Science")

print("Student details:", student)
print("Name:", student[0])
print("Age:", student[1])
print("Field:", student[2])

print("\n=== Sets ===")

# A set stores unique values
skills = {"Python", "SQL", "Python", "Machine Learning", "SQL"}

print("Skills:", skills)

# Adding a new item
skills.add("Data Science")
print("After adding:", skills)

# Removing an item
skills.remove("SQL")
print("After removing SQL:", skills)

# Checking membership
print("Is Python present?", "Python" in skills)

print("\n=== Removing Duplicates ===")

# Sets can be used to remove duplicate values
marks = [85, 90, 85, 72, 90, 78, 72]

unique_marks = set(marks)

print("Original marks:", marks)
print("Unique marks:", unique_marks)