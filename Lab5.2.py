import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a=2,b=3,c=8,title="parabola_plotter"):
    x=np.arange(-10,10,0.01)
    y=a*x**2+b*x+c
    plt.plot(x,y)
parabola_plotter(1)
def giperbola_plotter(title="giperbola_plotter"):
    x=np.arange(0.01,10,0.01)
    y=1/x
    plt.plot(x,y)
    x=np.arange(-10,-0.01,0.01)
    y=1/x
    plt.plot(x,y)
giperbola_plotter(1) 
plt.show   

