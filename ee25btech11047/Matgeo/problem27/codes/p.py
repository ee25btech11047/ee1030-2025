import ctypes

# Load the shared library
lib = ctypes.CDLL('./libmatrix_calc.so')

# Tell ctypes the return type of the function
lib.compute_result.restype = ctypes.c_int

# Call the function
result = lib.compute_result()

print("lambda1*lambda2*lambda3*(lambda1+lambda2+lambda3) =", result)
