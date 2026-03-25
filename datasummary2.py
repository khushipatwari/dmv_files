import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import re
import numpy as np

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

# Step 3: Group by genre
grouped = df.groupby('genre')['gross_total'].sum()

# Step 4: Keep top 10 genres
grouped_sorted = grouped.sort_values(ascending=False).head(10)
labels = grouped_sorted.index
sizes = grouped_sorted.values

# Step 5: Animated pie chart
fig, ax = plt.subplots(figsize=(8,8))
ax.axis('equal')

def animate(frame):
    ax.clear()
    ax.axis('equal')
    frac = frame / 100  # scale from 0 to 1
    scaled_sizes = sizes * frac
    # Avoid empty pie error by replacing all zeros with tiny positive number
    if np.sum(scaled_sizes) == 0:
        scaled_sizes = np.ones_like(scaled_sizes) * 1e-6
    ax.pie(
        scaled_sizes, 
        labels=labels, 
        startangle=90, 
        autopct=lambda p: f'{p:.1f}%' if p > 0 else ''
    )
    ax.set_title("Total Gross Revenue by Genre (Animated)")

ani = FuncAnimation(fig, animate, frames=101, interval=50, repeat=False)
plt.show()