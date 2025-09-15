import numpy as np
import matplotlib.pyplot as plt
# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

# Points
A = np.array([1, 2]).reshape(-1,1)
B = np.array([3, 6]).reshape(-1,1)

# Direction vector AB
d = B - A

# Normal vector n (perpendicular to AB)
n = np.array([-d[1,0], d[0,0]]).reshape(-1,1)

# Compute c using point A
c = (n.T @ A)[0,0]

# Line equation: y = (c - n1*x)/n2
x_vals = np.linspace(0, 5, 100)
y_vals = (c - n[0,0]*x_vals)/n[1,0]

# Plot
plt.figure(figsize=(6,6))

# Line
plt.plot(x_vals, y_vals, 'b-', label='Line AB')

# Points with coordinates labeled
plt.plot(A[0,0], A[1,0], 'ro')  
plt.text(A[0,0]+0.1, A[1,0]+0.1, f'A({A[0,0]}, {A[1,0]})', fontsize=12, color='red')

plt.plot(B[0,0], B[1,0], 'go')  
plt.text(B[0,0]+0.1, B[1,0]+0.1, f'B({B[0,0]}, {B[1,0]})', fontsize=12, color='green')

# Axes and grid
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line through points A and B')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
