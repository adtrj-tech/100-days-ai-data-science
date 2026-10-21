# Day 47: Pandas Grouping & Aggregation
# #100DaysOfAIwithAdhi

import pandas as pd

# 1. Create a sample employee dataset
data = {
    "Name": [
        "Adith", "Anaswara", "Sayooj",
        "Avanthika", "Vishnu", "Rahul"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", "IT", "HR"
    ],
    "Salary": [60000, 45000, 75000, 55000, 50000, 48000],
    "Experience": [2, 1, 3, 2, 1, 2]
}

df = pd.DataFrame(data)

print("--- Employee Dataset ---")
print(df)

# 2. Count employees in each department
print("\n--- Employee Count by Department ---")
print(df.groupby("Department").size())

# 3. Calculate average salary by department
print("\n--- Average Salary by Department ---")
print(df.groupby("Department")["Salary"].mean())

# 4. Calculate total salary by department
print("\n--- Total Salary by Department ---")
print(df.groupby("Department")["Salary"].sum())

# 5. Find maximum and minimum salaries by department
print("\n--- Salary Range by Department ---")
print(
    df.groupby("Department")["Salary"]
    .agg(["min", "max"])
)

# 6. Calculate multiple statistics together
print("\n--- Department Salary Summary ---")
summary = df.groupby("Department")["Salary"].agg(
    ["count", "mean", "min", "max", "sum"]
)
print(summary.round(2))

# 7. Group by department and experience
print("\n--- Average Salary by Department and Experience ---")
print(
    df.groupby(["Department", "Experience"])["Salary"]
    .mean()
)

# 8. Sort departments by average salary
print("\n--- Departments Ranked by Average Salary ---")
average_salary = (
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)
print(average_salary)

# 9. Filter departments with average salary above 50000
print("\n--- Departments with Average Salary Above 50000 ---")
filtered = average_salary[average_salary > 50000]
print(filtered)

# 10. Create a clean summary DataFrame
report = (
    df.groupby("Department")
    .agg(
        employee_count=("Name", "count"),
        average_salary=("Salary", "mean"),
        total_salary=("Salary", "sum")
    )
    .reset_index()
)

print("\n--- Final Department Report ---")
print(report.round(2))

# 11. Export the report
report.to_csv("day47_department_summary.csv", index=False)

print("\nReport saved to day47_department_summary.csv")