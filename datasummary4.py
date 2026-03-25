import pandas as pd
import matplotlib.pyplot as plt
import re

# Step 1: Load data
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

# Step 4: Take top 10 genres
grouped_sorted = grouped.sort_values(ascending=False).head(10)
genres = grouped_sorted.index
totals = grouped_sorted.values

# Step 5: Plot line graph with circles
plt.figure(figsize=(12,6))
plt.plot(genres, totals, marker='o', linestyle='-', color='skyblue', linewidth=2, markersize=8)
plt.xticks(rotation=45, ha='right')
plt.ylabel("Total Gross (in millions)")
plt.title("Total Gross Revenue by Top Genres")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()