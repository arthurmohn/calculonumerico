from sympy import sympify
import numpy as np

#MÉTODO Do PONTO FIXO

#p0 - Aproximação inicial
#TOL - tolerância
#N - número máximo de iterações
def pontofixo(p0, TOL, N):
    i = 1

    
    while i <= N:

        if abs(f(p0)) <= TOL:
            return  'Iteracao - %d, p0 = %0.10f e f(p0) = %0.10f' % (i, p0, f(p0))

        p = g(p0)
        
        if abs(f(p)) <= TOL:
           return 'Iteracao - %d, p = %0.10f e f(p) = %0.10f' % (i, p, f(p))

        print('Iteracao - %d, p = %0.10f e f(p) = %0.10f' % (i, p, f(p)))

        p0 = p

        i+= 1

    raise NameError('\nNum. max. de iter. excedido!')

def f(x):
    return np.e**(-x**2)-np.cos(x)
    ##return x**3-x-1
    ##return 4*np.sin(x)-np.e**x
    ##return x*np.log10(x)-1

def g(x):
    return np.cos(x)-np.e**(-x**2)+x
    ##return (x+1)**(1/3)
    ##return 2*np.sin(x)+0.5*np.e**x
    ##return x-1.3*(x*np.log10(x)-1)


p0 = float(input('Entre com a aproximacao inicial: '))
TOL = float(input('Entre com a tolerancia: '))
N = int(input("Entre com o numero maximo de iteracoes: "))

print(pontofixo(p0,TOL,N))