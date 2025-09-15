import ctypes
import numpy as np

# load library
lib = ctypes.CDLL("./librank.so")

# function signature
lib.compute_rank.argtypes = [
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
]
lib.compute_rank.restype = ctypes.c_int

def compute_rank(a, b, k):
    n = len(a)
    a = np.array(a, dtype=np.int32)
    b = np.array(b, dtype=np.int32)
    col1 = np.zeros(n, dtype=np.int32)
    col2 = np.zeros(n, dtype=np.int32)

    r = lib.compute_rank(
        n,
        a.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
        b.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
        k,
        col1.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
        col2.ctypes.data_as(ctypes.POINTER(ctypes.c_int)),
    )
    return col1.tolist(), col2.tolist(), r

if __name__ == "__main__":
    a = [1, 2]
    b = [3, 1]
    for k in [0, 1, 2]:
        col1, col2, r = compute_rank(a, b, k)
        print(f"\nFor k={k}:")
        for i in range(len(a)):
            print(f"[{col1[i]:3d}  {col2[i]:3d}]")
        print("Rank =", r)
        if r <= 1:
            print("=> Collinear")
        else:
            print("=> Not collinear")
