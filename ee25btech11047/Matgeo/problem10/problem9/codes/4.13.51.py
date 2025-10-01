

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


# local imports
from libs.line.funcs import *
from libs.triangle.funcs import *
from libs.conics.funcs import circ_gen

# Given points
A = np.array([-3,4]).reshape(-1,1)
B = np.array([5,4]).reshape(-1,1)

# Centre O lies on x=1 and x-4y=-7
x = 1
y = (x+7)/4
O = np.array([x,y]).reshape(-1,1)

# Opposite vertices
C = 2*O - A
D = 2*O - B

# Side vectors
AB = B - A
AD = D - A

# Area by cross product
area = abs(np.linalg.det(np.hstack((AB,AD))))
print("Area of rectangle =", area)

# Circumcircle radius
r = LA.norm(A - O)

# Circle points
x_circ = circ_gen(O.flatten(), r)

# Plotting
rect_coords = np.hstack((A,B,C,D,O))
labels = ['$A$','$B$','$C$','$D$','$O$']

plt.plot(x_circ[0,:], x_circ[1,:], label='Circumcircle')
plt.plot([A[0,0],B[0,0],C[0,0],D[0,0],A[0,0]],
         [A[1,0],B[1,0],C[1,0],D[1,0],A[1,0]],
         'k-',label='Rectangle')

plt.scatter(rect_coords[0,:], rect_coords[1,:])

for i, txt in enumerate(labels):
    plt.annotate(f'{txt}({rect_coords[0,i]:.0f},{rect_coords[1,i]:.0f})',
                 (rect_coords[0,i], rect_coords[1,i]),
                 textcoords="offset points", xytext=(-10,5), ha='center')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.grid()
plt.axis('equal')
plt.legend()
plt.show()

