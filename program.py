from sympy import *

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

#Aproximação Avançada Delta x = 10^-2


if __name__=='__main__':
    fun()
    d_fun()
    d_funQ()
    analitic()