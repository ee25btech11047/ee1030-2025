import ctypes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a simple vector class using ctypes
class MyVec(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double),
                ("z", ctypes.c_double)]
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Plane normal n and constant d for n^T x = 1
n = MyVec(2/7, 3/7, -6/7)
d = 1

# Distance from origin formula: |d| / ||n||
norm_n = (n.x**2 + n.y**2 + n.z**2)**0.5
distance = abs(d) / norm_n
print("Distance of plane from origin:", distance)

# Plotting the plane
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid
xx, yy = np.meshgrid(range(-10, 11), range(-10, 11))
# Solve for z using plane equation: n^T x = 1 -> z = (1 - n_x*x - n_y*y)/n_z
zz = (d - n.x*xx - n.y*yy) / n.z

# Plot the plane
ax.plot_surface(xx, yy, zz, alpha=0.5, color='cyan')

# Plot the origin and normal vector
ax.scatter(0, 0, 0, color='red', s=100, label='Origin')
ax.quiver(0, 0, 0, n.x, n.y, n.z, length=5, color='blue', label='Normal n')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Plane and its normal vector')
ax.legend()
plt.show()

