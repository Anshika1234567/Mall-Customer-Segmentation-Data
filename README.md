# Mall-Customer-Segmentation-Data
# Project: Data Cleaning and Preprocessing for Mall Customer Data

## Task Objective

This project focuses on cleaning and preprocessing the "Mall Customer Segmentation" dataset as part of the Elevate Labs Data Analyst Internship (Task 1). The goal is to prepare the raw data for future analysis by addressing common issues like missing values, duplicates, and inconsistent formatting.

## Tools Used

- **Python**: Core programming language.
- **Pandas**: For data manipulation and cleaning.

## Data Cleaning Steps

1.  **Loaded the Dataset**: The raw data was loaded from `Mall_Customers.csv` into a Pandas DataFrame.
2.  **Cleaned Column Headers**: Column names were standardized to a consistent format (lowercase, with underscores instead of spaces and special characters).
    - `Genre` -> `gender`
    - `Annual Income (k$)` -> `annual_income_k`
    - `Spending Score (1-100)` -> `spending_score_1-100`
3.  **Handled Missing Values**: Checked for null values across all columns. Any rows with missing data were handled (in this script, rows with missing 'notes' were dropped).
4.  **Removed Duplicates**: Inspected the dataset for duplicate rows and removed them to ensure data integrity.
5.  **Standardized Categorical Data**: The `gender` column values ('Male', 'Female') were converted to lowercase ('male', 'female') for consistency.
6.  **Verified Data Types**: Ensured all columns have appropriate data types (`Age` as `int64`, `annual_income_k` as `int64`, etc.).
7.  **Saved the Cleaned Data**: The fully cleaned dataset was saved to a new file named `cleaned_mall_customers.csv`.

## Final Deliverables

- **`cleaned_mall_customers.csv`**: The cleaned and preprocessed dataset, ready for analysis.
- **`data_cleaning_script.py`**: The Python script containing all the steps performed to clean the data.

