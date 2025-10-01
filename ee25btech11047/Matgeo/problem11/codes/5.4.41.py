import numpy as np
import libs.line.funcs as line
import libs.triangle.funcs as triangle

# Given matrix
A = np.array([[2, 1, 3],
              [4, -1, 0],
              [-7, 2, 1]], dtype=float)

# Compute inverse using numpy
A_inv = np.linalg.inv(A)

# Display results
print("Matrix A:")
print(A)
print("\nInverse of A:")
print(A_inv)

# Verification
I_check = A @ A_inv
print("\nVerification A * A_inv = ")
print(I_check)

