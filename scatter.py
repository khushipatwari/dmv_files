import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\rittw\Downloads\python file\ddos_dataset_updated_traffic.csv")

print(df.head())
print(df.dtypes)

x = "packet_count"
y = "packet_count_per_second"

df[x] = pd.to_numeric(df[x], errors='coerce')
df[y] = pd.to_numeric(df[y], errors='coerce')

df = df.dropna(subset=[x, y])

colors = df["traffic_type"].map({
    "Normal": "blue",
    "Heavy Traffic": "red",
    "Low Traffic": "green"
})

plt.figure()
plt.scatter(df[x], df[y], c=colors)

plt.xlabel(x)
plt.ylabel(y)
plt.title("Scatter Plot")

plt.show()