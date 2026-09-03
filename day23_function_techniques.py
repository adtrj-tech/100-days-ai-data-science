# Day 23 - Advanced Function Techniques
# 100 Days of AI & Data Science


# 1. *args - accepts multiple positional arguments
def calculate_total(*numbers):
    return sum(numbers)


total = calculate_total(10, 20, 30, 40, 50)

print("Total:", total)


# 2. **kwargs - accepts multiple keyword arguments
def display_student(**details):
    print("\nStudent Details:")

    for key, value in details.items():
        print(f"{key}: {value}")


display_student(
    name="Adith",
    course="B.Tech IT",
    goal="AI & Data Science"
)


# 3. Lambda function
square = lambda number: number ** 2

print("\nSquare of 6:", square(6))


# 4. map() with lambda
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(
    map(lambda number: number ** 2, numbers)
)

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)


# 5. filter() with lambda
marks = [45, 67, 82, 39, 91, 56, 74]

passed_marks = list(
    filter(lambda mark: mark >= 50, marks)
)

print("\nMarks:", marks)
print("Passed marks:", passed_marks)