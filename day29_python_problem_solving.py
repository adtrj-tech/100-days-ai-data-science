# Day 29 - Python Problem Solving

# Problem 1: Find the second largest number
def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[1]


# Problem 2: Count character frequency
def character_frequency(text):
    frequency = {}

    for character in text.lower():
        if character != " ":
            frequency[character] = frequency.get(character, 0) + 1

    return frequency


# Problem 3: Find duplicate elements
def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)
        else:
            seen.add(number)

    return duplicates


# Problem 4: Check whether a string is a palindrome
def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")

    return cleaned_text == cleaned_text[::-1]


# Problem 5: Find the student with the highest marks
def find_top_student(students):
    top_student = None
    highest_mark = -1

    for student in students:
        if student["marks"] > highest_mark:
            highest_mark = student["marks"]
            top_student = student["name"]

    return top_student


# Testing the functions

numbers = [10, 20, 5, 20, 40, 30, 40]

print("--- Problem 1: Second Largest ---")
print("Numbers:", numbers)
print("Second largest:", find_second_largest(numbers))


print("\n--- Problem 2: Character Frequency ---")
text = "python programming"
print("Text:", text)
print("Frequency:", character_frequency(text))


print("\n--- Problem 3: Duplicate Elements ---")
print("Numbers:", numbers)
print("Duplicates:", find_duplicates(numbers))


print("\n--- Problem 4: Palindrome ---")
word = "madam"
print("Word:", word)
print("Is palindrome:", is_palindrome(word))


print("\n--- Problem 5: Top Student ---")
students = [
    {"name": "Adith", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Anu", "marks": 88}
]

print("Top student:", find_top_student(students))