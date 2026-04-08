import matplotlib.pyplot as plt

n = int(input("Enter number of data values: "))

data = []

for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    data.append(value)

bins = int(input("Enter number of bins: "))

plt.hist(data, bins=bins, edgecolor='black')

plt.title("Dynamic Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
