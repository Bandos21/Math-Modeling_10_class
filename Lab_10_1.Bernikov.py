import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t=np.arange(0,20,0.01)
def diff_func(z,t):
    y,omega=z
    dy_dt=omega
    domega_dt=-np.sin(y)*omega-3*y*t-5
    return dy_dt,domega_dt
y0=0.01
omega0=0.05
z0=y0,omega0
sol=odeint(diff_func,z0,t)
plt.plot(sol[:,1],sol[:,0],label='амега(икс)')
plt.legend
plt.show