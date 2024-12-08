import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def load_data(filepath):
    """Loads the dataset from a CSV file."""
    data = pd.read_csv("C:\Users\HP\Desktop\Main Project\data")
    print("Data Loaded Successfully!")
    return data

def preprocess_data(data, target_column):
    """Preprocesses the dataset (encoding, scaling, etc.)."""
    # Handle missing values (example: fill with median for numerical columns)
    data.fillna(data.median(), inplace=True)

    # Separate features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # One-hot encode categorical features (e.g., 'gender', 'department', etc.)
    categorical_columns = X.select_dtypes(include=['object']).columns
    encoder = OneHotEncoder(drop='first', sparse=False)
    encoded_cats = encoder.fit_transform(X[categorical_columns])
    encoded_df = pd.DataFrame(encoded_cats, columns=encoder.get_feature_names_out(categorical_columns))
    X = pd.concat([X.drop(columns=categorical_columns), encoded_df], axis=1)

    # Scale numerical features
    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """Splits the data into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
