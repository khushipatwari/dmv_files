import matplotlib.pyplot as plt

n = int(input("Enter number of categories: "))

categories = []
values = []

for i in range(n):
    category = input(f"Enter category {i+1}: ")
    value = float(input(f"Enter value for {category}: "))
    categories.append(category)
    values.append(value)

plt.bar(categories, values)

plt.title("Dynamic Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis='y')

plt.show()
