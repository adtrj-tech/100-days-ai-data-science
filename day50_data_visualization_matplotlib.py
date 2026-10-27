# Day 50: Data Visualization with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a sample monthly sales dataset
data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [12000, 15000, 13500, 18000, 22000, 25000],
    "expenses": [8000, 9000, 8500, 11000, 13000, 14500],
    "customers": [120, 145, 138, 175, 210, 240]
}

df = pd.DataFrame(data)

# Calculate profit
df["profit"] = df["sales"] - df["expenses"]

print("--- Sales Dataset ---")
print(df)

# 2. Line chart: Sales trend
plt.figure(figsize=(8, 5))
plt.plot(
    df["month"], df["sales"],
    marker="o", label="Sales"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("day50_sales_trend.png")
plt.show()

# 3. Bar chart: Sales vs Expenses
plt.figure(figsize=(8, 5))
plt.bar(
    df["month"], df["sales"],
    label="Sales"
)
plt.bar(
    df["month"], df["expenses"],
    label="Expenses"
)
plt.title("Monthly Sales and Expenses")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.legend()
plt.tight_layout()
plt.savefig("day50_sales_expenses.png")
plt.show()

# 4. Scatter plot: Customers vs Sales
plt.figure(figsize=(8, 5))
plt.scatter(
    df["customers"], df["sales"],
    marker="o"
)
plt.title("Customers vs Sales")
plt.xlabel("Number of Customers")
plt.ylabel("Sales (₹)")
plt.grid(True)
plt.tight_layout()
plt.savefig("day50_customers_vs_sales.png")
plt.show()

# 5. Histogram: Distribution of sales
plt.figure(figsize=(8, 5))
plt.hist(
    df["sales"],
    bins=5,
    edgecolor="black"
)
plt.title("Distribution of Monthly Sales")
plt.xlabel("Sales (₹)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("day50_sales_distribution.png")
plt.show()

# 6. Compare monthly profit
plt.figure(figsize=(8, 5))
plt.bar(df["month"], df["profit"])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit (₹)")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("day50_monthly_profit.png")
plt.show()

# 7. Summary
print("\n--- Sales Insights ---")
print("Total sales:", df["sales"].sum())
print("Total expenses:", df["expenses"].sum())
print("Total profit:", df["profit"].sum())
print("Highest sales month:", df.loc[df["sales"].idxmax(), "month"])
print("Average monthly sales:", round(df["sales"].mean(), 2))

print("\nCharts saved successfully!")
