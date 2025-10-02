import numpy as np
import ctypes

# Load shared object
solver = ctypes.CDLL("./solver.so")

# Define return types and arguments
solver.solve.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C")]

# Prepare output array
out = np.zeros(2, dtype=np.float64)

# Call C function
solver.solve(out)

x, y = out[0], out[1]

print("x =", x)
print("y =", y)
print("Fraction = {}/{}".format(int(x), int(y)))

