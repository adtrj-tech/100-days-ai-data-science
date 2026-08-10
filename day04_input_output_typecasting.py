# Day 4 - Input, Output & Type Casting

print("=== Student Information ===")

# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))

# Displaying the information
print("\n--- Your Information ---")
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)

# Type Casting
age_in_5_years = age + 5

print("\nIn 5 years, you will be", age_in_5_years, "years old.")

# Checking data types
print("\n--- Data Types ---")
print("Name:", type(name))
print("Age:", type(age))
print("CGPA:", type(cgpa))