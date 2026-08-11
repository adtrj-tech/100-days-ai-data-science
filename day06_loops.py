# Day 6 - Loops in Python

print("=== For Loop ===")

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


print("\n=== Multiplication Table ===")

# Print multiplication table of 5
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


print("\n=== While Loop ===")

# Print numbers from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1


print("\n=== Sum of Numbers ===")

# Find the sum of numbers from 1 to 10
total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print("Sum from 1 to 10:", total)