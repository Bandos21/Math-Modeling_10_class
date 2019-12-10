import numpy as np 
from scipy.integrate import  odeint 
import matplotlib.pyplot as plt
t=np.arange(0,100,1)
def speedup_function(v,t):
    zavizspeed= f/m-(k*v**2)/m
    return zavizspeed
v=0
f=10
k=0.5
m=100
solve_speed=odeint(speedup_function,n_0,t)
plt.plot(t,solve_speed[:,0], label='Скорость. Я - скорость')
plt.legend()
plt.show()

