import ctypes
import numpy as np

lib = ctypes.CDLL("./circles.so")

lib.compute_circles.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    np.ctypeslib.ndpointer(dtype=np.float64, shape=(4,2)),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

lib.compute_circles.restype = None

a = 3.0
L = 2*np.sqrt(7)
centers = np.zeros((4,2), dtype=np.float64)
r = ctypes.c_double()
f = ctypes.c_double()

lib.compute_circles(a, L, centers, ctypes.byref(r), ctypes.byref(f))

print("Results from shared library:\n")
for i in range(4):
    h, k = centers[i]
    print(f"Circle {i+1}: Centre = ({round(h,2)}, {round(k,2)}), Radius = {round(r.value,2)}")

print(f"\nConstant term f = {round(f.value,2)}")

