import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
import matplotlib.pyplot as plt

def train_logistic_regression(x, y):
    x = np.array(x).reshape(-1, 1)  # Reshape x to a 2D array
    y = np.array(y)

    model = LogisticRegression()
    model.fit(x, y)

    return model

def evaluate_model(model, x, y):
    y_pred = model.predict(x)
    accuracy = accuracy_score(y, y_pred)
    confusion_mat = confusion_matrix(y, y_pred)
    classification_rep = classification_report(y, y_pred)

    return accuracy, confusion_mat, classification_rep

def plot_roc_curve(model, x, y):
    y_pred_proba = model.predict_proba(x)[:, 1]
    fpr, tpr, thresholds = roc_curve(y, y_pred_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.show()

def main():
    # Define your sample data here
    x = [2.5, 3.2, 1.8, 4.1, 5.2]
    y = [0, 1, 0, 1, 1]

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Train the logistic regression model
    model = train_logistic_regression(x_train, y_train)

    # Evaluate the model on the test set
    accuracy, confusion_mat, classification_rep = evaluate_model(model, x_test.reshape(-1, 1), y_test)

    # Print evaluation metrics
    print(f'Accuracy: {accuracy:.2f}')
    print('Confusion Matrix:')
    print(confusion_mat)
    print('Classification Report:')
    print(classification_rep)

    # Plot ROC curve
    plot_roc_curve(model, x_test.reshape(-1, 1), y_test)

if __name__ == "__main__":
    main()
