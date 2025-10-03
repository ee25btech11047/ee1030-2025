import ctypes

# Load shared library
lib = ctypes.CDLL("./libmatrix.so")

# Define argument and return types
lib.find_k.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.find_k.restype = ctypes.c_int

# Prepare variables
k1 = ctypes.c_double()
k2 = ctypes.c_double()

# Call function
n = lib.find_k(ctypes.byref(k1), ctypes.byref(k2))

# Print results
if n == 0:
    print("No real values of k")
elif n == 2:
    print("Values of k for which matrix is singular:")
    print("k =", k1.value)
    print("k =", k2.value)

