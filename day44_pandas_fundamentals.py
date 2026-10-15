# Day 44: Pandas Fundamentals
# #100DaysOfAIwithAdhi

import pandas as pd

# 1. Create a dictionary of student data
data = {
    "Name": ["Adith", "Anaswara", "Sayooj", "Avanthika", "Vishnu"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Marks": [85, 92, 78, 88, 95],
    "Age": [22, 21, 22, 21, 23]
}

# 2. Create a DataFrame
df = pd.DataFrame(data)

print("--- Student Dataset ---")
print(df)

# 3. Display the first and last rows
print("\n--- First 3 Rows ---")
print(df.head(3))

print("\n--- Last 2 Rows ---")
print(df.tail(2))

# 4. Explore the dataset
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Dataset Information ---")
df.info()

# 5. Select a single column
print("\n--- Student Names ---")
print(df["Name"])

# 6. Select multiple columns
print("\n--- Names and Marks ---")
print(df[["Name", "Marks"]])

# 7. Generate descriptive statistics
print("\n--- Numerical Summary ---")
print(df.describe())

# 8. Calculate the average marks
print("\n--- Average Marks ---")
print(df["Marks"].mean())

# 9. Count students by department
print("\n--- Students by Department ---")
print(df["Department"].value_counts())

# 10. Save the DataFrame as a CSV file
df.to_csv("day44_students.csv", index=False)

print("\nDataset saved to day44_students.csv")