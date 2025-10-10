import ctypes
import numpy as np
import matplotlib.pyplot as plt
from libs.line.funcs import line_gen
from libs.conics.funcs import circ_gen

# Load the shared library
lib = ctypes.CDLL('./libtangent.so')

# Define argument and return types
lib.tangent_points.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]

# Inputs
r = 4.0
P = np.array([[7.0], [0.0]])

# Prepare output containers
Ax = ctypes.c_double()
Ay = ctypes.c_double()
Bx = ctypes.c_double()
By = ctypes.c_double()

# Call the C function
lib.tangent_points(r, float(P[0]), float(P[1]),
                   ctypes.byref(Ax), ctypes.byref(Ay),
                   ctypes.byref(Bx), ctypes.byref(By))

# Convert results to numpy arrays
O = np.array([[0.0], [0.0]])
A = np.array([[Ax.value], [Ay.value]])
B = np.array([[Bx.value], [By.value]])

print("Tangent Points from C library:")
print(f"A({A[0,0]:.2f}, {A[1,0]:.2f})")
print(f"B({B[0,0]:.2f}, {B[1,0]:.2f})")

# Plot using your libs
x_circ = circ_gen(O, r)
x_tan1 = line_gen(P, A)
x_tan2 = line_gen(P, B)
x_OP = line_gen(O, P)

plt.plot(x_circ[0, :], x_circ[1, :], label='Circle')
plt.plot(x_tan1[0, :], x_tan1[1, :], color='orange', label='Tangent 1')
plt.plot(x_tan2[0, :], x_tan2[1, :], color='green', label='Tangent 2')
plt.plot(x_OP[0, :], x_OP[1, :], 'k--', label='$OP$')

# Mark and label points
points = {'O': O, 'P': P, 'A': A, 'B': B}
for name, pt in points.items():
    x, y = float(pt[0]), float(pt[1])
    plt.scatter(x, y, s=45, zorder=5)
    plt.text(x + 0.25, y + 0.25, f'{name}({round(x,2)}, {round(y,2)})',
             fontsize=9, ha='center')

# GVV-style axes
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.axis('equal')
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Tangents from External Point (using C library)')
plt.legend(loc='upper right')
plt.show()

