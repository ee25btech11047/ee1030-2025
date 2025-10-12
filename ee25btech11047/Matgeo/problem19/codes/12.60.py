import numpy as np

# Define a skew-symmetric matrix B
B = np.array([[0, 2, -1],
              [-2, 0, 3],
              [1, -3, 0]])

# Compute the transpose
B_T = B.T

# Compute -B
neg_B = -B

# Check if transpose equals negative of B
is_skew_symmetric = np.allclose(B_T, neg_B)

print("Matrix B:")
print(B)
print("\nTranspose B^T:")
print(B_T)
print("\nNegative of B (-B):")
print(neg_B)
print("\nIs B skew-symmetric (B^T = -B)?", is_skew_symmetric)
