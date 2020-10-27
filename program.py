from sympy import *
from Decimal import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

#função
def fun():
    global a
    a = cos(2 * pi * 60 * x)
    print(a)

#primeira derivada de fun()
def d_fun():
    global d_fun
    d_fun = diff(a, x, 1)
    print(d_fun)

#quinta derivada de fun()
def d_funQ():
    d_funQ = diff(a, x, 5)
    print(d_funQ)

#Valor analítico da derivada em x = pi/4
def analitic():
    print(d_fun.subs(x, pi/4))

#Aproximação Avançada deltax = 10^-2
def aproxSimples():
    f = -120*pi*sin(120*pi*pi/4)
    print(double(f))
    print(float(f))

if __name__=='__main__':
    fun()
    d_fun()
    #d_funQ()
    #analitic()
    aproxSimples()