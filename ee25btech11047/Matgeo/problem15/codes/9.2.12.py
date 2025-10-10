
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# Local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import *

# Setting up plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid()

# Conic parameters for y^2 = x
V = np.array(([0,0],[0,1]))
u = np.array(([-0.5,0]))
f = 0

# Line parameters x = h + k*m  (x = 2y)
h = np.array(([0,0]))
m = np.array(([2,1]))

# Function g(h)
def g(h,V,u,f):
    return h@V@h + 2*u@h + f

# Compute intersections using formula
mtVm = m@V@m
mVu = m@(V@h + u)
disc = mVu**2 - g(h,V,u,f)*mtVm
kappa1 = (-mVu + np.sqrt(disc))/mtVm
kappa2 = (-mVu - np.sqrt(disc))/mtVm

x1 = h + kappa1*m
x2 = h + kappa2*m

# Generate full parabola
y_parab = np.linspace(-3,3,400)
x_parab = y_parab**2
plt.plot(x_parab,y_parab,label='$y^2=x$',color='r')

# Generate full line
y_line = np.linspace(-3,3,400)
x_line = 2*y_line
plt.plot(x_line,y_line,label='$x=2y$',color='b')

# Shade the bounded area between y=0 and y=2
y_fill = np.linspace(0,2,200)
x_left = y_fill**2
x_right = 2*y_fill
plt.fill_betweenx(y_fill, x_left, x_right, color='blue', alpha=0.3)

# Intersection points
points = np.vstack((x1,x2)).T
plt.scatter(points[0,:],points[1,:],color='k')

# Labels with rounding
labels = [f"$({round(points[0,i],1)},{round(points[1,i],1)})$" for i in range(2)]
for i, txt in enumerate(labels):
    plt.annotate(txt,
                 (points[0,i], points[1,i]),
                 textcoords="offset points",
                 xytext=(0,5),
                 ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.title("Parabola $y^2=x$ and Line $x=2y$ with Bounded Area")
plt.show()

