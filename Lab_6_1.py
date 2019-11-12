import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
t=np.arange(-4*np.pi,4*np.pi,0.1)
R=3
x=R*(t-sin(t))
y=R*(1-cos(t))
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.plot(x,y,linestyle='--',lw=5)
plt.show()