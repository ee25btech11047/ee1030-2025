import numpy as np

# Define a square matrix A
A = np.array([
    [1/np.sqrt(2), -1/np.sqrt(2), 0],
    [1/np.sqrt(2),  1/np.sqrt(2), 0],
    [0,             0,            1]
])

# Compute A * A^T
AA_T = A @ A.T

# Check if AA^T is identity
if np.allclose(AA_T, np.eye(A.shape[0])):
    print("Matrix A is orthogonal.")
else:
    print("Matrix A is not orthogonal.")
