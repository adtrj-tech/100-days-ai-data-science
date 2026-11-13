import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Create a Population
# -----------------------------------

np.random.seed(42)

population = np.random.exponential(
    scale=50,
    size=100000
)

population_mean = np.mean(population)
population_std = np.std(population)

print("POPULATION STATISTICS")
print("---------------------")
print("Population Size:", len(population))
print("Population Mean:", round(population_mean, 2))
print("Population Std:", round(population_std, 2))


# -----------------------------------
# 2. Simple Random Sampling
# -----------------------------------

sample = np.random.choice(
    population,
    size=100,
    replace=False
)

sample_mean = np.mean(sample)

print("\nSAMPLE STATISTICS")
print("-----------------")
print("Sample Size:", len(sample))
print("Sample Mean:", round(sample_mean, 2))


# -----------------------------------
# 3. Sampling Distribution
# -----------------------------------

sample_means = []

number_of_samples = 1000
sample_size = 50

for _ in range(number_of_samples):

    current_sample = np.random.choice(
        population,
        size=sample_size,
        replace=False
    )

    sample_means.append(np.mean(current_sample))

sample_means = np.array(sample_means)

print("\nSAMPLING DISTRIBUTION")
print("---------------------")
print("Number of Samples:", number_of_samples)
print("Sample Size:", sample_size)
print("Mean of Sample Means:", round(np.mean(sample_means), 2))


# -----------------------------------
# 4. Standard Error
# -----------------------------------

standard_error = population_std / np.sqrt(sample_size)

print("\nSTANDARD ERROR")
print("---------------")
print("Theoretical SE:", round(standard_error, 2))
print(
    "Experimental SE:",
    round(np.std(sample_means, ddof=1), 2)
)


# -----------------------------------
# 5. Visualize CLT
# -----------------------------------

plt.figure(figsize=(12, 5))

# Original population distribution
plt.subplot(1, 2, 1)

plt.hist(
    population,
    bins=50,
    density=True
)

plt.title("Original Population")
plt.xlabel("Values")
plt.ylabel("Density")


# Sampling distribution
plt.subplot(1, 2, 2)

plt.hist(
    sample_means,
    bins=40,
    density=True
)

plt.title("Sampling Distribution of Means")
plt.xlabel("Sample Means")
plt.ylabel("Density")

plt.tight_layout()

plt.savefig("day55_sampling_clt.png")

plt.show()


# -----------------------------------
# 6. Compare Different Sample Sizes
# -----------------------------------

sample_sizes = [5, 10, 30, 50, 100]

results = []

for size in sample_sizes:

    means = []

    for _ in range(1000):

        current_sample = np.random.choice(
            population,
            size=size,
            replace=False
        )

        means.append(np.mean(current_sample))

    results.append({
        "Sample Size": size,
        "Mean of Means": np.mean(means),
        "Standard Error": np.std(means, ddof=1)
    })


results_df = pd.DataFrame(results)

print("\nCOMPARISON OF SAMPLE SIZES")
print("--------------------------")

print(results_df.round(2).to_string(index=False))


# -----------------------------------
# 7. Visualize Different Sample Sizes
# -----------------------------------

plt.figure(figsize=(10, 6))

for size in sample_sizes:

    means = []

    for _ in range(1000):

        current_sample = np.random.choice(
            population,
            size=size,
            replace=False
        )

        means.append(np.mean(current_sample))

    plt.hist(
        means,
        bins=35,
        alpha=0.35,
        density=True,
        label=f"Sample Size = {size}"
    )

plt.title("CLT: Effect of Different Sample Sizes")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.legend()

plt.tight_layout()

plt.savefig("day55_sample_size_comparison.png")

plt.show()