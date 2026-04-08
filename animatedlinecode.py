import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

x_data = []
y_data = []

line, = ax.plot([], [], marker='o')

ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

def update(frame):
    x_data.append(frame)
    y_data.append(frame * 10)
    line.set_data(x_data, y_data)
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(11), interval=500)

plt.title("Animated Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
