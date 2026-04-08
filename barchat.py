import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\rittw\Downloads\python file\ddos_dataset_updated_traffic.csv")

traffic_counts = df["traffic_type"].value_counts()

plt.figure()
traffic_counts.plot(kind="bar")

plt.xlabel("Traffic Type")
plt.ylabel("Count")
plt.title("Traffic Type Distribution")

plt.show()