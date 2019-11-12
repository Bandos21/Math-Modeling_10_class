import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig,ax=plt.subplots()
anime,=plt.plot([ ],[ ],marker='o', color='r')
R=5
t=np.arange(-4*np.pi,4*np.pi,0.1)
x=R*np.cos(t)**3
y=R*np.sin(t)**3
plt.plot(x,y,linestyle='--',lw=1)
def astr(R, t):
    x=R*np.cos(t)**3
    y=R*np.sin(t)**3
    return x,y
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
def animat(i):
    anime.set_data(astr(5, i))
ani=FuncAnimation(fig,
                  animat,
                  frames=np.arange(-4*np.pi,4*np.pi,0.1),
                  interval=300)
ani.save('anime_10.gif')

