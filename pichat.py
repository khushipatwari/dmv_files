import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [40, 25, 20, 15]

plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Static Pie Chart")
plt.axis('equal')
plt.show()
