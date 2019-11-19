import matplotlib.pyplot as plt
import numpy as np
from  matplotlib.animation import ArtistAnimation
fig=plt.figure()
def circle_func(x_centre_point,
                y_centre_point,
                R,
                N):
   for i in range(N):
       alpha=np.linspace(-5,5,N)
       x[i]=x_centre_point+R*np.cos(alpha[i])
       y[i]=y_centre_point+R*np.sin(alpha[i])
       return x, y
x_centre_move=np.linspace(-5,5,N)
y_centre_move=x_centre_move*x_centre_move+2*x_centre_move+10
anim_list=[]
N=100
for i in range(0,N,1):
    x, y=circle_func(x_centre_move[i],
                    y_centre_move[i],
                    R=0.05,
                    N=N)
    circle,=plt.plot(x,y,'ro',lw=2)
    anim_list.append([circle])
plt.axis('equal')
ani=ArtistAnimation(fig,anim_list,interval=50)
ani.save('ani.gif')

