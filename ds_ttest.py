import math
from scipy import stats

def calculate_sample_mean(sample):
    return sum(sample) / len(sample)

def calculate_sample_std_error(sample):
    return statistics.stdev(sample) / math.sqrt(len(sample))

def calculate_population_mean(population):
    return sum(population) / len(population)

def calculate_t_statistic(sample_mean, population_mean, std_error):
    return (sample_mean - population_mean) / std_error

def calculate_p_value(t_statistic, deg_of_freedom):
    return 2 * (1 - stats.t.cdf(abs(t_statistic), deg_of_freedom))

def calculate_confidence_interval(sample_mean, std_error, alpha, deg_of_freedom):
    margin_of_error = stats.t.ppf(1 - alpha / 2, deg_of_freedom) * std_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

# Population data
pop = [3, 20, 3, 3, 13, 5, 13, 12, 20, 15, 29, 16, 32, 30, 25, 40, 17, 23, 45, 50, 19, 20, 23, 25, 24, 15, 32, 30, 15, 20, 33, 35, 25, 36, 35, 34, 37, 38, 39, 40, 44, 42, 34, 46, 48, 48, 44, 42, 41, 49]

# Sample data
sample = [20, 12, 20, 16, 32, 40, 20, 24, 32, 20, 36, 40, 44, 48, 48, 44]

# Specify the significance level
alpha = 0.05

# Calculate sample statistics
sample_mean = calculate_sample_mean(sample)
std_error = calculate_sample_std_error(sample)
population_mean = calculate_population_mean(pop)

# Calculate t-statistic and p-value
t_statistic = calculate_t_statistic(sample_mean, population_mean, std_error)
deg_of_freedom = len(sample) - 1
p_value = calculate_p_value(t_statistic, deg_of_freedom)

# Print confidence interval
conf_interval = calculate_confidence_interval(sample_mean, std_error, alpha, deg_of_freedom)
print(f"Confidence Interval (1-alpha): ({conf_interval[0]:.2f}, {conf_interval[1]:.2f})")

# Hypothesis testing
if p_value < alpha:
    print("Hypothesis rejected. There is a significant difference between the sample mean and the population mean.")
else:
    print("Hypothesis accepted. There is no significant difference between the sample mean and the population mean.")
