import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
t=np.arange(0,10,0.1)
def rand_func(z,t):
    x,v_x,y,v_y = z
    dxdt = v_x
    dv_xdt=f1+f2*np.cos(np.pi/6)+f3*np.cos(np.pi/3)/m
    dydt=v_y
    dv_ydt=f4+f2*np.sin(np.pi/6)+f3*np.sin(np.pi/3)/m
    return dxdt,dv_xdt,dydt,dv_ydt

x0=0
v_x0=10
y0=0
v_y0=-100
z0=x0,v_x0,y0,v_y0

f1=19
f2=11
f3=12
f4=13
m=10

sol=odeint(rand_func,z0,t)
fig=plt.figure()
kryg=[]
for i in range(0,len(t),1):
    telo,=plt.plot(sol[:i,0],sol[:i,2],'-', color='r')
    telo_point,=plt.plot(sol[i,0],sol[i,2],'o', color='r')
    kryg.append([telo,telo_point])
ani=ArtistAnimation(fig,kryg,interval=50)
plt.axis('equal')
ani.save('krug.gif')