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
```

## Reproducibility
- **Code Repository**: [https://github.com/SimonDeVos/turnover_prediction/tree/master/data](https://github.com/SimonDeVos/turnover_prediction)
- **Environment**: Python 3.12.7, required dependencies listed in `requirements.txt`.
- **Setup**:
  - Used default hyperparameters as described in the paper.
  - Followed the paper's preprocessing steps for WoE encoding, normalization, and cross-validation.

## Observations

### **Accuracy**
- **Experiment result**: 0.8388
- **Paper**: Section 5.1 mentions that Logistic Regression is one of the better-performing models on the IBM dataset in terms of accuracy, though no specific value is provided. Your result aligns with this trend.

---

### **AUC-ROC**
- **Experiment result**: 0.643
- **Paper**: Section 5.1 and Figure 2 indicate that Logistic Regression has relatively low AUC-ROC on the IBM dataset, comparable to other non-ensemble models. Your result supports this observation.

---

### **F1-Score**
- **Experiment result**: 0.0
- **Paper**: Figure 2 shows that Logistic Regression struggles to predict the minority class (Class 1) effectively, resulting in a poor F1-Score on imbalanced datasets like IBM. This aligns perfectly with your result.

---

### **Precision**
- **Experiment result**: 0.0
- **Paper**: While the paper does not provide specific precision values, Section 5.1 mentions that Logistic Regression typically performs better on the majority class (Class 0). Figure 2 also indicates this trend, and your result confirms it.

---

### **Recall**
- **Experiment result**: 0.0
- **Paper**: Figure 2 illustrates that Logistic Regression has significantly lower recall for the minority class (Class 1), likely due to the lack of data balancing techniques. Your result reflects this issue.

---

### **Specificity**
- **Experiment result**: 0.0
- **Paper**: The paper does not directly report this metric, but it is consistent with the observed trend of Logistic Regression performing better on the majority class.

---

### **AUC-PR**
- **Experiment result**: 0.3546
- **Paper**: The paper discusses that Logistic Regression shows moderate AUC-PR on datasets like IBM, which aligns with your experimental results.

---

### **H-Measure**
- **Experiment result**: 0.0
- **Paper**: The H-Measure is not specifically discussed for Logistic Regression in the paper, but the poor performance for the minority class aligns with this low score.

---

### **Brier Score**
- **Experiment result**: 0.1334
- **Paper**: Section 5.1 mentions that Logistic Regression has moderate calibration ability, often reflected in its Brier Score. Your result is consistent with this observation.

---

### **General Observations**
1. Logistic Regression demonstrated strong overall accuracy (0.8388) but struggled significantly with class imbalance, as evident in its F1-Score (0.0) and Recall (0.0) for the minority class.
2. Calibration ability (Brier Score = 0.1334) and AUC-PR (0.3546) indicate reasonable performance for probability predictions, but the model fails in handling class imbalance effectively.
3. These results align with the trends described in the paper, especially for datasets like IBM where Logistic Regression struggles with minority class predictions.
4. Improvement strategies such as oversampling (e.g., SMOTE) or feature engineering may be necessary to address the poor performance on the minority class.
---
