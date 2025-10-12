import numpy as np

# Inputs
trace = 11       # sum of eigenvalues
det = 36         # product of eigenvalues

# List to store valid eigenvalues
valid_eigenvalues = []

# Loop over all possible positive integers for first two eigenvalues
for i in range(1, trace + 1):
    for j in range(1, trace - i + 1):
        k = trace - i - j
        if k > 0 and i * j * k == det:
            eigenvalues = np.array([i, j, k])
            valid_eigenvalues.append(eigenvalues)
            print("Eigenvalues:", eigenvalues)
            print("Largest eigenvalue:", np.max(eigenvalues))

# If needed, store the largest eigenvalue among all triplets
if valid_eigenvalues:
    largest_overall = max(np.max(triplet) for triplet in valid_eigenvalues)
    print("Largest eigenvalue among all triplets:", largest_overall)
