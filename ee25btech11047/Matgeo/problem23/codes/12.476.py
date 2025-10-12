import numpy as np

# Example 3x3 matrix A
A = np.array([[2, 1, 1],
              [1, 2, 1],
              [1, 1, 2]])

# Suppose B satisfies AB = I
# Compute B = inverse of A
B = np.linalg.inv(A)

# Verify AB = I
AB = np.dot(A, B)

print("Matrix A:\n", A)
print("\nMatrix B (A^-1):\n", B)
print("\nAB:\n", AB)

# Check if AB is approximately identity
if np.allclose(AB, np.eye(3)):
    print("\nHence, B = A^-1")
else:
    print("\nB is NOT the inverse of A")
