import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats


np.random.seed(42)


# -----------------------------------------
# 1. Generate Sample Data
# -----------------------------------------

customer_spending = np.random.normal(
    loc=1500,
    scale=300,
    size=100
)

sample_mean = np.mean(customer_spending)
sample_std = np.std(customer_spending, ddof=1)
sample_size = len(customer_spending)

print("SAMPLE STATISTICS")
print("-----------------")
print("Sample Size:", sample_size)
print("Sample Mean:", round(sample_mean, 2))
print("Sample Standard Deviation:", round(sample_std, 2))


# -----------------------------------------
# 2. Calculate 95% Confidence Interval
# Using t-distribution
# -----------------------------------------

confidence_level = 0.95
degrees_of_freedom = sample_size - 1

t_critical = stats.t.ppf(
    (1 + confidence_level) / 2,
    df=degrees_of_freedom
)

standard_error = sample_std / np.sqrt(sample_size)

margin_of_error = t_critical * standard_error

lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print("\nCONFIDENCE INTERVAL")
print("-------------------")
print("Confidence Level: 95%")
print("Lower Bound:", round(lower_bound, 2))
print("Upper Bound:", round(upper_bound, 2))


# -----------------------------------------
# 3. Hypothesis Testing
# One-sample t-test
# -----------------------------------------

# Company claims average spending is Rs. 1400

population_claim = 1400

t_statistic, p_value = stats.ttest_1samp(
    customer_spending,
    popmean=population_claim
)

alpha = 0.05

print("\nHYPOTHESIS TESTING")
print("------------------")

print("Null Hypothesis: Mean spending = 1400")
print("Alternative Hypothesis: Mean spending != 1400")

print("T-statistic:", round(t_statistic, 4))
print("P-value:", round(p_value, 6))

if p_value < alpha:
    print("Decision: Reject Null Hypothesis")
else:
    print("Decision: Fail to Reject Null Hypothesis")


# -----------------------------------------
# 4. Visualize Confidence Interval
# -----------------------------------------

plt.figure(figsize=(9, 5))

plt.errorbar(
    x=sample_mean,
    y=1,
    xerr=margin_of_error,
    fmt="o",
    capsize=8
)

plt.axvline(
    population_claim,
    linestyle="--",
    label="Company Claim"
)

plt.title("95% Confidence Interval")
plt.xlabel("Customer Spending")
plt.yticks([])
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("day56_confidence_interval.png")
plt.show()


# -----------------------------------------
# 5. Two-Sample Hypothesis Testing
# -----------------------------------------

# Compare old website and new website

old_website = np.random.normal(
    loc=1500,
    scale=250,
    size=100
)

new_website = np.random.normal(
    loc=1600,
    scale=250,
    size=100
)

t_stat, p_value = stats.ttest_ind(
    old_website,
    new_website,
    equal_var=False
)

print("\nTWO-SAMPLE T-TEST")
print("-----------------")

print("Old Website Mean:", round(np.mean(old_website), 2))
print("New Website Mean:", round(np.mean(new_website), 2))

print("T-statistic:", round(t_stat, 4))
print("P-value:", round(p_value, 6))

if p_value < alpha:
    print("Significant difference detected.")
else:
    print("No statistically significant difference detected.")


# -----------------------------------------
# 6. Summary
# -----------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Sample Mean",
        "Sample Standard Deviation",
        "Standard Error",
        "CI Lower Bound",
        "CI Upper Bound",
        "One Sample Test P-value"
    ],

    "Value": [
        sample_mean,
        sample_std,
        standard_error,
        lower_bound,
        upper_bound,
        p_value
    ]
})

print("\nSTATISTICAL SUMMARY")
print("-------------------")
print(summary.to_string(index=False))