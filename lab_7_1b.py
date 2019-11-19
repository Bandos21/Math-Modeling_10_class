  
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig = plt.figure()
def parabol(a, b, c, n):
    x = np.linspace(-5, 5, n)
    y = np.zeros(n)
    for i in range(n):
        y[i] = a * x[i] ** 2 + b * x[i] + c
    return x, y
def cir(x_centre, y_centre, r, n):
    x = np.zeros(n)
    y = np.zeros(n)
    alpha = np.linspace(0, 2 * np.pi, n)
    for i in range(n):
        x[i] = x_centre + r * np.cos(alpha[i])
        y[i] = y_centre + r * np.sin(alpha[i])
    return x, y
n = 100
anim_list = []
x = []
y = []
for i in range(n):
    x, y = parabol(1, 1, 0, n)
    x_cir, y_cir = cir(x[i], y[i], 3, n)
    circle, = plt.plot(x_cir, y_cir, 'g-', lw=2)
    parabola, = plt.plot(x[:i+1], y[:i+1], 'r-', lw=2)
    point, = plt.plot(x[i], y[i], 'o', markersize=4)
    anim_list.append([parabola, circle, point])
ani = ArtistAnimation(fig, anim_list, interval=50)
plt.axes().set_aspect('equal')
ani.save('anim.gif')