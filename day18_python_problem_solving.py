# Day 18 - Python Problem Solving
# Problem: Count the frequency of each character in a string

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("\nCharacter Frequency:")

for char, count in frequency.items():
    print(char, ":", count)