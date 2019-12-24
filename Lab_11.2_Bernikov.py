import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
t=np.arange(0,10,0.1)
def yadro_func(z,t):
    x,v_x,y,v_y = z
    dxdt = v_x
    dv_xdt=(v_x0*np.cos(a)-Fs)/m
    dydt=v_y
    dv_ydt=(v_y0*np.sin(a)-Fs)/m
    return dxdt,dv_xdt,dydt,dv_ydt
x0=0
v_x0=1000
y0=0
v_y0=0
z0=x0,v_x0,y0,v_y0

Fs=1
a=np.pi/4

sol=odeint(rand_func,z0,t)
fig=plt.figure()
kryg=[]
for i in range(0,len(t),1):
    telo,=plt.plot(sol[:i,0],sol[:i,2],'-', color='r')
    telo_point,=plt.plot(sol[i,0],sol[i,2],'o', color='r')
    kryg.append([telo,telo_point])
ani=ArtistAnimation(fig,kryg,interval=50)
plt.axis('equal')
ani.save('yadro.gif')