import ctypes
import numpy as np
import matplotlib.pyplot as plt
# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

# Load C shared library
lib = ctypes.CDLL('./libline.so')

# Define argument and return types
lib.line_normal.argtypes = [ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double),
                            ctypes.POINTER(ctypes.c_double)]

# Points
Ax, Ay = 1.0, 2.0
Bx, By = 3.0, 6.0

# Prepare output variables
n1 = ctypes.c_double()
n2 = ctypes.c_double()
c  = ctypes.c_double()

# Call the C function
lib.line_normal(Ax, Ay, Bx, By, ctypes.byref(n1), ctypes.byref(n2), ctypes.byref(c))

print("Normal vector n =", n1.value, n2.value)
print("Scalar c =", c.value)

# Line: y = (c - n1*x)/n2
x_vals = np.linspace(0, 5, 100)
y_vals = (c.value - n1.value * x_vals)/n2.value

# Plot
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, 'b-', label='Line AB')

# Points labeled with coordinates
plt.plot(Ax, Ay, 'ro')
plt.text(Ax+0.1, Ay+0.1, f'A({Ax}, {Ay})', fontsize=12, color='red')

plt.plot(Bx, By, 'go')
plt.text(Bx+0.1, By+0.1, f'B({Bx}, {By})', fontsize=12, color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line through points A and B (computed via C + ctypes)')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()
