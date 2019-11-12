import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
t=np.arange(-4*np.pi,4*np.pi,0.1)
R=4
x=R*cos(t)**3
y=R*sin(t)**3
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.plot(x,y,linestyle='--',lw=5)
plt.show()
