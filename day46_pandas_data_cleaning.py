# Day 46: Pandas Data Cleaning
# #100DaysOfAIwithAdhi

import pandas as pd

# 1. Create a sample dataset with data quality issues
data = {
    "Name": ["Adith", "Anaswara", "Sayooj", "Avanthika",
             "Vishnu", "Sayooj", None],
    "Department": ["IT", "HR", "IT", "Finance",
                   "IT", "IT", "HR"],
    "Age": [22, 21, None, 21, 23, None, 22],
    "Marks": [85, 92, 78, None, 95, 78, 88],
    "Salary": [60000, 45000, 75000, 55000,
               50000, 75000, 48000]
}

df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df)

# 2. Inspect missing values
print("\n--- Missing Values Per Column ---")
print(df.isnull().sum())

# 3. Calculate the percentage of missing values
print("\n--- Missing Value Percentage ---")
print((df.isnull().mean() * 100).round(2))

# 4. Fill missing ages with the median age
df["Age"] = df["Age"].fillna(df["Age"].median())

# 5. Fill missing marks with the average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# 6. Handle missing names
df["Name"] = df["Name"].fillna("Unknown")

# 7. Detect duplicate records
print("\n--- Duplicate Records ---")
print(df[df.duplicated()])

# 8. Remove exact duplicate rows
df = df.drop_duplicates()

# 9. Check and correct data types
print("\n--- Data Types Before Correction ---")
print(df.dtypes)

df["Age"] = df["Age"].astype(int)

print("\n--- Data Types After Correction ---")
print(df.dtypes)

# 10. Check the cleaned dataset
print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())

print("\n--- Cleaned Dataset ---")
print(df)

# 11. Save the cleaned dataset
df.to_csv("day46_cleaned_data.csv", index=False)

print("\nCleaned dataset saved to day46_cleaned_data.csv")