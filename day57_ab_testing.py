import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.stats.proportion import (
    proportions_ztest,
    proportion_confint
)

np.random.seed(42)


# ---------------------------------------
# 1. Simulate A/B Testing Data
# ---------------------------------------

visitors_a = 1000
visitors_b = 1000

# Simulate purchases
purchases_a = np.random.binomial(
    n=1,
    p=0.10,
    size=visitors_a
)

purchases_b = np.random.binomial(
    n=1,
    p=0.13,
    size=visitors_b
)

conversions_a = np.sum(purchases_a)
conversions_b = np.sum(purchases_b)


# ---------------------------------------
# 2. Calculate Conversion Rates
# ---------------------------------------

conversion_rate_a = (
    conversions_a / visitors_a
) * 100

conversion_rate_b = (
    conversions_b / visitors_b
) * 100

print("A/B TESTING RESULTS")
print("-------------------")

print("Version A Conversions:", conversions_a)
print("Version B Conversions:", conversions_b)

print("Version A Conversion Rate:",
      round(conversion_rate_a, 2), "%")

print("Version B Conversion Rate:",
      round(conversion_rate_b, 2), "%")


# ---------------------------------------
# 3. Calculate Relative Improvement
# ---------------------------------------

relative_improvement = (
    (conversion_rate_b - conversion_rate_a)
    / conversion_rate_a
) * 100

print("\nRELATIVE IMPROVEMENT")
print("--------------------")

print(
    "Improvement:",
    round(relative_improvement, 2),
    "%"
)


# ---------------------------------------
# 4. Two-Proportion Z-Test
# ---------------------------------------

successes = np.array([
    conversions_a,
    conversions_b
])

sample_sizes = np.array([
    visitors_a,
    visitors_b
])

z_stat, p_value = proportions_ztest(
    count=successes,
    nobs=sample_sizes,
    alternative="two-sided"
)

alpha = 0.05

print("\nHYPOTHESIS TESTING")
print("------------------")

print("Z-statistic:", round(z_stat, 4))
print("P-value:", round(p_value, 6))

if p_value < alpha:
    print("Result: Statistically significant difference")
else:
    print("Result: No statistically significant difference")


# ---------------------------------------
# 5. Confidence Intervals
# ---------------------------------------

ci_a = proportion_confint(
    conversions_a,
    visitors_a,
    alpha=0.05,
    method="wilson"
)

ci_b = proportion_confint(
    conversions_b,
    visitors_b,
    alpha=0.05,
    method="wilson"
)

print("\n95% CONFIDENCE INTERVALS")
print("------------------------")

print(
    "Version A:",
    round(ci_a[0] * 100, 2),
    "% to",
    round(ci_a[1] * 100, 2),
    "%"
)

print(
    "Version B:",
    round(ci_b[0] * 100, 2),
    "% to",
    round(ci_b[1] * 100, 2),
    "%"
)


# ---------------------------------------
# 6. Create Results DataFrame
# ---------------------------------------

results = pd.DataFrame({
    "Version": ["A", "B"],
    "Visitors": [visitors_a, visitors_b],
    "Conversions": [conversions_a, conversions_b],
    "Conversion Rate": [
        conversion_rate_a,
        conversion_rate_b
    ]
})

print("\nFINAL RESULTS")
print("-------------")

print(results.to_string(index=False))


# ---------------------------------------
# 7. Visualize Conversion Rates
# ---------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    ["Version A", "Version B"],
    [conversion_rate_a, conversion_rate_b]
)

plt.title("A/B Testing - Conversion Rate Comparison")
plt.ylabel("Conversion Rate (%)")
plt.xlabel("Website Version")

plt.tight_layout()

plt.savefig("day57_conversion_comparison.png")

plt.show()