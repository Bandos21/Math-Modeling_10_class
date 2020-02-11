import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)
N=100
alpha = np.linspace(10,0,N)

phi = np.linspace(0,2*np.pi,100)
theta = np.linspace(0,4*np.pi,100)

x1 = np.outer(phi, np.cos(theta))
y1 = np.outer(phi, np.sin(theta))
z1 = 2 * np.outer(np.ones(np.size(phi)), theta  )

ax.plot_surface(x1,y1,z1,color='g')

x = phi * np.cos(theta)
y = phi * np.sin(theta)
z = 2 * theta

ball, = ax.plot(x, y, z, 'o', color='b')
line, = ax.plot(x, y, z, '-', color='b')

def animation_func(i):
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])

ax.set_xlim3d([-10.0, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([0, 20.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-10.0, 10.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)




ani.save('ani.gif')















