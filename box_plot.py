import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ddos_dataset_updated_traffic.csv')

df.replace("NAN", pd.NA, inplace=True)

cols = ['packet_count', 'packet_count_per_second', 'byte_count', 'byte_count_per_second']

# Convert all to numeric
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop NaNs per column
data = [df[col].dropna() for col in cols]

# Plot multiple boxplots
plt.boxplot(data)
plt.xticks([1,2,3,4], cols, rotation=20)
plt.title('Network Traffic Features Boxplot')

plt.show()