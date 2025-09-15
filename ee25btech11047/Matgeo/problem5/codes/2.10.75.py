import numpy as np
import matplotlib.pyplot as plt
from libs.rank import rank
from libs.line.funcs import line_dir_pt   # your definition

# Base vectors
a = np.array([1, 2], dtype=float)
b = np.array([3, 1], dtype=float)

# Fixed points
P = a + b
Q = a - b

# Points for k = 0,1,2
R_points = {f"R{k}": a + k*b for k in [0,2]}

# --- Print ranks and matrices ---
def M_matrix(a, b, k):
    col1 = 2*b
    col2 = (k-1)*b
    return np.column_stack((col1, col2))

print("P =", P, "Q =", Q)
for k, R in R_points.items():
    M = M_matrix(a, b, int(k[1]))
    print(f"\n{k}: {R}")
    print("M =\n", M)
    print("rank =", rank(M))

# --- Plotting ---
plt.figure(figsize=(7,6))
ax = plt.gca()
ax.set_aspect("equal")

def to_tuple(arr):
    return tuple(int(x) for x in arr)

# Plot P and Q
ax.scatter(P[0], P[1], color="blue", s=100, zorder=3)
ax.text(P[0]+0.3, P[1]+0.3, f"P {to_tuple(P)}", fontsize=12)

ax.scatter(Q[0], Q[1], color="blue", s=100, zorder=3)
ax.text(Q[0]+0.3, Q[1]+0.3, f"Q {to_tuple(Q)}", fontsize=12)

# Plot R0, R1, R2
for label, pt in R_points.items():
    ax.scatter(pt[0], pt[1], color="red", s=100, zorder=3)
    ax.text(pt[0]+0.3, pt[1]+0.3, f"{label} {to_tuple(pt)}", fontsize=12)

# Line through P and Q
dir_vec = (P - Q).reshape(-1,1)
P_col = P.reshape(-1,1)
line_points = line_dir_pt(dir_vec, P_col, -10, 10)  # smaller range
ax.plot(line_points[0,:], line_points[1,:], 'k--', linewidth=1.8)

# Zoom into region around points
all_points = np.array([P, Q] + list(R_points.values()))
xmin, ymin = np.min(all_points, axis=0) - 2
xmax, ymax = np.max(all_points, axis=0) + 2
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

# Labels & grid
ax.set_xlabel("x-axis", fontsize=13)
ax.set_ylabel("y-axis", fontsize=13)
ax.set_title("Collinearity of P, Q, R(k=0,2)", fontsize=14, weight="bold")
ax.grid(True, linestyle="--", alpha=0.7)

plt.show()
