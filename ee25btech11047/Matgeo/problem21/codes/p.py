import ctypes

# Load the shared library
lib = ctypes.CDLL('./eigen.so')

# Define the function argument and return types
lib.find_largest_eigen.argtypes = [ctypes.c_int, ctypes.c_int]
lib.find_largest_eigen.restype = ctypes.c_int

# Inputs
trace = 11
det = 36

# Call the C function
largest = lib.find_largest_eigen(trace, det)

print(f"Largest eigenvalue for trace={trace}, det={det} is: {largest}")
