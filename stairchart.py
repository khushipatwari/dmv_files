import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\rittw\Downloads\python file\ddos_dataset_updated_traffic.csv")

df = df.apply(pd.to_numeric, errors='coerce')

df = df.fillna(0)

numeric_cols = df.select_dtypes(include=["number"]).columns

if len(numeric_cols) == 0:
    print("No numeric columns found!")
    exit()

y = df[numeric_cols[4]]

plt.figure()
plt.step(range(len(y)), y, where='mid')

plt.xlabel("Index")
plt.ylabel(numeric_cols[4])
plt.title("Stair (Step) Chart")

plt.show()