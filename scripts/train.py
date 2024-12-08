from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

def train_model(X_train, y_train):
    """Trains a Random Forest model."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    print("Model Trained Successfully!")
    return model

def hyperparameter_tuning(X_train, y_train):
    """Performs hyperparameter tuning."""
    param_grid = {'n_estimators': [50, 100, 150], 'max_depth': [5, 10, None]}
    grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
    grid_search.fit(X_train, y_train)
    print("Best Parameters:", grid_search.best_params_)
    return grid_search.best_estimator_
