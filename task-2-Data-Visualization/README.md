# Data Visualization & Analysis

**Status:** Complete
**Assigned:** 2026-06-28 | **Due:** 2026-07-12

## Objective
Explore an employee dataset using Matplotlib and Seaborn to surface distributions,
relationships between variables, correlations, and outliers — via histograms, scatterplots,
a correlation matrix, and boxplots.

## Dataset
`cleaned_employee_data.csv` — the cleaned dataset carried over from Task 1 (Data Cleanup).
Columns used:
- **Numeric:** age, salary, years_at_company, performance_score, projects_completed,
  training_hours, satisfaction_score, salary_percentile_in_band
- **Categorical:** gender, department, education_level, remote_work, seniority_band,
  performance_tier
- **Target (used for hue in plots):** performance_tier

Identifier columns (employee_id, full_name, email, phone, manager_id) and derived/duplicate
columns (salary_range_min/max/mid) were excluded from analysis as non-informative or redundant.

## Structure
```
Task-X-Data-Visualization/
├── README.md
├── Data_Visualization_Analysis.ipynb
├── cleaned_employee_data.csv
└── visualizations/                # auto-generated PNG exports, created by the notebook
```

## Notebook Contents
1. **Configuration** — relative path (`PROJECT_ROOT / "cleaned_employee_data.csv"`) + named
   column lists, no hardcoding
2. **Load Data** — clear error message pointing back to the working-directory check if the
   file isn't found
3. **Validation Checks** — asserts configured columns exist, reports nulls, confirms dtypes
4. **Reusable Plotting Functions** — `plot_histograms()`, `plot_scatterplots()`,
   `plot_correlation_matrix()`, `plot_boxplots()`, `plot_pairwise()`, each parameterized by
   column list rather than hardcoded to specific columns
5. **Generate Visualizations** — histograms for all numeric columns, a correlation matrix,
   boxplots of numeric columns by department, a pairplot, and a targeted scatterplot of
   training_hours vs. performance_score
6. **Insights & Observations** — written interpretation, including:
   - Salary clusters in bands rather than a smooth distribution
   - Almost no meaningful correlation between variables (aside from one derived relationship)
   - A few salary outliers by gender
   - Salary is essentially flat across gender groups

## How to Run
1. Keep `cleaned_employee_data.csv` in the same folder as the notebook (already set up this way).
2. Open the notebook **from that folder** in Jupyter — this ensures `Path.cwd()` resolves correctly.
3. Run all cells top-to-bottom (`Cell → Run All`). Outputs are already saved from the last run,
   but re-running confirms everything still executes cleanly end-to-end.

## Notes
- All charts are saved automatically to `visualizations/` when the notebook runs.
- Findings here reflect what the dataset shows rather than assumptions about real workplace
  behavior — see the Insights section for the reasoning (the data reads as closer to
  synthetic/random than a real HR snapshot in several respects).
- Update the root repo `README.md` completion table once this task is submitted and approved.
