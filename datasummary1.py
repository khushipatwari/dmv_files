import pandas as pd
import matplotlib.pyplot as plt
import re

# Step 1: Load the data
df = pd.read_csv(r"C:\Users\lab\Downloads\archive (2)\movies.csv")

# Step 2: Clean 'gross_total' column
# Remove dollar signs and 'M', then convert to float
def parse_gross(x):
    # Keep only digits and decimal points
    x = str(x)
    # If multiple numbers are stuck together, take only the first one
    match = re.search(r'[\d,.]+', x)
    if match:
        value = match.group(0).replace(',', '')
        return float(value)
    return 0.0  # fallback for missing/invalid data

df['gross_total'] = df['gross_total'].apply(parse_gross)

# Step 3: Group by genre and calculate sum, mean, count
grouped = df.groupby('genre')['gross_total'].agg(['sum', 'mean', 'count'])

# Step 4: Sort by total gross
grouped_sorted = grouped.sort_values(by='sum', ascending=False)

# Step 5: Plot horizontal bar chart
plt.figure(figsize=(10,8))
plt.barh(
    grouped_sorted.index, 
    grouped_sorted['sum'], 
    color='skyblue'
)
plt.xlabel("Total Gross (in millions)")
plt.ylabel("Genre")
plt.title("Total Gross Revenue by Genre")
plt.gca().invert_yaxis()  # highest gross on top
plt.tight_layout()
plt.show()