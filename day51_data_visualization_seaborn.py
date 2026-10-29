# Day 51: Data Visualization with Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a consistent visual theme
sns.set_theme(style="whitegrid")

# 1. Create a sample student performance dataset
data = {
    "student": [
        "A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L"
    ],
    "department": [
        "IT", "IT", "IT", "CSE", "CSE", "CSE",
        "ECE", "ECE", "ECE", "IT", "CSE", "ECE"
    ],
    "study_hours": [2, 4, 3, 6, 5, 7, 2, 4, 6, 5, 8, 3],
    "attendance": [60, 75, 70, 90, 85, 95, 65, 80, 92, 82, 98, 72],
    "marks": [40, 65, 55, 85, 78, 95, 45, 68, 88, 72, 98, 52]
}

df = pd.DataFrame(data)

print("--- Dataset Preview ---")
print(df.head())

print("\n--- Dataset Summary ---")
print(df.describe())

# 2. Bar plot: Average marks by department
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="department", y="marks", errorbar=None)
plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("day51_average_marks.png")
plt.show()

# 3. Scatter plot: Study hours vs marks
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="study_hours",
    y="marks",
    hue="department",
    s=100
)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("day51_study_hours_vs_marks.png")
plt.show()

# 4. Histogram: Distribution of marks
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="marks", bins=6, kde=True)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("day51_marks_distribution.png")
plt.show()

# 5. Box plot: Marks across departments
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="department", y="marks")
plt.title("Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("day51_marks_boxplot.png")
plt.show()

# 6. Heatmap: Correlation between numerical columns
numeric_df = df[["study_hours", "attendance", "marks"]]
correlation = numeric_df.corr()

plt.figure(figsize=(7, 5))
sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("day51_correlation_heatmap.png")
plt.show()

# 7. Pair plot: Relationships among numerical variables
pair_plot = sns.pairplot(
    df,
    vars=["study_hours", "attendance", "marks"],
    hue="department"
)
pair_plot.figure.suptitle(
    "Relationships in Student Performance Data",
    y=1.02
)
pair_plot.savefig("day51_pairplot.png")
plt.show()

# 8. Print a few observations
print("\n--- Key Statistics ---")
print("Average marks:", round(df["marks"].mean(), 2))
print("Highest marks:", df["marks"].max())
print("Lowest marks:", df["marks"].min())

print("\nAverage marks by department:")
print(df.groupby("department")["marks"].mean().round(2))

print("\nCorrelation with marks:")
print(correlation["marks"].round(2))

print("\nDay 51 completed! Charts saved as PNG files.")
