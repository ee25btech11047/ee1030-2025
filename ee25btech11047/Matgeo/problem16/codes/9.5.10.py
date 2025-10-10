#Program to plot intersection of a conic with x-axis
#Author: Shashank Reddy
#Format consistent with funcs-based CoordGeo framework

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------
# libs
# ----------------------------------------------------
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import *

# ----------------------------------------------------
# Given polynomial: p(x) = 2x² - k√2 x + 1
# ----------------------------------------------------
k = 2
V = np.array([[2, 0],
              [0, 0]])
u = np.array([[-k*np.sqrt(2)/2],
              [0]])
f = 1

# ----------------------------------------------------
# Intersection with x-axis: y = 0
# Substitute in conic: 2x² - k√2 x + 1 = 0
# ----------------------------------------------------
a = 2
b = -k*np.sqrt(2)
c = 1

# Use function from funcs to compute roots
x1, x2 = quad_roots(a, b, c)
x_vals = np.array([x1, x2])
y_vals = np.zeros(2)

# ----------------------------------------------------
# Compute sum of roots (verification)
# ----------------------------------------------------
sum_roots = x1 + x2
print(f"Sum of zeroes = {np.round(sum_roots,3)} ≈ √2")

# ----------------------------------------------------
# Plot the conic and x-axis intersection
# ----------------------------------------------------
x_plot = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 400)
y_plot = 2*x_plot**2 - k*np.sqrt(2)*x_plot + 1

plt.figure(figsize=(7, 5))
plt.axhline(0, color='black', linewidth=1.2, label='x-axis')
plt.plot(x_plot, y_plot, 'b', label=r'$2x^2 - 2\sqrt{2}x + 1$')
plt.scatter(x_vals, y_vals, color='red', zorder=5)

# Label intersection points inside the plot
for i in range(2):
    label_point(x_vals[i], y_vals[i],
                f"({np.round(x_vals[i],2)}, {np.round(y_vals[i],2)})",
                offset=(0,0.2), color='darkred')

# Display sum of zeroes
plt.text(np.mean(x_vals), max(y_plot)/2,
         f"Sum of zeroes = {np.round(sum_roots, 3)} ≈ √2",
         fontsize=10, color='purple', ha='center')

plt.title("Intersection of Conic with x-axis")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

