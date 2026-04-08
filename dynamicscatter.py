import matplotlib.pyplot as plt

n = int(input("Enter number of points: "))

x = []
y = []

for i in range(n):
    x_value = float(input(f"Enter x value {i+1}: "))
    y_value = float(input(f"Enter y value {i+1}: "))
    x.append(x_value)
    y.append(y_value)

plt.scatter(x, y, marker='o')

plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()
