import pandas as pd

# Load the processed data
df = pd.read_csv('data/processed_sales.csv')

# Show first few rows
print("\n--- Sample Data ---")
print(df.head())

# Show data types and non-null counts
print("\n--- Columns and Data Types ---")
print(df.info())

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check unique values per column
print("\n--- Unique Values ---")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# Show summary stats
print("\n--- Summary Statistics ---")
print(df.describe())

