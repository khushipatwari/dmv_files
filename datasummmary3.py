import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

# Step 1: Load the data
df = pd.read_csv(r"C:\Users\lab\Downloads\archive (2)\movies.csv")

# Step 2: Clean 'gross_total' column
def parse_gross(x):
    x = str(x)
    match = re.search(r'[\d,.]+', x)
    if match:
        value = match.group(0).replace(',', '')
        return float(value)
    return 0.0

df['gross_total'] = df['gross_total'].apply(parse_gross)

# Step 3: Group by genre and sum total gross
grouped = df.groupby('genre')['gross_total'].sum()

# Step 4: Sort top 10 genres
grouped_sorted = grouped.sort_values(ascending=False).head(10)

# Step 5: Prepare data for staircase (cumulative sum)
genres = grouped_sorted.index
totals = grouped_sorted.values
cumulative = np.cumsum(totals)

# Step 6: Plot staircase chart
plt.figure(figsize=(12,6))
plt.step(range(len(cumulative)), cumulative, where='mid', linewidth=2, color='skyblue')
plt.scatter(range(len(cumulative)), cumulative, color='blue')  # mark steps
plt.xticks(range(len(cumulative)), genres, rotation=45, ha='right')
plt.ylabel("Cumulative Gross (in millions)")
plt.title("Staircase Chart: Cumulative Total Gross by Top Genres")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()