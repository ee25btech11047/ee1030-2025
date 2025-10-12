import numpy as np

# Define matrix L and vector b
L = np.array([
    [3, -1, -1, -1],
    [-1, 2, -1, 0],
    [-1, -1, 3, 0],
    [-1, 0, -1, 1]
], dtype=float)

b = np.array([1, 1, 1, 1], dtype=float)

# Step 1: Make R1 = R1 + R2 + R3 + R4
R1 = L[0] + L[1] + L[2] + L[3]

# Check if the new R1 is a zero row
zero_row = np.allclose(R1, np.zeros(4))

# Step 2: Rank of L
rank = np.linalg.matrix_rank(L)

# Step 3: Compatibility condition
sum_b = np.sum(b)

# Step 4: Print results
if zero_row:
    print("Option a) TRUE")
else:
    print("Option a) FALSE")

if rank == 4:
    print("Option b) TRUE")
else:
    print("Option b) FALSE")

if np.isclose(sum_b, 0):
    print("Option c) TRUE")
else:
    print("Option c) FALSE")

if rank == 3:
    print("Option d) TRUE")
else:
    print("Option d) FALSE")
