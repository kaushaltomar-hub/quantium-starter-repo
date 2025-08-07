import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('data/processed_sales.csv')
df['sales'] = df['sales'].replace('[\$,]', '', regex=True).astype(float)
df['date'] = pd.to_datetime(df['date'])

# Group by date (in case multiple entries per day)
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['date'], daily_sales['sales'], marker='o')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Total Sales Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
