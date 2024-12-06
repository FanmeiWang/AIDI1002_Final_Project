# AIDI1002_Final_Project

## Group Member Names:
- Fanmei Wang
- Roshni Sanjay Pamak

## Project Overview
This project reproduces the experimental section of the paper *Predicting Employee Turnover: Scoping and Benchmarking the State-of-the-Art*, focusing on the performance of the Logistic Regression (LR) model on the IBM dataset.

## Dataset
- **Name**: IBM Dataset
- **Description**: The dataset contains employee information and attrition status, aimed at analyzing factors that influence employee turnover.

## Experimental Steps
1. Download the code provided by the paper.
2. Configure the experimental parameters (e.g., IBM dataset and Logistic Regression method).
3. Run `main.py` and generate the results.

## Experiment Steps
1. **Code Download**: Cloned the code repository provided by the paper.
2. **Configuration**: Set the dataset to `IBM` and enabled the Logistic Regression (`lr`) method in the configuration file (`main.py`).
3. **Environment Setup**: 
   - **Python Version**: Python 3.12.7
   - **Dependencies**: Installed required packages from `requirements.txt`.
4. **Run Experiment**: Executed `main.py` to reproduce the results.
5. **Results Generation**: Collected evaluation metrics for the Logistic Regression model.

## Reproduced Results
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
  - `numpy==1.23.5`
  - `pandas==1.5.3`
  - `scikit-learn==1.2.1`

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt

## Reproducibility
- **Code Repository**: [https://github.com/SimonDeVos/turnover_prediction/tree/master/data](https://github.com/SimonDeVos/turnover_prediction)
- - **Environment**: Python 3.12.7, required dependencies listed in `requirements.txt`.
- **Setup**:
  - Used default hyperparameters as described in the paper.
  - Followed the paper's preprocessing steps for WoE encoding, normalization, and cross-validation.

## Observations
- The model showed high accuracy but failed to predict the minority class effectively (F1-Score = 0).
- The paper did not provide explicit numerical results for direct comparison; thus, results were validated against trends described in the paper (e.g., Table 5).
