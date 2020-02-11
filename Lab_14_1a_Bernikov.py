import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0,2*np.pi,100)
theta = np.linspace(0,2*np.pi,100)

x = np.outer(phi, np.cos(theta))
y = np.outer(phi,np.sin(theta))
z = np.outer(phi**2, np.ones(np.size(theta)))

ax.plot_surface(x,y,z,color='y')
plt.show