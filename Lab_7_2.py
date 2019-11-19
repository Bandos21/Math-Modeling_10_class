import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig = plt.figure()
def circle_func(x_centre_point, y_centre_point, r, n):
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(0 ,n, 1):
        alpha = np.linspace(0, 2 * np.pi, n)
        x[i] = x_centre_point + r * np.cos(alpha[i])
        y[i] = y_centre_point + r * np.sin(alpha[i])
    return x, y
thetas = np.linspace(0, 4 * np.pi, 100)
r = 16
n = 100
x_centre = r * np.cos(thetas) ** 3
y_centre = r * np.sin(thetas) ** 3
anim_list = []
for i in range(0 ,n ,1):
    x, y = circle_func(x_centre[i], y_centre[i], r/4, n)
    circle, = plt.plot(x, y, 'r-', lw=2)
    circle_main, = plt.plot(x, y, 'k-', lw=2)
    point, = plt.plot(x_centre[i], y_centre[i], 'bo', markersize=4)
    anim_list.append([circle, point])
ani = ArtistAnimation(fig, anim_list, interval=50)
plt.axis('equal')
ani.save('anim1.gif')
