# Day 7 - Functions in Python

print("=== Python Functions ===")


# Function to greet a user
def greet(name):
    return f"Hello, {name}!"


# Function to calculate the square of a number
def square(number):
    return number * number


# Function to check whether a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Function to calculate the sum from 1 to n
def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# Taking input
name = input("Enter your name: ")
number = int(input("Enter a number: "))

# Calling functions
print("\n" + greet(name))
print("Square:", square(number))
print("Number is:", check_even_odd(number))
print("Sum from 1 to", number, ":", calculate_sum(number))