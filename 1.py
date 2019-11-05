import matplotlib.pyplot as plt

def lense(l='собирающая', f=500):
    x = [0,0]
    y = [0,1000]
    plt.plot(x,y,marker="^",color='k')
    y = [0,-1000]
    plt.plot(x,y,marker="v",color='k')
    x = [0,0]
    y = [0,0]
    plt.plot(x,y,marker="o",color='k')
    x = [-1000,0]
    y = [0,0]
    plt.plot(x,y,marker='<',color='k')
    x = [0,1000]
    y = [0,0]
    plt.plot(x,y,marker='>',color='k')
    x = [f,f]
    y = [0,0]
    plt.plot(x,y,marker='o',color='k')
    x = [-1000,0]
    y = [500,500]
    plt.plot(x,y,marker='>',color='b')
    x = [0,f]
    y = [500,0]
    plt.plot(x,y,marker='>',color='b')
    plt.legend()
    plt.show()
    
    
lense()