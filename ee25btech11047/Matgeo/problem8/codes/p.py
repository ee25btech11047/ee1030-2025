import numpy as np
import ctypes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# local imports (as per your requirement)
from libs.line import funcs as line_funcs
from libs.triangle import funcs as tri_funcs

# Given plane parameters
n1 = np.array([1, 3, 0], dtype=float)
n2 = np.array([3, -1, -4], dtype=float)
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

# Normals in n^T x = 1 form
n_case1 = (n1 + lambda1*n2) / (c1 + lambda1*c2)
n_case2 = (n1 + lambda2*n2) / (c1 + lambda2*c2)

# -------- Shared Output Style --------
print("=== Shared Output with ctypes ===")
print("Solutions for λ:")
print("λ1 =", ctypes.c_double(lambda1).value)
print("λ2 =", ctypes.c_double(lambda2).value)

print("\nPlane equations in n^T x = 1 form:")
print("1) ", [ctypes.c_double(val).value for val in n_case1], "· x = 1")
print("2) ", [ctypes.c_double(val).value for val in n_case2], "· x = 1")

# -------- Plotting --------
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

fig = plt.figur

