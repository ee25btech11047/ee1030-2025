import ctypes
import os

# Load shared library
lib = ctypes.CDLL(os.path.abspath("./libellipse.so"))

# Define the struct (must match C struct)
class EllipseResult(ctypes.Structure):
    _fields_ = [
        ("f0", ctypes.c_double),
        ("eccentricity", ctypes.c_double),
        ("a", ctypes.c_double),
        ("b", ctypes.c_double),
        ("c_directrix", ctypes.c_double),
        ("Fy", ctypes.c_double),
        ("latus_rectum", ctypes.c_double)
    ]

# Set return type of the function
lib.compute_ellipse.restype = EllipseResult

# Call the function
res = lib.compute_ellipse()

print(f"f0 = {res.f0}")
print(f"Eccentricity = {res.eccentricity}")
print(f"Semi-major a = {res.a}, Semi-minor b = {res.b}")
print(f"Directrix constant c = {res.c_directrix}")
print(f"Foci y = {res.Fy}")
print(f"Latus rectum = {res.latus_rectum}")

