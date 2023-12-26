import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def train_linear_regression(x, y):
    x = np.array(x).reshape(-1, 1)  # Reshape x to a 2D array
    y = np.array(y)

    model = LinearRegression()
    model.fit(x, y)

    return model

def evaluate_model(model, x, y):
    y_pred = model.predict(x)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    return mse, r2

def plot_regression_line(model, x, y):
    plt.scatter(x, y, color='black')
    plt.plot(x, model.predict(x.reshape(-1, 1)), color='blue', linewidth=3)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression')
    plt.show()

def main():
    # Define your sample data here
    x = np.array([2.5, 3.2, 1.8, 4.1, 5.2])
    y = np.array([0, 1, 0, 1, 1])

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = train_linear_regression(x_train, y_train)

    # Evaluate the model on the test set
    mse, r2 = evaluate_model(model, x_test.reshape(-1, 1), y_test)

    # Print evaluation metrics
    print(f'Mean Squared Error: {mse:.2f}')
    print(f'R-squared: {r2:.2f}')

    # Plot the regression line
    plot_regression_line(model, x, y)

if __name__ == "__main__":
    main()
