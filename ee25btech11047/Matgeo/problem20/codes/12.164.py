import numpy as np

# Define matrix A
A = np.array([
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
], dtype=float)

# Step 1: Eigenvalues
eigenvalues, _ = np.linalg.eig(A)
print("Eigenvalues:")
for i, val in enumerate(eigenvalues, start=1):
    print(f"λ{i} = {val:.2f}")

# Step 2: For eigenvalue = 1, compute (A - I)
I = np.eye(3)
AI = A - I

print("\nMatrix (A - I):")
print(AI)

# Step 3: Find null space to get eigenvectors
# (A - I)x = 0 → eigenvectors for λ = 1
u, s, vh = np.linalg.svd(AI)
tol = 1e-10
null_mask = (s <= tol)
null_space = np.compress(null_mask, vh, axis=0)

print("\nEigenvectors corresponding to λ = 1:")
if null_space.size == 0:
    print("No eigenvectors found.")
else:
    print(null_space.T)

# Step 4: Number of linearly independent eigenvectors
num_independent = null_space.shape[0]
print(f"\nMaximum number of linearly independent eigenvectors = {num_independent}")

