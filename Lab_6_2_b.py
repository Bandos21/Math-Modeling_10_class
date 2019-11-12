import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig,ax=plt.subplots()
anime,=plt.plot([ ],[ ],marker='o', color='r')
t=np.arange(-4*np.pi,4*np.pi,0.1)
R=5
x=R*(t-np.sin(t))
y=R*(1-np.cos(t))
plt.plot(x,y,linestyle='--',lw=1)
def cikl(R,t):
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    return x,y
ax.set_xlim(-110,110)
ax.set_ylim(-5,15)
def animat(i):
    anime.set_data(cikl(5, i))
ani=FuncAnimation(fig,
                  animat,
                  frames=np.arange(-4*np.pi,4*np.pi,0.1),
                  interval=300)
ani.save('anime_20.gif')
