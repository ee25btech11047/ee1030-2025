import numpy as np
import matplotlib.pyplot as plt

# local imports as you asked
import libs.line.funcs as linefuncs
import libs.triangle.funcs as trifuncs

# Coefficients of the system Ax=b
A = np.array([
    [3, -1, -2],
    [0,  2, -1],
    [3, -5,  0]
], dtype=float)

b = np.array([2, -1, 3], dtype=float)

# Check consistency via rank
rankA = np.linalg.matrix_rank(A)
rankAb = np.linalg.matrix_rank(np.c_[A, b])

print("Rank(A) =", rankA)
print("Rank([A|b]) =", rankAb)

if rankA != rankAb:
    print("System is inconsistent -> No solution")

# --- Plot the planes ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for x,y
x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Equation 1: 3x - y - 2z = 2 -> z = (3x - y - 2)/2
Z1 = (3*X - Y - 2)/2

# Equation 2: 2y - z = -1 -> z = 2y + 1
Z2 = 2*Y + 1

# Equation 3: 3x - 5y = 3 -> (no z term, it's a vertical plane)
# So plot separately
Z3 = np.linspace(-5, 5, 50)
X3, Z3m = np.meshgrid(x_vals, Z3)
Y3 = (3*X3 - 3)/5

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.5, color='red', label='Plane 1')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='blue', label='Plane 2')
ax.plot_surface(X3, Y3, Z3m, alpha=0.5, color='green', label='Plane 3')

# Labels
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Three Planes (Inconsistent System)")

plt.show()

