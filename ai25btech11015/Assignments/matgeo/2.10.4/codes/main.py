import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import ctypes

# #Run the C code to generate var.dat
# dll = ctypes.CDLL("./get_coordinates.so")
# dll.get_coordinates()

# Read arrays from var.dat
with open("var.dat", "r") as f:
	lines = f.readlines()
	A = np.array([int(x) for x in lines[0].split()])
	B = np.array([int(x) for x in lines[1].split()])
	C = np.array([int(x) for x in lines[2].split()])

AB = B - A
AC = C - A

# Area calculation
area = 0.5 * np.linalg.norm(np.cross(AB, AC))
print("Area of triangle ABC:", area)

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Triangle vertices
triangle = np.array([A, B, C])

# Plot triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='blue')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='blue')
ax.plot([C[0], A[0]], [C[1], A[1]], [C[2], A[2]], color='blue')

# Fill triangle surface
ax.add_collection3d(Poly3DCollection([triangle], color='cyan', alpha=0.5))

# Scatter vertices
ax.scatter(A[0], A[1], A[2], color='red')
ax.text(A[0], A[1], A[2], "A", fontsize=12, ha='right')
ax.scatter(B[0], B[1], B[2], color='red')
ax.text(B[0], B[1], B[2], "B", fontsize=12, ha='left')
ax.scatter(C[0], C[1], C[2], color='red')
ax.text(C[0], C[1], C[2], "C", fontsize=12, ha='center')

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Area : " + str(area))

# Save figure
plt.savefig("../figs/fig.png", dpi=300)

