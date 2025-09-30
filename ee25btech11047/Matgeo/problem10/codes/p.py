import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libgauss.so")

# Function signature: int solve_system(double *A_in, double *x_out)
lib.solve_system.argtypes = [ctypes.POINTER(ctypes.c_double),
                             ctypes.POINTER(ctypes.c_double)]
lib.solve_system.restype = ctypes.c_int

# Input augmented matrix [A|b]
A = np.array([
    [3, -1, -2,  2],   # 3x - y - 2z = 2
    [0,  2, -1, -1],   # 2y - z = -1
    [3, -5,  0,  3]    # 3x - 5y = 3
], dtype=np.float64)

A_flat = A.flatten()
x_out = np.zeros(3, dtype=np.float64)

# Call the C function
status = lib.solve_system(A_flat.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                          x_out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

if status == 1:
    print("System is inconsistent -> No solution")
else:
    print("Solution:", x_out)

