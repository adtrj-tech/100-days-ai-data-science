# Day 19 - Python Problem Solving
# Problem: Find duplicate elements in a list


numbers = [10, 20, 30, 20, 40, 50, 10, 60, 30, 70]

duplicates = []
seen = set()

for number in numbers:
    if number in seen:
        if number not in duplicates:
            duplicates.append(number)
    else:
        seen.add(number)

print("Original list:", numbers)
print("Duplicate elements:", duplicates)