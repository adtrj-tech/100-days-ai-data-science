import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------
# 1. Generate Dataset
# ---------------------------------------

np.random.seed(42)

number_of_students = 200

study_hours = np.random.uniform(
    1, 10, number_of_students
)

sleep_hours = np.random.uniform(
    4, 9, number_of_students
)

attendance = np.random.uniform(
    50, 100, number_of_students
)

exam_score = (
    5 * study_hours
    + 2 * sleep_hours
    + 0.2 * attendance
    + np.random.normal(0, 8, number_of_students)
)

exam_score = np.clip(exam_score, 0, 100)

df = pd.DataFrame({
    "study_hours": study_hours,
    "sleep_hours": sleep_hours,
    "attendance": attendance,
    "exam_score": exam_score
})


# ---------------------------------------
# 2. Explore Dataset
# ---------------------------------------

print("\nDATASET OVERVIEW")
print("----------------")

print(df.head())

print("\nSTATISTICAL SUMMARY")

print(df.describe().round(2))


# ---------------------------------------
# 3. Pearson Correlation
# ---------------------------------------

pearson_corr = df.corr(method="pearson")

print("\nPEARSON CORRELATION MATRIX")
print("--------------------------")

print(pearson_corr.round(2))


# ---------------------------------------
# 4. Spearman Correlation
# ---------------------------------------

spearman_corr = df.corr(method="spearman")

print("\nSPEARMAN CORRELATION MATRIX")
print("---------------------------")

print(spearman_corr.round(2))


# ---------------------------------------
# 5. Correlation with Exam Score
# ---------------------------------------

print("\nCORRELATION WITH EXAM SCORE")
print("---------------------------")

score_corr = pearson_corr["exam_score"].sort_values(
    ascending=False
)

print(score_corr.round(2))


# ---------------------------------------
# 6. Correlation Heatmap
# ---------------------------------------

plt.figure(figsize=(9, 6))

sns.heatmap(
    pearson_corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Student Performance Correlation Heatmap")

plt.tight_layout()

plt.savefig("day58_correlation_heatmap.png")

plt.show()


# ---------------------------------------
# 7. Study Hours vs Exam Score
# ---------------------------------------

plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="study_hours",
    y="exam_score"
)

plt.title("Study Hours vs Exam Score")

plt.xlabel("Study Hours")

plt.ylabel("Exam Score")

plt.tight_layout()

plt.savefig("day58_study_hours_correlation.png")

plt.show()


# ---------------------------------------
# 8. Pearson vs Spearman Comparison
# ---------------------------------------

comparison = pd.DataFrame({
    "Pearson": pearson_corr["exam_score"],
    "Spearman": spearman_corr["exam_score"]
})

print("\nPEARSON VS SPEARMAN")
print("-------------------")

print(comparison.round(3))


# ---------------------------------------
# 9. Identify Strong Correlations
# ---------------------------------------

print("\nSTRONG CORRELATIONS")
print("-------------------")

for column in df.columns:

    if column != "exam_score":

        value = pearson_corr.loc[
            column, "exam_score"
        ]

        if abs(value) >= 0.5:

            print(
                f"{column}: Strong correlation ({value:.2f})"
            )

        else:

            print(
                f"{column}: Weak or moderate correlation ({value:.2f})"
            )