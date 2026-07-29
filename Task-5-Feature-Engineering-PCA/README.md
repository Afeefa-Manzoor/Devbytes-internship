# Task 5: Feature Engineering & PCA

## Objective
Perform standard feature scaling, one-hot encoding, and Principal Component Analysis (PCA) to reduce dimensionality.

## Dataset
Seaborn built-in `tips` dataset (244 rows) — chosen to avoid path/download issues, with both numeric and categorical features suited to this task.

- **Numeric features:** `total_bill`, `tip`, `size`
- **Categorical features:** `sex`, `smoker`, `day`, `time`

## Approach
1. Loaded and validated data (null checks, dtype checks).
2. Scaled numeric features with `StandardScaler`.
3. One-hot encoded categorical features with `OneHotEncoder` (first category dropped).
4. Applied PCA to reduce the combined feature space to 2 components.
5. Visualized explained variance and the 2D PCA projection.

## Files
- `Task5_Feature_Engineering_PCA.ipynb` — full notebook, executed top-to-bottom with saved outputs
- `visualizations/explained_variance.png` — explained variance per component
- `visualizations/pca_scatter.png` — 2D PCA projection colored by `time`

## Key Results
See notebook output cells for exact explained variance ratios and total variance retained.
