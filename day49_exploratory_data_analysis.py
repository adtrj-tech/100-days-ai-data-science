# Day 49: Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a sample student performance dataset
data = {
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108, 108],
    "study_hours": [2, 4, 1, 6, 5, 3, 7, 4, 4],
    "attendance": [65, 80, 55, 95, 85, 70, 98, 88, 88],
    "marks": [45, 68, 35, 92, 78, None, 96, 72, 72],
    "department": [
        "IT", "CSE", "IT", "CSE", "ECE",
        "IT", "CSE", "ECE", "ECE"
    ]
}

df = pd.DataFrame(data)

# 2. Understand the dataset
print("\n--- First Five Rows ---")
print(df.head())

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Information ---")
df.info()

# 3. Check missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 4. Check duplicate records
print("\n--- Duplicate Rows ---")
print(df.duplicated().sum())

# 5. Explore numerical columns
print("\n--- Descriptive Statistics ---")
print(df.describe())

# 6. Explore categorical columns
print("\n--- Department Distribution ---")
print(df["department"].value_counts())

# 7. Analyze average marks by department
print("\n--- Average Marks by Department ---")
print(
    df.groupby("department")["marks"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

# 8. Explore relationships between numerical columns
print("\n--- Correlation Matrix ---")
print(
    df[["study_hours", "attendance", "marks"]]
    .corr()
    .round(2)
)

# 9. Clean the dataset
clean_df = df.drop_duplicates().copy()

# Fill missing marks with the median
clean_df["marks"] = clean_df["marks"].fillna(
    clean_df["marks"].median()
)

print("\n--- Cleaned Dataset Summary ---")
print("Rows before cleaning:", len(df))
print("Rows after cleaning:", len(clean_df))
print("Missing values after cleaning:")
print(clean_df.isnull().sum())

# 10. Visualize the data
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Marks distribution
axes[0].hist(
    clean_df["marks"],
    bins=5,
    edgecolor="black"
)
axes[0].set_title("Distribution of Marks")
axes[0].set_xlabel("Marks")
axes[0].set_ylabel("Number of Students")

# Study hours vs marks
axes[1].scatter(
    clean_df["study_hours"],
    clean_df["marks"]
)
axes[1].set_title("Study Hours vs Marks")
axes[1].set_xlabel("Study Hours")
axes[1].set_ylabel("Marks")

# Average marks by department
department_marks = clean_df.groupby("department")["marks"].mean()

axes[2].bar(
    department_marks.index,
    department_marks.values
)
axes[2].set_title("Average Marks by Department")
axes[2].set_xlabel("Department")
axes[2].set_ylabel("Average Marks")

plt.tight_layout()
plt.show()

# 11. Export the cleaned dataset
clean_df.to_csv("day49_cleaned_student_data.csv", index=False)

print("\nEDA completed successfully!")
print("Cleaned dataset saved to day49_cleaned_student_data.csv")
