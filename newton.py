from sympy import sympify
import numpy as np

#METODO DE NEWTON-RAPHSON 

#f - função objetivo
#df - derivada de df
#p0 - aproximaçao inicial 
#TOL - tolerância (critério de parada)
#N - número máximo de iterações

def newton(f, df, p0, TOL, N):
    i = 1
    p = 0
    
    while i<=N:

        p = p0- f(p0)/df(p0)

        print('Iteracao - %d, p = %.10f, f(p) = %.15f' % (i, p, f(p)))
    
        if abs(f(p)) <= TOL:
            return 'Raiz aproximada: %.10f' % p

        p0 = p
        i += 1

    raise NameError('\nNum. max. de iter. excedido!')

def f(x):
    return np.e**(-x**2)-np.cos(x)
    ##return x**3-x-1
    ##return 4*np.sin(x)-np.e**x
    ##return x*np.log10(x)-1

def df(x):
    h = 1e-7
    return (f(x+h)-f(x))/h

p0 = float(input('Entre com a aproximacao inicial: '))
TOL = float(input('Entre com a tolerancia: '))
N = int(input("Entre com o numero maximo de iteracoes: "))

print(newton(f, df, p0, TOL, N))