from scripts.preprocess import load_data, preprocess_data, split_data
from scripts.train import train_model, hyperparameter_tuning
from scripts.evaluate import evaluate_model


# Define the correct path to the dataset
DATA_PATH = r'C:\Users\HP\Desktop\Main Project\data\ibm.csv'


TARGET_COLUMN = 'Attrition'  # The target column in the dataset

def main():
    # Load and preprocess data
    data = load_data(DATA_PATH)
    X, y = preprocess_data(data, target_column=TARGET_COLUMN)
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train and tune model
    model = train_model(X_train, y_train)
    # Uncomment for hyperparameter tuning
    # model = hyperparameter_tuning(X_train, y_train)

    # Evaluate model
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
