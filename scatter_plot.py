import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('ddos_dataset_updated_traffic.csv')

# Convert "NAN" strings to actual NaN
df.replace("NAN", pd.NA, inplace=True)

# Convert columns to numeric
df['packet_count'] = pd.to_numeric(df['packet_count'], errors='coerce')
df['byte_count'] = pd.to_numeric(df['byte_count'], errors='coerce')

# Drop rows where either column is missing
df = df.dropna(subset=['packet_count', 'byte_count'])

# Extract values
x = df['packet_count']
y = df['byte_count']

# Scatter plot
plt.scatter(x, y)

plt.xlabel('Packet Count')
plt.ylabel('Byte Count')
plt.title('Packet Count vs Byte Count')

plt.show()