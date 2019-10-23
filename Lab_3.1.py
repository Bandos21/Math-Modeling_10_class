
from const_mod import g
from math import cos, tan, pi
h=100
B=30*pi/180
a=pi/3
v=((g*h*(1/tan(B)**2))/2*cos(a)**2*(1-1/tan(B)*1/tan(a)))**0.5
print(v)
print()
from const_mod import k, e, h
from math import pi
T=200
E=300
N=2/pi**0.5*h/(k*T)**1.5*e**E/k*T*E**T/2
print(N)