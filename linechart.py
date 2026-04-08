import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\rittw\Downloads\python file\ddos_dataset_updated_traffic.csv")

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

numeric_cols = df.select_dtypes(include=["number"]).columns

if len(numeric_cols) < 2:
    print("Not enough numeric columns!")
    exit()

df[numeric_cols] = df[numeric_cols].fillna(0)

x = numeric_cols[0]
y = numeric_cols[2]

plt.figure()
plt.plot(df[x], df[y], marker='o')

plt.xlabel(x)
plt.ylabel(y)
plt.title("Line Chart")

plt.grid()

plt.show()