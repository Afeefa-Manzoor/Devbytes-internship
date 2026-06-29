# Task 1 — Pandas Data Cleanup Pipeline

**Status:** Completed  
**Due Date:** 2026-07-05  
**Language:** Python  
**Libraries:** Pandas, NumPy  

---

## What This Task Is About

Load a raw messy CSV file, identify data quality issues, clean null entries, normalize columns, and parse data ranges using Python and Pandas. Export the final cleaned dataset.

---

## Files in This Folder

| File | Description |
|------|-------------|
| `data_cleanup.ipynb` | Jupyter Notebook with the full 8-step cleaning pipeline |
| `raw_employee_data.csv` | Raw dataset with 520 rows and intentional data issues |
| `cleaned_employee_data.csv` | Final cleaned output with 500 rows and 24 columns |

---

## Data Issues Found in Raw File

- Missing values disguised as strings: `NULL`, `N/A`, `n/a`, `-`, `none`
- Inconsistent name casing: `JOHN SMITH`, `john smith`, `John Smith`
- Inconsistent gender labels: `MALE`, `male`, `Male`
- 20 exact duplicate rows
- Salary stored as string range: `70000-150000`
- Missing salary, age, performance score values

---

## How to Run

1. Place all files in the same folder
2. Open `data_cleanup.ipynb` in Jupyter
3. Run all cells top to bottom
4. Output saves as `cleaned_employee_data.csv`
