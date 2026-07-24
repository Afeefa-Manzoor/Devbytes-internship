# Task 4: Classification Model Evaluation

Trains a Decision Tree classifier and evaluates it with precision, recall,
F1-score, and a confusion matrix.

## Dataset
Breast Cancer Wisconsin (Diagnostic), loaded via `sklearn.datasets.load_breast_cancer`
— no external file dependency. 30 numeric features predicting `malignant` vs `benign`.

## Approach
1. Load dataset and validate (nulls, dtypes, binary target, no constant columns)
2. Train/test split (80/20, stratified)
3. Grid search over `max_depth`, `min_samples_leaf`, `criterion` with 5-fold CV (scoring: F1)
4. Train final Decision Tree on best params
5. Evaluate: accuracy, precision, recall, F1, confusion matrix, classification report
6. Feature importance plot
7. Cross-validated F1 as a stability/overfitting check

## Results
- Best params: `criterion=gini, max_depth=4, min_samples_leaf=1`
- Accuracy: 0.9386
- Precision: 0.9577
- Recall: 0.9444
- F1-score: 0.9510
- Mean CV F1: 0.9368 (± 0.0169)

## Files
- `Task4_Classification_Model_Evaluation.ipynb` — full notebook with code, validation checks, and outputs
- `visualizations/confusion_matrix.png`
- `visualizations/feature_importance.png`
