import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL("./conic_kappa.so")

# Define argument/return types
lib.kappa_sum.restype = ctypes.c_double
lib.kappa_sum.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,2)),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,)),
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(2,))
]

lib.compute_k.restype = ctypes.c_double

# ----------------------------
# Given data (same as LaTeX)
# ----------------------------
k = 2.0
V = np.array([[2, 0],
              [0, 0]], dtype=np.float64)
u = np.array([-k*np.sqrt(2)/2, 0], dtype=np.float64)
h = np.array([0, 0], dtype=np.float64)
m = np.array([1, 0], dtype=np.float64)

# Call C function for kappa sum
kappa_sum_val = lib.kappa_sum(V, u, h, m)
print("Computed (κ₁ + κ₂) from .so =", np.round(kappa_sum_val, 4))

# Check against √2
print("Expected =", np.round(np.sqrt(2), 4))

# Plot the conic and intersection points
a, b, c = 2, -k*np.sqrt(2), 1
D = b**2 - 4*a*c
x1 = (-b + np.sqrt(D)) / (2*a)
x2 = (-b - np.sqrt(D)) / (2*a)
x_vals = np.array([x1, x2])
y_vals = np.zeros(2)

# Generate parabola
x_plot = np.linspace(min(x_vals)-1, max(x_vals)+1, 400)
y_plot = 2*x_plot**2 - k*np.sqrt(2)*x_plot + 1

plt.figure(figsize=(7,5))
plt.axhline(0, color='black', linewidth=1)
plt.plot(x_plot, y_plot, 'b', label=r'$2x^2 - 2\sqrt{2}x + 1$')
plt.scatter(x_vals, y_vals, color='red')

# Label points
for (x,y) in zip(x_vals, y_vals):
    plt.text(x, y+0.2, f"({np.round(x,2)}, {np.round(y,2)})",
             ha='center', va='bottom', color='darkred')

plt.text(np.mean(x_vals), max(y_plot)/2,
         f"(κ₁+κ₂) from C = {np.round(kappa_sum_val,3)} ≈ √2",
         fontsize=10, color='purple', ha='center')

plt.legend()
plt.title("κ₁ + κ₂ from C shared library (Conic Intersection)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

