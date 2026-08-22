# Day 17 - Nested Dictionaries
# Working with structured and nested data

students = {
    "student_001": {
        "name": "Adith",
        "age": 22,
        "course": "Information Technology",
        "skills": {
            "Python": 85,
            "SQL": 78,
            "Machine Learning": 72
        }
    },
    "student_002": {
        "name": "Rahul",
        "age": 22,
        "course": "Computer Science",
        "skills": {
            "Python": 90,
            "SQL": 82,
            "Machine Learning": 88
        }
    }
}

print("=== Student Information ===")

# Accessing nested dictionary values
student = students["student_001"]

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

print("\n--- Skills ---")

for skill, score in student["skills"].items():
    print(skill, ":", score)

# Finding the average skill score
scores = student["skills"].values()

average_score = sum(scores) / len(scores)

print("\nAverage Skill Score:", round(average_score, 2))

# Accessing another student's data
print("\n=== Second Student ===")

student_2 = students["student_002"]

print("Name:", student_2["name"])
print("Python Score:", student_2["skills"]["Python"])
print("Machine Learning Score:", student_2["skills"]["Machine Learning"])