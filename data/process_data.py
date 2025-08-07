import os
import pandas as pd

input_dir = 'data'  # Make sure this is the correct folder with CSVs
output_file = 'data/processed_sales.csv'

# Load and combine CSV files
all_files = [file for file in os.listdir(input_dir) if file.endswith('.csv')]
df_list = []

for file in all_files:
    data = pd.read_csv(os.path.join(input_dir, file))
    df_list.append(data)

df = pd.concat(df_list, ignore_index=True)

# Filter for 'Pink Morsel'
df = df[df['product'] == 'pink morsel']

# Calculate sales
# Ensure quantity and price are numeric
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with missing values in quantity or price
df = df.dropna(subset=['quantity', 'price'])

# Calculate sales
# Ensure quantity and price are numeric
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with missing values in quantity or price
df = df.dropna(subset=['quantity', 'price'])

# Calculate sales
df['sales'] = df['quantity'] * df['price']


# Save cleaned data
df.to_csv(output_file, index=False)
print("✅ Done! The processed data is saved in 'data/processed_sales.csv'")

