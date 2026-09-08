# Day 25 - File Handling
# 100 Days of AI & Data Science


# Student data
students = [
    "Adith - IT - 85",
    "Rahul - CSE - 78",
    "Anu - ECE - 92",
    "Arjun - IT - 67",
    "Vishnu - CSE - 81"
]


# 1. Writing data to a file
with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("Student data written successfully.")


# 2. Reading data from the file
print("\n--- Student Records ---")

with open("students.txt", "r") as file:
    data = file.read()

print(data)


# 3. Reading line by line
print("--- Reading Line by Line ---")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


# 4. Appending new data
with open("students.txt", "a") as file:
    file.write("Meera - ECE - 88\n")

print("\nNew student added successfully.")


# 5. Display updated data
print("\n--- Updated Student Records ---")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())