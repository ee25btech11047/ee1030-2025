import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./libalpha.so")

# Define argument and return types
lib.compute_alpha.argtypes = [
    (ctypes.c_double * 3 * 3),  # 3x3 matrix
    (ctypes.c_double * 3),      # f vector
    (ctypes.c_double * 3)       # output alpha
]

# Prepare data
U = np.array([
    [1.0, 1.0, 1.0],
    [0.0, 1.0, 1.0],
    [0.0, 0.0, 1.0]
], dtype=np.double)

f = np.array([1.0, 1.0, 1.0], dtype=np.double)
alpha = np.zeros(3, dtype=np.double)

# Convert numpy arrays to ctypes
U_ctypes = (ctypes.c_double * 3 * 3)(*map(lambda row: (ctypes.c_double * 3)(*row), U))
f_ctypes = (ctypes.c_double * 3)(*f)
alpha_ctypes = (ctypes.c_double * 3)(*alpha)

# Call C function
lib.compute_alpha(U_ctypes, f_ctypes, alpha_ctypes)

# Convert result back to numpy array
alpha_result = np.array(list(alpha_ctypes))

print("alpha =", alpha_result)
