import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *

# Given normals and constants
n1 = np.array([1, 3, 0])
n2 = np.array([3, -1, -4])
c1, c2 = -6, 0

# Inner products
n1n1 = np.dot(n1, n1)
n1n2 = np.dot(n1, n2)
n2n2 = np.dot(n2, n2)

# Quadratic coefficients
A = c2**2 - n2n2
B = 2*c1*c2 - 2*n1n2
C = c1**2 - n1n1

disc = B**2 - 4*A*C
if disc < 0:
    raise ValueError("No real solutions for λ")

lambda1 = (-B + np.sqrt(disc)) / (2*A)
lambda2 = (-B - np.sqrt(disc)) / (2*A)

# Compute normals in n^T x = 1 form
n_case1 = (n1 + lambda1*n2) / (c1 + lambda1*c2)
n_case2 = (n1 + lambda2*n2) / (c1 + lambda2*c2)

print("Plane 1: ", n_case1, "· x = 1")
print("Plane 2: ", n_case2, "· x = 1")

# -------- Plotting --------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Meshgrid
x = np.linspace(-4, 4, 20)
y = np.linspace(-4, 4, 20)
X, Y = np.meshgrid(x, y)

def plane_eq(normal, X, Y):
    a, b, c = normal
    if abs(c) < 1e-6:
        return np.full_like(X, np.nan)
    return (1 - a*X - b*Y) / c

Z1 = plane_eq(n_case1, X, Y)
Z2 = plane_eq(n_case2, X, Y)

# Plot both planes
ax.plot_surface(X, Y, Z1, alpha=0.6, color='lightblue', label="Plane 1")
ax.plot_surface(X, Y, Z2, alpha=0.6, color='lightgreen', label="Plane 2")

# Origin
ax.scatter(0, 0, 0, color='red', s=50)
ax.text(0, 0, 0, "(0,0,0)", color='red')

# Intersection line: cross product of n1 and n2 gives direction
d = np.cross(n1, n2)
# Solve for one point on the line (z=0 case)
A_mat = np.vstack([n1, n2])
b_vec = np.array([c1, c2])
# Take only x,y by ignoring z in this solve
P = np.linalg.lstsq(A_mat[:, :2], b_vec, rcond=None)[0]
point = np.array([P[0], P[1], 0])
t = np.linspace(-3, 3, 2)
line_points = (point.reshape(3,1) + np.outer(d, t))
ax.plot(line_points[0,:], line_points[1,:], line_points[2,:], 'k--', label="Intersection line")

# Labels
ax.text(line_points[0,0], line_points[1,0], line_points[2,0], "Line of Intersection", color='black')

# Axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Planes through intersection at unit distance from origin")
ax.view_init(20, 30)

plt.show()

