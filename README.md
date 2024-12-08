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
- Explore model performance across various metrics like Accuracy, Precision, Recall, and more.
- Gain insights into the challenges posed by imbalanced datasets in predictive modeling.

## Dataset
The IBM dataset contains 1,470 records and 35 features, including employee demographics, work-related factors, and attrition status. It is synthetic and publicly available.

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
