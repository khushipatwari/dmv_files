import matplotlib.pyplot as plt

data = [12, 15, 13, 10, 18, 20, 22, 19, 14, 16, 11, 17]

plt.hist(data, bins=5)

plt.title("Static Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.grid(axis='y')
plt.grid(axis='x')

plt.show()
