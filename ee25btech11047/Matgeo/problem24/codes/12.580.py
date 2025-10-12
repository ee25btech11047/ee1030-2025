import numpy as np

def dimension_W1_plus_W2(n=3):
    # Dimension of V: all n x n complex matrices over R
    dimV = n * n * 2  # 2 real numbers per complex entry

    # Dimension of W1 (Hermitian)
    # Diagonal: n real numbers
    # Off-diagonal: n*(n-1)/2 complex numbers = n*(n-1) real numbers
    dimW1 = n + n*(n-1)

    # Dimension of W2 (trace zero)
    # Trace=0 gives 1 complex constraint = 2 real
    dimW2 = dimV - 2

    # Dimension of W1 ∩ W2
    dimIntersection = dimW1 - 1  # trace constraint reduces 1 real dimension

    # Dimension of W1 + W2
    dimSum = dimW1 + dimW2 - dimIntersection
    return dimSum

if __name__ == "__main__":
    n = 3  # 3x3 matrix
    print(dimension_W1_plus_W2(n))
