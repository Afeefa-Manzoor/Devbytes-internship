# Task 3: Supervised Learning (Regression)

Predicts median house value using Linear Regression, validated with R-squared.

## Dataset
California Housing dataset (`sklearn.datasets.fetch_california_housing`), cached locally as `california_housing.csv`. 8 features (median income, house age, rooms, population, location, etc.) predicting `MedHouseVal`.

## Approach
1. Load and cache dataset locally
2. Validate data (nulls, dtypes, value ranges)
3. Train/test split (80/20) + feature scaling
4. Train Linear Regression model
5. Evaluate with R², MAE, RMSE
6. Visualize predicted vs. actual values

**Note:** Logistic Regression wasn't applicable here — house value is a continuous target, making this a regression problem, not classification.

## Results
- R²: 0.5758
- MAE: 0.5332
- RMSE: 0.7456

## Files
- `Task3_House_Value_Regression.ipynb` — full notebook with code, validation checks, and outputs
- `california_housing.csv` — cached dataset
