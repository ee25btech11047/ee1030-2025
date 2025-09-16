import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-6, 10, 100)   
y = x/2 - 2
X = [0, 2, 4, 1, math.sqrt(2) ]
Y = [2, 0, 0, 1, 4*math.sqrt(2)]

plt.plot(x, y, 'r-', label="x-2y=4")
plt.plot(X, Y, 'ko')  

plt.text(8.17, 1.76, "x-2y=4", fontsize=12, color='black')

for i in range(len(X)-1):
    plt.text(X[i]+0.1, Y[i]+0.1, f"({X[i]},{Y[i]})", fontsize=10, color='black')

plt.text(X[4]+0.1, Y[4]+0.1, f"({X[4]:.2f},{Y[4]:.2f})", fontsize=10, color='black')

plt.axvline(x=0, color='k', linewidth=1.5)

plt.axhline(y=0, color='k', linewidth=1.5)
plt.title("Plot of the given line and points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis('equal')
plt.grid(True)
plt.savefig("../figs/plot.png")
plt.show()
