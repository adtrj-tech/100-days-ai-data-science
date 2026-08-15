# Day 10 - String Indexing & Slicing

print("=== String Indexing & Slicing ===")

text = input("Enter a word or sentence: ")

print("\n--- Indexing ---")

print("First character:", text[0])
print("Last character:", text[-1])

print("\n--- Slicing ---")

print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])
print("Every second character:", text[::2])
print("Reversed:", text[::-1])

print("\n--- String Analysis ---")

print("Length:", len(text))

if text.lower() == text.lower()[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")