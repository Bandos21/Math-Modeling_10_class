import numpy as np 
from scipy.integrate import  odeint 
import matplotlib.pyplot as plt
t=np.arange(0,100,1)
def bio_function(n,t):
    bioploding=k*n
    return bioploding
b_0=2
k= 0.02
solve_bio=odeint(bio_function,b_0,t)
plt.plot(t,solve_bio[:,0], label='Бактериально деление')
plt.legend()
plt.show()