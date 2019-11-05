import matplotlib.pyplot as plt
import numpy as np
def circlea_plotter(R=2,a=3,b=2,title='circlea_plotter'):
    x=np.arange(-5,5,0.1)
    y=np.arange(-5,5,0.1)
    X,Y=np.meshgrid(x,y)
    fxy=X**2+Y**2
    plt.contour(X,Y,fxy,levels=[R**2])
    fxy=X**2/a**2+Y**2/b**2
    plt.contour(X,Y,fxy,levels=[1])
    plt.show()
circlea_plotter(1)

    