import numpy as np
import libs.line.funcs as line
import libs.triangle.funcs as tri

# Coefficient matrix A and RHS vector b
A = np.array([[3, -1],
              [4, -1]], dtype=float)
b = np.array([3, 8], dtype=float)

# Solve system A x = b
x = np.linalg.solve(A, b)

num, den = x[0], x[1]

print("x =", num)
print("y =", den)
print("Fraction = {}/{}".format(int(num), int(den)))

