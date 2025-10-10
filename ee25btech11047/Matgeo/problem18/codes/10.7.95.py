import numpy as np
import matplotlib.pyplot as plt
from libs.conics.funcs import *

a = 3
L = 2*np.sqrt(7)
r = float(np.sqrt(a**2 + (L/2)**2))
f = float(a**2 + (L/2)**2 - r**2)

centers = [
    np.array([[ a],[ r]]),
    np.array([[ a],[-r]]),
    np.array([[-a],[ r]]),
    np.array([[-a],[-r]])
]

for i,C in enumerate(centers,1):
    u = -C
    O,R = circ_param(u,f)
    O = np.round(O,2)
    R = round(float(R),2)
    print(f"Circle {i}: Centre = ({O[0,0]}, {O[1,0]}), Radius = {r}")

fig,ax=plt.subplots(figsize=(7,7))
ax.set_aspect('equal',adjustable='box')
ax.grid(True,linestyle='--',alpha=0.6)

for i,C in enumerate(centers,1):
    u = -C
    O,R = circ_param(u,f)
    O = np.round(O,2)
    R = round(float(R),2)
    circ = circ_gen(O,R)
    ax.plot(circ[0,:],circ[1,:],linewidth=1.8)
    ax.scatter(O[0],O[1],color='black',s=25)
    ax.text(O[0]-0.7,O[1]-0.4,f"C{i}({O[0,0]},{O[1,0]})",fontsize=10,bbox=dict(boxstyle="round,pad=0.2",fc="white",alpha=0.7))

ax.axhline(0,color='gray',linewidth=1)
ax.axvline(0,color='gray',linewidth=1)
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Circles touching x-axis at distance 3 and y-intercept 2√7")
plt.show()

