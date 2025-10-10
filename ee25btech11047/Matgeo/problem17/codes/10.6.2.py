# Tangents to a circle from an external point
# Using user's libraries: libs.line.funcs and libs.conics.funcs
# Author: ChatGPT (GVV-style corrected)

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Local imports
from libs.line.funcs import line_gen
from libs.conics.funcs import circ_gen

# --- Circle and external point ---
O = np.array([[0.0], [0.0]])     # Centre
r = 4.0                          # Radius
P = np.array([[7.0], [0.0]])     # External point

# --- Tangent point calculation ---
u = P - O
d = float(LA.norm(u))
u_hat = u / d

# Rotation matrix for 90 degrees
R90 = np.array([[0, -1], [1, 0]])

# Tangent points formula
r2 = r**2
sqrt_term = np.sqrt(d**2 - r**2)

A = O + (r2/d)*u_hat + (r/d)*sqrt_term*(R90 @ u_hat)
B = O + (r2/d)*u_hat - (r/d)*sqrt_term*(R90 @ u_hat)

# --- Generate required curves ---
x_circ = circ_gen(O, r)
x_tan1 = line_gen(P, A)
x_tan2 = line_gen(P, B)
x_OP = line_gen(O, P)

# --- Plotting ---
plt.plot(x_circ[0, :], x_circ[1, :] )
plt.plot(x_tan1[0, :], x_tan1[1, :], color='orange' )
plt.plot(x_tan2[0, :], x_tan2[1, :], color='green' )
plt.plot(x_OP[0, :], x_OP[1, :], 'k--')

# --- Mark and label points (rounded neatly) ---
points = {'O': O, 'P': P, 'A': A, 'B': B}
for name, pt in points.items():
    x, y = float(pt[0]), float(pt[1])
    plt.scatter(x, y, s=45, zorder=5)
    plt.text(x + 0.25, y + 0.25,
             f'{name}({round(x,2)}, {round(y,2)})',
             fontsize=9, ha='center')

# --- Axes setup (GVV style) ---
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# --- Style ---
plt.axis('equal')
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Tangents from an External Point to a Circle')
plt.legend(loc='upper right')
plt.show()

