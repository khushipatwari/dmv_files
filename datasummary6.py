import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import re
import numpy as np

# -----------------------------
# User inputs
# -----------------------------
frame_size = int(input("Enter number of frames (e.g., 50-200): "))
speed = int(input("Enter animation speed in ms per frame (e.g., 100-1000): "))
circle_radius = float(input("Enter circle radius/size (e.g., 5-15): "))

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
x = np.arange(len(genres))

# Step 5: Set up plot
fig, ax = plt.subplots(figsize=(12,6))
ax.set_xticks(x)
ax.set_xticklabels(genres, rotation=45, ha='right')
ax.set_ylabel("Total Gross (in millions)")
ax.set_title("Total Gross Revenue by Top Genres (Animated)")
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Line and moving circle initialization
line, = ax.plot([], [], color='skyblue', linewidth=2)
circle, = ax.plot([], [], 'o', color='red', markersize=circle_radius)

ax.set_xlim(-0.5, len(genres)-0.5)
ax.set_ylim(0, max(totals)*1.1)

# Step 6: Animation function
def animate(frame):
    # Calculate current index based on frame size
    progress = frame / (frame_size - 1)  # scale 0 to 1
    idx = min(int(progress * (len(x)-1)), len(x)-1)
    line.set_data(x[:idx+1], totals[:idx+1])
    circle.set_data([x[idx]], [totals[idx]])
    return line, circle

# Step 7: Create animation
ani = FuncAnimation(fig, animate, frames=frame_size, interval=speed, repeat=False)

plt.tight_layout()
plt.show()