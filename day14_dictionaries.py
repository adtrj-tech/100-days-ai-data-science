# Day 14 - Dictionaries in Python

print("=== Python Dictionaries ===")

# Creating a dictionary
student = {
    "name": "Adith Raj",
    "age": 22,
    "field": "AI & Data Science",
    "score": 85
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Field:", student["field"])
print("Score:", student["score"])

# Adding a new key-value pair
student["grade"] = "A"

print("\nAfter adding grade:")
print(student)

# Updating a value
student["score"] = 90

print("\nUpdated score:", student["score"])

# Checking whether a key exists
print("\nIs 'email' present?", "email" in student)

# Getting all keys and values
print("\nKeys:", student.keys())
print("Values:", student.values())

# Looping through a dictionary
print("\n--- Student Details ---")

for key, value in student.items():
    print(key, ":", value)