import numpy as np
from scipy import stats

def calculate_sample_mean(sample):
    return np.mean(sample)

def calculate_sample_std_dev(sample):
    return np.std(sample, ddof=1)

def calculate_standard_error(sample_std_dev, sample_size):
    return sample_std_dev / np.sqrt(sample_size)

def calculate_z_score(sample_mean, population_mean, standard_error):
    return (sample_mean - population_mean) / standard_error

def calculate_p_value(z_score):
    return 2 * (1 - stats.norm.cdf(np.abs(z_score)))

def calculate_confidence_interval(sample_mean, standard_error, alpha):
    margin_of_error = stats.norm.ppf(1 - alpha / 2) * standard_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

# Sample data
sample = [20, 12, 20, 16, 32, 40, 20, 24, 32, 20, 36, 40, 44, 48, 48, 44]
sample_size = len(sample)

# Known population parameters
population_mean = 28.54  # Population mean
population_std_dev = 12.18  # Population standard deviation

# Significance level
alpha = 0.05

# Calculate sample statistics
sample_mean = calculate_sample_mean(sample)
sample_std_dev = calculate_sample_std_dev(sample)
standard_error = calculate_standard_error(sample_std_dev, sample_size)

# Perform hypothesis test
z_score = calculate_z_score(sample_mean, population_mean, standard_error)
p_value = calculate_p_value(z_score)

# Calculate and print the confidence interval
lower_bound, upper_bound = calculate_confidence_interval(sample_mean, standard_error, alpha)
print(f"Confidence Interval (1-alpha): ({lower_bound:.2f}, {upper_bound:.2f})")

# Print results
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Z-Score: {z_score:.2f}")
print(f"P-Value: {p_value:.4f}")

# Hypothesis testing
if np.abs(z_score) > stats.norm.ppf(1 - alpha / 2):
    print("Hypothesis rejected. There is a significant difference between the sample mean and the population mean.")
else:
    print("Hypothesis accepted. There is no significant difference between the sample mean and the population mean.")
