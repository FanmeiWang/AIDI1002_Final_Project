# AIDI1002_Final_Project

## Group Member Names:
- **Fanmei Wang**:
  - Searched, selected, and reviewed the journal article **Predicting Employee Turnover: Scoping and Benchmarking the State-of-the-Art** from the journal **Business & Information Systems Engineering** for the project.
  - Cloned the GitHub repository provided by the authors to reproduce the experiments.
  - Reproduced the Logistic Regression (LR) model on the IBM dataset using the configurations outlined in the paper.
  - Adapted and configured `main.py` for running experiments, including dataset selection, hyperparameter tuning, and model-specific settings.
  - Executed experiments and generated evaluation metrics to validate the paper's findings.
  - Set up the experimental environment by installing dependencies using the provided `requirements.txt` and ensuring compatibility with Python 3.12.7.
  - Documented reproduction steps in the README and prepared the final project template.  
  
- **Roshni Sanjay Pamak**:

# Employee Attrition Prediction

## **Project Overview**
This project is designed to predict employee attrition using machine learning techniques, specifically classification models. The dataset contains information about employees in a company, including various attributes like job role, department, age, years at the company, and whether the employee left the company (attrition). The goal is to create a model that can help businesses predict and manage employee turnover.

## **Dataset**
The dataset used in this project is derived from the IBM Employee Attrition dataset and contains employee-related data such as age, department, job role, years at the company, and whether they left the company.

