# Task 6: Neural Networks Core Setup

## Objective
Construct a simple neural network layer to classify dataset rows, then train, test, and graph the loss curve.

## Dataset
**Breast Cancer Wisconsin (Diagnostic)** — loaded via `sklearn.datasets.load_breast_cancer` (built-in, no external file needed). 569 rows, 30 numeric features, binary target (malignant / benign).

## Approach
1. Loaded the dataset and ran post-load validation checks (no nulls, binary target, matching row counts, all-numeric features).
2. Split into train/test sets (80/20, stratified) and standardized features with `StandardScaler` (fit on train only, to avoid leakage).
3. Built a simple feedforward neural network — `MLPClassifier` with **one hidden layer of 16 neurons**, ReLU activation, Adam solver.
4. Trained the model and tracked training loss via `loss_curve_`.
5. Evaluated on the held-out test set: accuracy, precision/recall/F1, and confusion matrix.
6. Plotted and saved the training loss curve.

## Results
- **Test accuracy:** 95.6%
- Model converged in 154 iterations (final training loss ≈ 0.0026).
- See `visualizations/loss_curve.png` and `visualizations/confusion_matrix.png`.

## Files
- `neural_network_core_setup.ipynb` — fully executed notebook (config block, reusable functions, validation checks, all cells run top-to-bottom)
- `visualizations/loss_curve.png` — training loss curve
- `visualizations/confusion_matrix.png` — test set confusion matrix

## Notes
- Used a built-in sklearn dataset to avoid working-directory/file-path issues.
- No hardcoded paths or magic numbers — all configuration lives in a constants block at the top of the notebook.
- Core logic (splitting/scaling, model building/training, evaluation, plotting) is wrapped in reusable functions.
