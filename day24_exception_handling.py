# Day 24 - Exception Handling
# 100 Days of AI & Data Science


# Function to calculate average marks
def calculate_average(marks):
    try:
        average = sum(marks) / len(marks)
        return average

    except ZeroDivisionError:
        return 0


# Taking marks as input
marks = []

print("Enter marks for 5 subjects:")

for i in range(5):
    try:
        mark = float(input(f"Subject {i + 1}: "))

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            continue

        marks.append(mark)

    except ValueError:
        print("Invalid input! Please enter a number.")


# Calculate result
try:
    average = calculate_average(marks)

    print("\n--- Student Result ---")
    print("Marks:", marks)
    print("Average:", average)

except Exception as error:
    print("Something went wrong:", error)

finally:
    print("\nProgram execution completed.")