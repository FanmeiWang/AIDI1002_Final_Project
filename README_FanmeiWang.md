# AIDI1002_Final_Project: Predicting Employee Turnover: Scoping and Benchmarking the State-of-the-Art (Fanmei Wang)

- **Fanmei Wang**:
  - Searched, selected, and reviewed the journal article **Predicting Employee Turnover: Scoping and Benchmarking the State-of-the-Art** from the journal **Business & Information Systems Engineering** for the project.
  - Cloned the GitHub repository (https://github.com/SimonDeVos/turnover_prediction) provided by the authors to reproduce the experiments.
  - Reproduced the Logistic Regression (LR) model on the IBM dataset using the configurations outlined in the paper.
  - Adapted and configured main.py for running experiments, including dataset selection, hyperparameter tuning, and model-specific settings.
  - Executed experiments and generated evaluation metrics to validate the paper's findings.
  - Set up the experimental environment by installing dependencies using the provided requirements.txt and ensuring compatibility with Python 3.12.7.
  - Documented reproduction steps in the README.
  - Prepared the final project report: Part 1, Part 2.1, and Part 3.

## Overview
This project reproduces experiments from the paper *Predicting Employee Turnover: Scoping and Benchmarking the State-of-the-Art* by De Vos et al. (2024). The study evaluates the performance of various classification models on employee turnover prediction, focusing on the IBM dataset and the Logistic Regression (LR) model in this reproduction.

## Objectives
- Validate the performance of the LR model on the IBM dataset.
- Examine model performance across various metrics like Accuracy, Precision, Recall, etc.

## Dataset
The dataset used for this project is the IBM dataset (public), including 1,470 records with 35 features, such as employee demographics, work-related factors, attrition status, etc. It is designed to help identify key factors influencing employee turnover.

## Steps Followed

**Step 1: Cloning**
- Accessed the GitHub repository provided by the authors and cloned it into the local environment. 
- After cloning, updated the path configurations to match with the local folder structure and ensure that the codes can be executed locally.

**Step 2: Configuration of the Dataset**
- Analyzed the dataset setup requirements and determined to use the IBM dataset as the data source for this reproduction task.
- The experiment configuration file was modified to enable only the Logistic Regression (LR) model, whereas the rest of the models were disabled.

**Step 3: Environment Setup**
- Created a virtual environment in Python locally and installed all required dependencies, such as NumPy, Pandas, and scikit-learn, by using the requirements.txt file.
- Checked the package versions installed to make sure that they meet the running requirements described.

**Step 4: Experiment Execution**
- Ran the main experiment script to retrieve the results, including but not limited to Accuracy, Precision, Recall, F1-Score, etc.
- The output was then saved in a text file.

**Step 5: Evaluation**
- The output metrics were documented and then compared against the results reported in the paper.  
- Checked whether my reproduction results were in line with the findings reported in the paper.

## Key Contributions
- **Reproduction:** Replicated the LR model experiment using the provided configurations, focusing on the IBM dataset.
- **Code Refinement:** Adjusted dataset and methodology configurations to align with the paper's objectives.
- **Evaluation:** Compared reproduced results with trends reported in the paper.

## Results Summary
| Metric        | Reproduced Result | Paper Trend (Ranking) |
|---------------|-------------------|------------------------|
| Accuracy      | 0.8388            | 8.1                   |
| Recall        | 0.0000            | 10.9                  |
| Precision     | 0.0000            | 8.0                   |
| F1-Score      | 0.0000            | 9.9                   |
| AUC-PR        | 0.3546            | 7.9                   |
| AUC-ROC       | 0.6430            | 7.6                   |
| H-Measure     | 0.0000            | 10.0                  |
| Brier Score   | 0.1334            | 6.4                   |

The reproduced results confirm the challenges Logistic Regression faces with imbalanced datasets, particularly in metrics like Recall and F1-Score.

## Limitations
- This reproduction focuses solely on the IBM dataset and the LR model. Results may vary for other datasets or algorithms.
- Imbalanced classes in the IBM dataset significantly impacted the LR model's ability to predict minority class instances.

## Future Work
- Extend reproduction to other models like Random Forest and XGBoost.
- Incorporate advanced balancing techniques (e.g., SMOTE, ADASYN) to improve minority class predictions.
- Explore deep learning methods, such as BERT, for turnover prediction from textual data.

## Repository
The implementation and results are available in this repository.

## Citation
De Vos, S., Bockel-Rickermann, C., Van Belle, J., & Verbeke, W. (2024). Predicting Employee Turnover: Scoping and Benchmarking the State-of-the-Art. *Business & Information Systems Engineering, 1–20.* Springer. [https://doi.org/10.1007/s12599-024-00898-z](https://doi.org/10.1007/s12599-024-00898-z)
