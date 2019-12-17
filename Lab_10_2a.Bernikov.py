import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,20,0.01)
def diff_func(z,t):
    s,omega=z
    ds_dt=omega
    domega_dt=-g*np.sin(s/l)
    return ds_dt,domega_dt
l=1
g=9.81
s0=1
omega0=0.05
z0=s0,omega0
sol=odeint(diff_func,z0,t)
plt.plot(t,sol[:,0],label='маятник')
plt.legend
plt.show
