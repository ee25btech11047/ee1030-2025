import numpy as np

# Given basis matrix U
U = np.array([
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
], dtype=float)

# Given linear functional f(a,b,c) = a + b + c
f = np.array([1, 1, 1], dtype=float)

# Compute alpha^T = f * U
alpha = f @ U   # matrix multiplication

print("alpha =", alpha)
