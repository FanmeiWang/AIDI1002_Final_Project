# **Turnover Prediction Using IBM Employee Data**

## **Project Overview**
This project aims to predict employee attrition using machine learning techniques. The dataset used is from IBM, which contains employee-related data, including features such as job role, department, years at company, and attrition status. The goal is to build a predictive model that can help businesses identify employees likely to leave the organization, thereby enabling timely interventions.

## **Dataset Information**
- **Source**: [IBM Employee Attrition Dataset](https://github.com/SimonDeVos/turnover_prediction/blob/master/data/ibm.csv)
- **Dataset Description**: The dataset contains information about employees in IBM. It includes various features like age, gender, department, education level, job satisfaction, and whether the employee has left the company (attrition).
- **Target Column**: `Attrition` (binary column: 'Yes' for employees who left and 'No' for employees who stayed)

### **Features**
- `Age`: The age of the employee.
- `JobRole`: The role of the employee in the company.
- `Department`: The department in which the employee works.
- `Education`: The education level of the employee.
- `DistanceFromHome`: The distance of the employee's home from the office.
- `YearsAtCompany`: The number of years the employee has worked at the company.
- `YearsInCurrentRole`: The number of years the employee has worked in their current role.
- `Attrition`: The target variable, which indicates whether the employee left the company (`Yes` or `No`).

## **Preprocessing**
The data is loaded, cleaned, and preprocessed in the following steps:

1. **Load Data**: The dataset is loaded from a CSV file into a pandas DataFrame.
2. **Handle Missing Values**: Missing values (if any) are filled or removed to prevent errors during modeling.
3. **Feature Encoding**: Categorical variables (like `JobRole`, `Department`) are encoded into numerical values using one-hot encoding.
4. **Feature Scaling**: Numerical features are scaled using standardization or normalization techniques to ensure consistent data distribution for the model.
5. **Train-Test Split**: The dataset is split into training and testing sets using an 80-20 ratio.

## **Model Training and Hyperparameter Tuning**
A machine learning model is trained using the training data. The model used in this project is **Random Forest Classifier**, which is a robust and effective model for classification tasks.

1. **Model Training**: The model is trained using the training data (`X_train` and `y_train`).
2. **Hyperparameter Tuning**: (optional) Hyperparameter tuning is applied using techniques like GridSearchCV to find the best parameters for the model, such as the number of trees in the forest and the maximum depth of the trees.

### **Model Evaluation**
Once the model is trained, it is evaluated using the testing data (`X_test` and `y_test`). The following metrics are used for evaluation:
- **Accuracy**: The proportion of correct predictions to the total predictions.
- **Precision**: The number of true positives divided by the sum of true positives and false positives.
- **Recall**: The number of true positives divided by the sum of true positives and false negatives.
- **F1 Score**: The harmonic mean of precision and recall.
- **Confusion Matrix**: A matrix that shows the true positives, true negatives, false positives, and false negatives.

A confusion matrix is also plotted to visualize the model's performance.

## **Results**
After training and evaluating the model, the results are as follows:

- **Accuracy**: 85.3% (for example)
- **Precision**: 80.5% (for example)
- **Recall**: 88.7% (for example)
- **F1-Score**: 84.5% (for example)

A confusion matrix is used to visualize how well the model classifies employees into those who stay and those who leave.

## **Conclusion**
- The Random Forest model is effective for predicting employee attrition, with good performance metrics across accuracy, precision, and recall.
- The model can be used by organizations to identify employees who might leave the company, allowing HR teams to take proactive measures to improve retention.

## **Future Work**
- Further improvements can be made by trying other machine learning algorithms such as Gradient Boosting, XGBoost, or Neural Networks.
- Collecting additional features such as employee feedback or salary data could improve the model's accuracy.
- Real-time model deployment can be done to provide live predictions.

## **File Structure**
```
Main Project/
├── data/
│   └── ibm.csv  # Dataset file
├── scripts/
│   ├── preprocess.py  # Data loading, preprocessing, and feature engineering
│   ├── train.py       # Model training and hyperparameter tuning
│   └── evaluate.py    # Model evaluation and result visualization
├── main.py            # Main script that ties everything together
└── README.md          # Project documentation
```

## **Dependencies**
The following libraries are used in this project:
- `pandas`: For data manipulation and loading CSV files.
- `scikit-learn`: For model training, hyperparameter tuning, and evaluation metrics.
- `matplotlib` & `seaborn`: For plotting the confusion matrix and other visualizations.
- `numpy`: For numerical operations and array manipulation.

You can install the necessary dependencies using the following command:

```bash
pip install pandas scikit-learn matplotlib seaborn numpy
```

## **How to Run**
1. Clone or download this repository.
2. Install the required dependencies by running `pip install -r requirements.txt` (if you have a requirements file).
3. Run the `main2.py` script to load the data, train the model, and evaluate the results.

```bash
python main2.py
```

---

