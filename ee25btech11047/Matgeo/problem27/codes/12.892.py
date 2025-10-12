import numpy as np

# Define the matrix
A = np.array([[3, -1, 1],
              [-1, 5, -1],
              [1, -1, 3]])

# Compute trace
trace = np.trace(A)

# Compute determinant
det = np.linalg.det(A)

# Compute the required value
result = det * trace

print("Trace =", trace)
print("Determinant =", det)
print("lambda1*lambda2*lambda3*(lambda1+lambda2+lambda3) =", result)