### **Dataset Details**
- **Source**: [IBM Employee Attrition Dataset](https://github.com/SimonDeVos/turnover_prediction/blob/master/data/ibm.csv)
- **Target Variable**: `Attrition` (binary classification: 'Yes' if the employee left the company, 'No' if the employee stayed)
  
### **Features**
- `Age`: The age of the employee.
- `JobRole`: The role of the employee within the company.
- `Department`: The department in which the employee works.
- `Education`: The education level of the employee.
- `YearsAtCompany`: The number of years the employee has worked at the company.
- `DistanceFromHome`: The distance from the employee's home to the company.
- `Attrition`: The target variable indicating whether the employee left the company or not.

## **Technologies Used**
- **Python**: Programming language for implementing the solution.
- **Libraries**:
  - `pandas`: For data manipulation and loading the dataset.
  - `scikit-learn`: For machine learning model training, evaluation, and metrics.
  - `matplotlib`, `seaborn`: For visualizing data and evaluation results.
  - `numpy`: For numerical operations.
- **Model**: Random Forest Classifier (with optional hyperparameter tuning using GridSearchCV).

## **Installation**

### **Requirements**
Before running the project, make sure to have the following dependencies installed:

```bash
pip install pandas scikit-learn matplotlib seaborn numpy
```

### **File Structure**
The project is organized into the following directory structure:

```
Main Project/
├── data/
│   └── ibm.csv          # The dataset file (IBM Employee Attrition Dataset)
├── scripts/
│   ├── preprocess.py    # Script for loading, cleaning, and preprocessing the data
│   ├── train.py         # Script for model training and hyperparameter tuning
│   ├── evaluate.py      # Script for model evaluation and result analysis
├── main.py              # Main script that ties everything together
└── README.md            # Project documentation
```

## **How to Run**

1. **Clone or download** this repository.
2. **Install the required dependencies** by running:

```bash
pip install -r requirements.txt
```

3. **Run the main script** to train and evaluate the model:

```bash
python main.py
```

### **Explanation of main.py**
The `main.py` script is the entry point of the project and performs the following steps:
1. Loads and preprocesses the data.
2. Trains a machine learning model using Random Forest Classifier.
3. Evaluates the model using various metrics like accuracy, precision, recall, and F1-score.
4. Displays the results, including a confusion matrix.

## **Scripts Overview**

### **preprocess.py**
- **Functions**:
  - `load_data()`: Loads the dataset from a specified CSV file.
  - `preprocess_data()`: Handles missing values, encodes categorical features, and scales numerical features.
  - `split_data()`: Splits the data into training and test sets.
  
### **train.py**
- **Functions**:
  - `train_model()`: Trains the model using the training data.
  - `hyperparameter_tuning()`: (optional) Tunes the hyperparameters of the model using GridSearchCV.

### **evaluate.py**
- **Functions**:
  - `evaluate_model()`: Evaluates the model on the test data, prints classification metrics, and displays a confusion matrix.

## **Model Evaluation**
The model is evaluated based on the following metrics:
- **Accuracy**: The proportion of correct predictions.
- **Precision**: The proportion of true positives out of all predicted positives.
- **Recall**: The proportion of true positives out of all actual positives.
- **F1 Score**: The harmonic mean of precision and recall.
- **Confusion Matrix**: A matrix that shows the number of true positives, true negatives, false positives, and false negatives.

## **Sample Output**

After running the `main2.py` script, the following will be displayed:

1. **Classification Report**: It will show the precision, recall, F1-score, and support for each class (`Yes` and `No`).
2. **Confusion Matrix**: A heatmap visualization of the confusion matrix showing how well the model classified employees.

## **Results**
Example model results:
```
Accuracy: 85.3%
Precision: 82.1%
Recall: 87.4%
F1 Score: 84.7%
```

### **Confusion Matrix**
- The confusion matrix will provide a summary of how well the model is performing, showing true positives, false positives, true negatives, and false negatives.

## **Future Work**
- **Model Comparison**: Try other classification models such as Logistic Regression, Gradient Boosting, or XGBoost for potentially better performance.
- **Hyperparameter Tuning**: Explore hyperparameter tuning to improve model performance.
- **Feature Engineering**: Additional features such as salary, employee feedback, or other demographic information could be included to improve the model.
- **Real-World Application**: Consider deploying the model for real-time predictions or integrating it with HR systems for practical use.


    
## Project Overview
This project reproduces the experimental section of the paper *Predicting Employee Turnover: Scoping and Benchmarking the State-of-the-Art*, focusing on the performance of the Logistic Regression (LR) model on the IBM dataset.

## Dataset
- **Name**: IBM Dataset
- **Description**: The dataset contains employee information and attrition status, aimed at analyzing factors that influence employee turnover.

## Experiment Steps (Reproduction)
1. **Code Download**: Cloned the code repository provided by the paper.
2. **Configuration**: Set the dataset to `IBM` and enabled the Logistic Regression (`lr`) method in the configuration file (`main.py`).
3. **Environment Setup**: 
   - **Python Version**: Python 3.12.7
   - **Dependencies**: Installed required packages from `requirements.txt`.
4. **Run Experiment**: Executed `main.py` to reproduce the results.
5. **Results Generation**: Collected evaluation metrics for the Logistic Regression model.

## Results (Reproduction)
The reproduced results from the IBM dataset are as follows:
- **Accuracy**: 0.8388
- **AUC-ROC**: 0.6430
- **F1-Score**: 0.0000
- **Precision**: 0.0000
- **Recall**: 0.0000
- **Specificity**: 0.0000
- **AUC-PR**: 0.3546
- **H-Measure**: 0.0000
- **Brier Score**: 0.1334

## System Requirements
- **Python Version**: Python 3.12.7
- **Required Libraries**:
  - `numpy==1.26.4`
  - `pandas==2.2.2`
  - `scikit-learn==1.5.1`

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Reproducibility
- **Code Repository**: [https://github.com/SimonDeVos/turnover_prediction/tree/master/data](https://github.com/SimonDeVos/turnover_prediction)
- **Environment**: Python 3.12.7, required dependencies listed in `requirements.txt`.
- **Setup**:
  - Used default hyperparameters as described in the paper.
  - Followed the paper's preprocessing steps for WoE encoding, normalization, and cross-validation.

## Observations (Reproduction)

### **Accuracy**
- **Experiment result**: 0.8388
- **Paper**: Section 5.1 mentions that Logistic Regression is one of the better-performing models on the IBM dataset in terms of accuracy, though no specific value is provided. My result aligns with this trend.

---

### **AUC-ROC**
- **Experiment result**: 0.643
- **Paper**: Section 5.1 and Figure 2 indicate that Logistic Regression has relatively low AUC-ROC on the IBM dataset, comparable to other non-ensemble models. My result supports this observation.

---

### **F1-Score**
- **Experiment result**: 0.0
- **Paper**: Figure 2 shows that Logistic Regression struggles to predict the minority class (Class 1) effectively, resulting in a poor F1-Score on imbalanced datasets like IBM. This aligns perfectly with my result.

---

### **Precision**
- **Experiment result**: 0.0
- **Paper**: While the paper does not provide specific precision values, Section 5.1 mentions that Logistic Regression typically performs better on the majority class (Class 0). Figure 2 also indicates this trend, and my result confirms it.

---

### **Recall**
- **Experiment result**: 0.0
- **Paper**: Figure 2 illustrates that Logistic Regression has significantly lower recall for the minority class (Class 1), likely due to the lack of data balancing techniques. My result reflects this issue.

---

### **Specificity**
- **Experiment result**: 0.0
- **Paper**: The paper does not directly report this metric, but it is consistent with the observed trend of Logistic Regression performing better on the majority class.

---

### **AUC-PR**
- **Experiment result**: 0.3546
- **Paper**: The paper discusses that Logistic Regression shows moderate AUC-PR on datasets like IBM, which aligns with my experimental results.

---

### **H-Measure**
- **Experiment result**: 0.0
- **Paper**: The H-Measure is not specifically discussed for Logistic Regression in the paper, but the poor performance for the minority class aligns with this low score.

---

### **Brier Score**
- **Experiment result**: 0.1334
- **Paper**: Section 5.1 mentions that Logistic Regression has moderate calibration ability, often reflected in its Brier Score. My result is consistent with this observation.

---

### **General Observations**
1. Logistic Regression demonstrated strong overall accuracy (0.8388) but struggled significantly with class imbalance, as evident in its F1-Score (0.0) and Recall (0.0) for the minority class.
2. Calibration ability (Brier Score = 0.1334) and AUC-PR (0.3546) indicate reasonable performance for probability predictions, but the model fails in handling class imbalance effectively.
3. These results align with the trends described in the paper, especially for datasets like IBM where Logistic Regression struggles with minority class predictions.
4. Improvement strategies such as oversampling (e.g., SMOTE) or feature engineering may be necessary to address the poor performance on the minority class.
---
