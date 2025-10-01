import ctypes
import numpy as np
import libs.line.funcs as line
import libs.triangle.funcs as triangle

# Load shared library
lib = ctypes.CDLL("./libinverse.so")

# Define function signature
lib.inverse.argtypes = [ctypes.POINTER(ctypes.c_double),
                        ctypes.POINTER(ctypes.c_double)]
lib.inverse.restype = None

# Input matrix
A = np.array([[2, 1, 3],
              [4, -1, 0],
              [-7, 2, 1]], dtype=np.double)

A_inv = np.zeros((3,3), dtype=np.double)

# Call C function
lib.inverse(A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            A_inv.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print("Matrix A:")
print(A)

print("\nInverse from C (via ctypes):")
print(A_inv)

# Verify
print("\nVerification A * A_inv =")
print(A @ A_inv)

