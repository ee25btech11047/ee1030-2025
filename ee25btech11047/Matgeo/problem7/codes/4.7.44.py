import numpy as np
import matplotlib.pyplot as plt
from libs.line.funcs   import *  
from libs.triangle.funcs import *   

# --- Plane normal and constant ---
n = np.array([2/7, 3/7, -6/7])
c = 1

# --- Origin ---
origin = np.array([0, 0, 0])

# --- Closest point from origin to plane ---
closest_point = (c / np.dot(n, n)) * n
d = np.linalg.norm(closest_point)

print("Closest point:", closest_point)
print("Distance:", d)

# --- Basis vectors lying in the plane ---
u = np.array([n[1], -n[0], 0])
if np.allclose(u, 0):
    u = np.array([0, n[2], -n[1]])
v = np.cross(n, u)

u = u / np.linalg.norm(u) * 2
v = v / np.linalg.norm(v) * 2

# Define four corners of a plane patch (parallelogram)
p1 = closest_point + u + v
p2 = closest_point - u + v
p3 = closest_point - u - v
p4 = closest_point + u - v

# --- Plotting ---
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Plot plane patch (semi-transparent)
ax.plot_trisurf([p1[0], p2[0], p3[0], p4[0]],
                [p1[1], p2[1], p3[1], p4[1]],
                [p1[2], p2[2], p3[2], p4[2]],
                color="cyan", alpha=0.4)

# Line (Origin → Closest Point)
ax.plot([origin[0], closest_point[0]],
        [origin[1], closest_point[1]],
        [origin[2], closest_point[2]],
        color="black", linestyle="--")

# Origin (red with label)
ax.scatter(*origin, color="red", s=60)
ax.text(*origin, "(0,0,0)", color="red", fontsize=9, weight="bold")

# Closest Point (blue with fraction coords as label)
ax.scatter(*closest_point, color="blue", s=60)
ax.text(*closest_point,
        "(2/7, 3/7, -6/7)",
        color="blue", fontsize=9, weight="bold")

# Axes labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Plane with Closest Point from Origin")

plt.show()
