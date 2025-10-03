import numpy as np
from libs.matrix.funcs import det   # your custom determinant function

# Define matrix with k
def det_val(k):
    A = np.array([[k, 8],
                  [1, 2*k]], dtype=float)
    return det(A)

solutions = []
for k in range(-10, 11):  # checking a range
    if abs(det_val(k)) < 1e-9:
        solutions.append(k)

print("Values of k for which matrix is singular:", solutions)

