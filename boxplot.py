import numpy as np
import matplotlib.pyplot as plt

# Create the exact 30x30 dataset (1 to 900)
data = np.arange(1, 901).reshape(30, 30)

# BOXPLOT (column-wise → 30 boxplots)
plt.figure(figsize=(12, 6))
plt.boxplot(data)

plt.title("Boxplot of 30x30 Dataset (1 to 900)")
plt.xlabel("Columns")
plt.ylabel("Values")

plt.show()