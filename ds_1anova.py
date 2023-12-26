def calculate_anova(samples):
    means = [sum(sample) / len(sample) for sample in samples]
    population_mean = sum(sum(sample) for sample in samples) / sum(len(sample) for sample in samples)

    between_group_var = sum(len(sample) * (mean - population_mean) ** 2 for sample, mean in zip(samples, means))
    within_group_var = sum(sum((x - mean) ** 2 for x in sample) for sample, mean in zip(samples, means))

    df_between = len(samples) - 1
    df_within = sum(len(sample) - 1 for sample in samples)
    
    ms_between = between_group_var / df_between
    ms_within = within_group_var / df_within
    
    f_statistic = ms_between / ms_within
    
    return f_statistic

def perform_anova_test():
    # Define your sample data here
    samples = [
        [10, 12, 15],
        [20, 22, 25],
        [5, 7, 9]
    ]

    anova_value = calculate_anova(samples)

    # Assuming a significance level of 0.05
    alpha = 0.05

    # Critical value from an F-distribution table (you may want to look up for your specific degrees of freedom)
    critical_value = 3.885

    print(f"F-Statistic: {anova_value:.4f}")
    print(f"Critical Value: {critical_value:.4f}")

    if anova_value > critical_value:
        print("H0 REJECTED: There is a significant difference between the group means.")
    else:
        print("H0 ACCEPTED: There is no significant difference between the group means.")

if __name__ == "__main__":
    perform_anova_test()
