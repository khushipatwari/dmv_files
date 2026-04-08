import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\rittw\Downloads\python file\ddos_dataset_updated_traffic.csv")

traffic_counts = df["traffic_type"].value_counts()

plt.figure()
plt.pie(traffic_counts, labels=traffic_counts.index, autopct="%1.1f%%")

plt.title("Traffic Type Distribution")

plt.show()