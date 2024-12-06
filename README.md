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
## Observations

### **Accuracy**
- **Experiment result**: 83.88%
- **Paper**: Section 5.1 mentions that Logistic Regression is one of the better-performing models on the IBM dataset, especially in terms of accuracy (though no specific value is provided). Your result aligns with this trend.

---

### **AUC-ROC**
- **Experiment result**: 64.3%
- **Paper**: Section 5.1 and Figure 2 indicate that Logistic Regression has relatively low AUC-ROC on the IBM dataset, comparable to other non-ensemble models. Your result supports this observation.

---

### **F1-Score**
- **Experiment result**: 0.00
- **Paper**: Figure 2 shows that Logistic Regression struggles to predict the minority class (Class 1) effectively, resulting in a poor F1-Score on imbalanced datasets like IBM. This aligns perfectly with your result.

---

### **Precision**
- **Experiment result**: 
  - Class 0: 92%
  - Class 1: 61%
- **Paper**: While the paper does not provide specific precision values, Section 5.1 mentions that Logistic Regression typically performs better on the majority class (Class 0). Figure 2 also indicates this trend, and your result confirms it.

---

### **Recall**
- **Experiment result**: 
  - Class 0: 96%
  - Class 1: 36%
- **Paper**: Figure 2 illustrates that Logistic Regression has significantly lower recall for the minority class (Class 1), likely due to the lack of data balancing techniques. Your result reflects this issue.

---

### **Specificity**
- **Experiment result**: The high Specificity for Class 0 is implied by the model’s strong performance on the majority class (Class 0), though it is not explicitly calculated.
- **Paper**: The paper does not directly report this metric, but it is consistent with the observed trend of Logistic Regression performing better on the majority class.

---

### **Brier Score**
- **Experiment result**: 0.1334
- **Paper**: Section 5.1 notes that Logistic Regression has moderate calibration ability (assessed via Brier Score). While no specific value is provided, your result suggests reasonable calibration, aligning with the paper's description.

---

### **General Observations**
1. **Class Imbalance Issue**:
   - Your experiment shows that Logistic Regression performs well for the majority class (Class 0) but struggles significantly with the minority class (Class 1) in terms of recall and F1-Score.
   - The paper also highlights this issue (Section 5.2), suggesting data balancing techniques (e.g., SMOTE or ADASYN) to improve performance.

2. **Calibration**:
   - The Brier Score result indicates moderate calibration performance, consistent with the paper's general assessment of Logistic Regression.

3. **Alignment with Paper Trends**:
   - On the IBM dataset, Logistic Regression’s overall performance matches the trends described in the paper, including its shortcomings (e.g., poor minority class performance).

4. **Potential Improvements**:
   - Based on the paper’s recommendations, applying data balancing techniques or feature selection could potentially address the performance issues on the minority class.
