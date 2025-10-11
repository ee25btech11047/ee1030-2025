import math
import numpy as np
import matplotlib.pyplot as plt
from libs.conics.funcs import circ_gen, circ_param

a = 3.0
L = 2.0 * math.sqrt(7.0)
half = L / 2.0
r = math.sqrt(a*a + half*half)
f = a*a

centers = [
    np.array([[ a],[ r]], dtype=float),
    np.array([[ a],[-r]], dtype=float),
    np.array([[-a],[ r]], dtype=float),
    np.array([[-a],[-r]], dtype=float)
]

for i, C in enumerate(centers, 1):
    h = float(round(C[0,0],2))
    k = float(round(C[1,0],2))
    R = float(round(r,2))
    print(f"Circle {i}: Centre = ({h}, {k}), Radius = {R}")

fig, ax = plt.subplots(figsize=(7,7))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--', alpha=0.5)

for i, C in enumerate(centers,1):
    circ = circ_gen(C, r)
    ax.plot(circ[0,:], circ[1,:], linewidth=1.8)
    ax.scatter(float(C[0,0]), float(C[1,0]), color='black', s=25)
    dx = -0.6 if C[0,0] >= 0 else 0.6
    dy = -0.4 if C[1,0] >= 0 else 0.4
    h = float(round(C[0,0],2))
    k = float(round(C[1,0],2))
    ax.text(h + dx, k + dy, f"O{i}({h},{k})", fontsize=10, bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.8))

for s in (a, -a):
    ax.scatter(s, 0, color='red', s=50, marker='x')
    ax.text(s + 0.25, -0.45, f"({s},0)", color='red')

ax.axhline(0, color='gray', linewidth=1)
ax.axvline(0, color='gray', linewidth=1)
ax.set_xlim(-8,8)
ax.set_ylim(-8,8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Circles tangent to x-axis at (±3,0) with y-axis intercept 2√7')
plt.show()

