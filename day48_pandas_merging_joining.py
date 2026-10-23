# Day 48: Pandas Merging & Joining

import pandas as pd

# 1. Create an employee DataFrame
employees = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105],
    "name": ["Adith", "Anaswara", "Sayooj", "Avanthika", "Vishnu"],
    "department_id": [1, 2, 1, 3, 1],
    "salary": [60000, 45000, 75000, 55000, 50000]
})

# 2. Create a department DataFrame
departments = pd.DataFrame({
    "department_id": [1, 2, 3, 4],
    "department": ["IT", "HR", "Finance", "Marketing"],
    "location": ["Kochi", "Bangalore", "Chennai", "Mumbai"]
})

print("--- Employees ---")
print(employees)

print("\n--- Departments ---")
print(departments)

# 3. INNER MERGE
# Keep only employees whose department_id matches
print("\n--- Inner Merge ---")
inner_result = pd.merge(
    employees, departments,
    on="department_id",
    how="inner"
)
print(inner_result)

# 4. LEFT MERGE
# Keep every employee, including unmatched employees
print("\n--- Left Merge ---")
left_result = pd.merge(
    employees, departments,
    on="department_id",
    how="left"
)
print(left_result)

# 5. RIGHT MERGE
# Keep every department, including departments without employees
print("\n--- Right Merge ---")
right_result = pd.merge(
    employees, departments,
    on="department_id",
    how="right"
)
print(right_result)

# 6. OUTER MERGE
# Keep all employees and all departments
print("\n--- Outer Merge ---")
outer_result = pd.merge(
    employees, departments,
    on="department_id",
    how="outer"
)
print(outer_result)

# 7. Merge and select specific columns
print("\n--- Employee Names and Locations ---")
location_report = pd.merge(
    employees[["name", "department_id", "salary"]],
    departments[["department_id", "department", "location"]],
    on="department_id",
    how="inner"
)
print(location_report)

# 8. Analyze the merged data
print("\n--- Average Salary by Department ---")
salary_summary = (
    inner_result.groupby("department")["salary"]
    .mean()
    .sort_values(ascending=False)
)
print(salary_summary)

# 9. Save the merged report
location_report.to_csv(
    "day48_employee_department_report.csv",
    index=False
)

print("\nReport saved to day48_employee_department_report.csv")