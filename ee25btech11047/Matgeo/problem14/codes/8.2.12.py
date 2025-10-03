
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# local imports
from libs.line.funcs import *
from libs.conics.funcs import *

# Matrix form: x^T V x + 2u^T x + f = 0
V = np.array(([36,0],[0,4]))
u = np.array(([0,0])).reshape(-1,1)
f = -144

# Get parameters
n,c,F,O,lam,P,e = conic_param(V,u,f)
ab = ellipse_param(V,u,f)

print("Eigenvalues =", lam)
print("Rotation matrix P =\n", P)
print("Semi-axes a,b =", ab)

# Compute eccentricity from matrix formula
lam1, lam2 = min(lam), max(lam)
f0 = u.T @ LA.inv(V) @ u - f
f0 = f0.item()
ecc = np.sqrt(1 - lam1/lam2)
print("f0 =", f0, "eccentricity =", ecc)

# Compute c using big formula
c_val = np.array([
    (ecc*u.T@n + np.sqrt(
        ecc**2*(u.T@n)**2 - lam2*(ecc**2-1)*(LA.norm(u)**2 - lam2*f)
    )) / (lam2*ecc*(ecc**2-1)),
    (ecc*u.T@n - np.sqrt(
        ecc**2*(u.T@n)**2 - lam2*(ecc**2-1)*(LA.norm(u)**2 - lam2*f)
    )) / (lam2*ecc*(ecc**2-1))
], dtype=float).flatten()

print("Directrix constants c =", c_val)

# Generate ellipse points
xStandard = ellipse_gen_num(ab[0], ab[1], 100)

# Directrix lines
k1, k2 = -1, 1
x_A = line_norm(n,c_val[0],k1,k2)
x_C = line_norm(n,c_val[1],k1,k2)

# Plot
plt.plot(xStandard[0,:], xStandard[1,:], label='Ellipse')
plt.plot(x_A[0,:], x_A[1,:], label='Directrix 1')
plt.plot(x_C[0,:], x_C[1,:], label='Directrix 2')

# Plot center, foci
plt.scatter(O[0],O[1], c='r', label='Center O')
plt.scatter(F[0,:],F[1,:], c='g', label='Foci')

# Annotate
plt.annotate("O", (O[0],O[1]), xytext=(5,5), textcoords="offset points")
for i in range(F.shape[1]):
    x_coord = round(float(F[0, i]), 2)
    y_coord = round(float(F[1, i]), 2)
    coord_text = f"F{i+1} ({x_coord}, {y_coord})"
    plt.annotate(coord_text,
                 (x_coord, y_coord),
                 xytext=(5, -15), textcoords="offset points")

# Axes setup
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.legend()
plt.axis('equal')
plt.grid()
plt.show()

