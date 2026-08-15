# Day 9 - Strings in Python

print("=== Python Strings ===")

text = input("Enter a sentence: ")

# Basic string information
print("\n--- String Information ---")
print("Original:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Searching inside a string
print("\n--- Searching ---")

word = input("Enter a word to search for: ")

if word.lower() in text.lower():
    print("The word was found in the sentence.")
else:
    print("The word was not found in the sentence.")

# Counting characters
print("\n--- Character Analysis ---")

print("Number of 'a' characters:", text.lower().count("a"))

# Splitting a sentence into words
words = text.split()

print("Number of words:", len(words))
print("Words:", words)