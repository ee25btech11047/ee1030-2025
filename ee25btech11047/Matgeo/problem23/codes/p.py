import ctypes
import numpy as np

N = 3

# Load the shared library
lib = ctypes.CDLL('./libmatrix.so')

# Define argument types for verify_inverse
lib.verify_inverse.argtypes = [ctypes.POINTER(ctypes.c_double) for _ in range(2)]
lib.verify_inverse.restype = ctypes.c_int

# Example matrix A
A = np.array([[2.0,1.0,1.0],
              [1.0,2.0,1.0],
              [1.0,1.0,2.0]])

# Compute B = inverse of A using numpy
B = np.linalg.inv(A)

# Convert numpy arrays to ctypes
A_ctypes = A.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
B_ctypes = B.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Call C function
result = lib.verify_inverse(A_ctypes, B_ctypes)

if result:
    print("AB = I, hence B = A^-1 (Verified in C via ctypes)")
else:
    print("B is NOT the inverse of A")
