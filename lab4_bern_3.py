from const_module_1 import g

def P(m,h,v):
    """Функция для определения полной механической энергии"""
    Ep=m*g*h
    
    Ek=m*v**2/2
    Ef=Ep+Ek
    print(Ef)
m=3
h=8
v=10
P(m,h,v)    