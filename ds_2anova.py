import numpy as np
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

def calculate_anova(samples):
    # Flatten the samples into a single list
    flat_samples = [item for sublist in samples for item in sublist]

    # Create a data frame with a categorical column for each factor
    data = {
        'Values': flat_samples,
        'Factor1': np.repeat(['A1', 'A2', 'A3'], len(samples[0])),
        'Factor2': np.tile(['B1', 'B2'], len(samples)),
    }

    df = pd.DataFrame(data)

    # Fit the two-way ANOVA model
    formula = 'Values ~ C(Factor1) + C(Factor2) + C(Factor1):C(Factor2)'
    model = ols(formula, df).fit()

    # Perform the ANOVA
    anova_table = anova_lm(model, typ=2)

    # Extract the F-statistic from the table
    f_statistic = anova_table['F']['C(Factor1):C(Factor2)']

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
        print("H0 REJECTED: There is a significant interaction effect between Factor1 and Factor2.")
    else:
        print("H0 ACCEPTED: There is no significant interaction effect between Factor1 and Factor2.")

if __name__ == "__main__":
    perform_anova_test()
