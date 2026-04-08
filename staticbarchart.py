import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.bar(categories, values)

plt.title("Static Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()
