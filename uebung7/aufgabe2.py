import matplotlib.pyplot as plt
import numpy as np
from math import *

def f(x,y):
    return np.exp(-x**2)*np.sin(y)

x = np.linspace(-2*np.pi, 2*np.pi,100)
y = np.linspace(-2*np.pi, 2*np.pi,100)

X, Y = np.meshgrid(x, y)

Z = f(X,Y)

plt.pcolormesh(X, Y, Z)
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.show()