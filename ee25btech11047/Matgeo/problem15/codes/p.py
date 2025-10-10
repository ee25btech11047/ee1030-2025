import ctypes

# Load shared library
lib = ctypes.CDLL('./libparab_area.so')

# Define function signature
lib.parab_area.argtypes = [ctypes.POINTER(ctypes.c_double), 
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double)]

# Prepare variables
x1 = ctypes.c_double()
y1 = ctypes.c_double()
x2 = ctypes.c_double()
y2 = ctypes.c_double()
area = ctypes.c_double()

# Call function
lib.parab_area(ctypes.byref(x1), ctypes.byref(y1), 
               ctypes.byref(x2), ctypes.byref(y2), ctypes.byref(area))

# Print results
print(f"Intersection 1: ({round(x1.value,2)}, {round(y1.value,2)})")
print(f"Intersection 2: ({round(x2.value,2)}, {round(y2.value,2)})")
print(f"Area = {round(area.value,4)}")

