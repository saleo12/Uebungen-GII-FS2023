import random
import matplotlib.pyplot as plt

x = []
y = []
color = []

for i in range(1000):
    x.append(random.uniform(-100,100))
    y.append(random.uniform(-100,100))
    color.append(random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']))

plt.scatter(x, y, c = color)
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.show()