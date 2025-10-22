import pandas as pd

# 1. Load the Dataset
# Replace 'Mall_Customers.csv' with the actual path to your dataset.
try:
    df = pd.read_csv('Mall_Customers.csv')
except FileNotFoundError:
    print("Error: 'Mall_Customers.csv' not found. Please download it and place it in the same directory.")
    # As a fallback, create a sample dataframe for demonstration
    data = {'CustomerID': [1, 2, 3, 4, 4],
            'Genre': ['Male', 'Male', 'Female', 'Female', 'Female'],
            'Age': [19, 21, 20, 23, 23],
            'Annual Income (k$)': [15, 15, 16, 16, 16],
            'Spending Score (1-100)': [39, 81, 6, 77, 77],
            'Notes': [None, 'VIP', None, 'Regular', 'Regular']}
    df = pd.DataFrame(data)

print("--- Initial Dataset Info ---")
df.info()
print("\n--- First 5 Rows of Raw Data ---")
print(df.head())

# 2. Clean Column Headers
# Standardize column names to lowercase and replace special characters/spaces with underscores.
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('(k$)', '_k', regex=False).str.replace('(', '', regex=False).str.replace(')', '', regex=False)
print("\n--- Cleaned Column Names ---")
print(df.columns)

# 3. Handle Missing Values
# Check for missing values in each column.
print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())

# For this dataset, let's assume we drop rows where 'notes' is missing for simplicity.
# In a real-world scenario, you might fill them based on other data.
if 'notes' in df.columns:
    df.dropna(subset=['notes'], inplace=True)

# 4. Remove Duplicates
# Check for duplicate rows.
print(f"\nNumber of duplicate rows before cleaning: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)
print(f"Number of duplicate rows after cleaning: {df.duplicated().sum()}")

# 5. Standardize Categorical Data
# The 'Genre' column is renamed to 'gender'. Let's check its values.
if 'genre' in df.columns:
    df.rename(columns={'genre': 'gender'}, inplace=True)
    print("\n--- Unique Values in 'gender' Column ---")
    print(df['gender'].unique())
    # Standardize values to lowercase for consistency, e.g., 'Male' -> 'male'
    df['gender'] = df['gender'].str.lower()
    print("\n--- Standardized Unique Values in 'gender' Column ---")
    print(df['gender'].unique())

# 6. Verify Data Types
print("\n--- Data Types After Cleaning ---")
df.info()

# 7. Save the Cleaned Dataset
# The deliverable is a cleaned dataset.
df.to_csv('cleaned_mall_customers.csv', index=False)
print("\nSuccessfully cleaned the data and saved it as 'cleaned_mall_customers.csv'")

