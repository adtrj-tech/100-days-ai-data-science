# Day 45: Pandas Data Selection & Filtering

import pandas as pd

# 1. Create a student dataset
data = {
    "Name": ["Adith", "Anaswara", "Sayooj", "Avanthika", "Vishnu", "Rahul"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR"],
    "Marks": [85, 92, 78, 88, 95, 72],
    "Age": [22, 21, 22, 21, 23, 22]
}

df = pd.DataFrame(data)

print("--- Complete Dataset ---")
print(df)

# 2. Select a single column
print("\n--- Student Names ---")
print(df["Name"])

# 3. Select multiple columns
print("\n--- Names and Marks ---")
print(df[["Name", "Marks"]])

# 4. Filter students scoring above 85
print("\n--- Marks Above 85 ---")
print(df[df["Marks"] > 85])

# 5. Filter students from the IT department
print("\n--- IT Department Students ---")
print(df[df["Department"] == "IT"])

# 6. Apply multiple conditions
print("\n--- IT Students Scoring Above 80 ---")
print(df[(df["Department"] == "IT") & (df["Marks"] > 80)])

# 7. Filter using OR
print("\n--- Students Scoring Below 80 OR Above 90 ---")
print(df[(df["Marks"] < 80) | (df["Marks"] > 90)])

# 8. Select rows using loc
print("\n--- Selected Rows Using loc ---")
print(df.loc[df["Marks"] >= 85, ["Name", "Marks"]])

# 9. Select rows by position using iloc
print("\n--- First Three Rows ---")
print(df.iloc[:3])

# 10. Filter using isin()
print("\n--- IT and HR Students ---")
print(df[df["Department"].isin(["IT", "HR"])])

# 11. Sort filtered results by marks
print("\n--- Top Scorers ---")
print(df[df["Marks"] >= 80].sort_values("Marks", ascending=False))