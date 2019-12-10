import numpy as np 
from scipy.integrate import  odeint 
import matplotlib.pyplot as plt
t=np.arange(0,15,1)
def investlost_function(n,t):
    moneylost= -k*n*t
    return moneylost
n_0=2
k= 0.08
solve_money=odeint(investlost_function,n_0,t)
plt.plot(t,solve_money[:,0], label='Снижение инвестиций')
plt.legend()
plt.show()
