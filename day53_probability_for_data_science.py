# Day 53: Probability for Data Science

import random

# --------------------------------------------------
# 1. Basic Probability
# --------------------------------------------------

# Probability = Favorable outcomes / Total possible outcomes

total_outcomes = 6
favorable_outcomes = 1  # Rolling a 6

probability_of_six = favorable_outcomes / total_outcomes

print("--- Basic Probability ---")
print("Probability of rolling a 6:", probability_of_six)
print("Percentage:", probability_of_six * 100, "%")


# --------------------------------------------------
# 2. Sample Space and Events
# --------------------------------------------------

dice_sample_space = {1, 2, 3, 4, 5, 6}

even_numbers = {2, 4, 6}
probability_even = len(even_numbers) / len(dice_sample_space)

print("\n--- Sample Space and Events ---")
print("Sample space:", dice_sample_space)
print("Even outcomes:", even_numbers)
print("Probability of an even number:", probability_even)


# --------------------------------------------------
# 3. Simulate Dice Rolls
# --------------------------------------------------

number_of_rolls = 10000
six_count = 0

for _ in range(number_of_rolls):
    roll = random.randint(1, 6)

    if roll == 6:
        six_count += 1

experimental_probability = six_count / number_of_rolls

print("\n--- Dice Roll Simulation ---")
print("Number of rolls:", number_of_rolls)
print("Number of times 6 appeared:", six_count)
print("Experimental probability:", round(experimental_probability, 4))
print("Theoretical probability:", round(1 / 6, 4))


# --------------------------------------------------
# 4. Independent Events
# --------------------------------------------------

# Example: Tossing a coin twice
# Probability of heads on each toss = 1/2

probability_heads = 1 / 2

probability_two_heads = probability_heads * probability_heads

print("\n--- Independent Events ---")
print("Probability of heads on one toss:", probability_heads)
print("Probability of heads twice:", probability_two_heads)


# --------------------------------------------------
# 5. Conditional Probability
# --------------------------------------------------

# Example dataset: Students who studied and passed

students = {
    "A": {"studied": True, "passed": True},
    "B": {"studied": True, "passed": True},
    "C": {"studied": True, "passed": False},
    "D": {"studied": True, "passed": True},
    "E": {"studied": False, "passed": False},
    "F": {"studied": False, "passed": True},
    "G": {"studied": False, "passed": False},
    "H": {"studied": False, "passed": False}
}

studied_students = [
    student for student in students.values()
    if student["studied"]
]

studied_and_passed = [
    student for student in studied_students
    if student["passed"]
]

if len(studied_students) > 0:
    conditional_probability = (
        len(studied_and_passed) / len(studied_students)
    )
else:
    conditional_probability = 0

print("\n--- Conditional Probability ---")
print("Students who studied:", len(studied_students))
print("Students who studied and passed:", len(studied_and_passed))

print(
    "Probability of passing given that a student studied:",
    round(conditional_probability, 2)
)


# --------------------------------------------------
# 6. Probability of At Least One Event
# --------------------------------------------------

# Probability of getting at least one head in two coin tosses

probability_no_heads = (1 / 2) * (1 / 2)
probability_at_least_one_head = 1 - probability_no_heads

print("\n--- At Least One Event ---")
print("Probability of no heads:", probability_no_heads)
print("Probability of at least one head:", probability_at_least_one_head)


print("\nDay 53 completed successfully!")