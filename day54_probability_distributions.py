# Day 54: Probability Distributions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import comb

# --------------------------------------------------
# 1. Random Variables
# --------------------------------------------------

# A random variable assigns a numerical value to an outcome.
# Example: X = number of heads in two coin tosses

sample_space = ["HH", "HT", "TH", "TT"]

number_of_heads = {
    "HH": 2,
    "HT": 1,
    "TH": 1,
    "TT": 0
}

print("--- Random Variable ---")

for outcome in sample_space:
    print(
        f"Outcome: {outcome}, "
        f"Number of heads: {number_of_heads[outcome]}"
    )


# --------------------------------------------------
# 2. Discrete Probability Distribution
# --------------------------------------------------

# X = number of heads in two fair coin tosses

values = [0, 1, 2]
probabilities = [0.25, 0.50, 0.25]

distribution = pd.DataFrame({
    "Number of Heads": values,
    "Probability": probabilities
})

print("\n--- Discrete Probability Distribution ---")
print(distribution)

print("Sum of probabilities:", sum(probabilities))


# --------------------------------------------------
# 3. Binomial Distribution
# --------------------------------------------------

# Example:
# A fair coin is tossed 5 times.
# X = number of heads.
#
# Formula:
# P(X = k) = C(n, k) * p^k * (1-p)^(n-k)

n = 5
p = 0.5

binomial_values = list(range(n + 1))
binomial_probabilities = []

for k in binomial_values:
    probability = (
        comb(n, k)
        * (p ** k)
        * ((1 - p) ** (n - k))
    )

    binomial_probabilities.append(probability)

binomial_df = pd.DataFrame({
    "Number of Heads": binomial_values,
    "Probability": binomial_probabilities
})

print("\n--- Binomial Distribution ---")
print(binomial_df)

print(
    "Probability of exactly 3 heads:",
    round(binomial_probabilities[3], 4)
)


# --------------------------------------------------
# 4. Simulate the Binomial Experiment
# --------------------------------------------------

number_of_experiments = 10000

simulation = np.random.binomial(
    n=n,
    p=p,
    size=number_of_experiments
)

simulation_df = pd.DataFrame({
    "Number of Heads": simulation
})

experimental_distribution = (
    simulation_df["Number of Heads"]
    .value_counts(normalize=True)
    .sort_index()
)

print("\n--- Experimental Probability ---")
print(experimental_distribution)


# --------------------------------------------------
# 5. Compare Theoretical and Experimental Probability
# --------------------------------------------------

comparison = pd.DataFrame({
    "Number of Heads": binomial_values,
    "Theoretical Probability": binomial_probabilities,
    "Experimental Probability": [
        experimental_distribution.get(k, 0)
        for k in binomial_values
    ]
})

print("\n--- Probability Comparison ---")
print(comparison.round(4))


# --------------------------------------------------
# 6. Visualize the Binomial Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    binomial_values,
    binomial_probabilities,
    width=0.6,
    label="Theoretical Probability"
)

plt.title("Binomial Distribution: 5 Coin Tosses")
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.xticks(binomial_values)
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("day54_binomial_distribution.png")
plt.show()


# --------------------------------------------------
# 7. Normal Distribution Simulation
# --------------------------------------------------

# Simulate exam marks with a mean of 70
# and standard deviation of 10.

normal_data = np.random.normal(
    loc=70,
    scale=10,
    size=1000
)

print("\n--- Normal Distribution Simulation ---")
print("Simulated mean:", round(np.mean(normal_data), 2))
print("Simulated standard deviation:", round(np.std(normal_data), 2))

plt.figure(figsize=(8, 5))

plt.hist(
    normal_data,
    bins=30,
    density=True,
    edgecolor="black"
)

plt.title("Simulated Normal Distribution of Exam Marks")
plt.xlabel("Marks")
plt.ylabel("Density")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("day54_normal_distribution.png")
plt.show()


print("\nDay 54 completed successfully!")