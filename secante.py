from sympy import sympify
import numpy as np

#MÉTODO DA SECANTE

#p0 - Aproximação inicial 1
#p1 - Aproximaçao inicial 2
#TOL - tolerância
#N - número máximo de iterações

def secante(p0, p1, TOL, N):
    i = 1

    q0 = f(p0)
    q1 = f(p1)

    while i <= N-1:
        p = p1 - q1*((p1-p0)/(q1-q0))

        print('Iteracao - %d, p = %0.10f and f(p) = %0.10f' % (i, p, f(p)))
    
        if abs(f(p)) <= TOL:
           return 'Raiz aproximada = %.10f' % p
        i += 1

        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    raise NameError('\nNum. max. de iter. excedido!')

def f(x):
    return np.e**(-x**2)-np.cos(x)
    ##return x**3-x-1
    ##return 4*np.sin(x)-np.e**x
    ##return x*np.log10(x)-1

#funcao = input('\nEntre com sua funcao: ')
#func = sympify(funcao)
#f = lambda x:func.subs({'x':x})

p0 = float(input('Entre com a aproximacao inicial p0: '))
p1 = float(input('Entre com a aproximacao inicial p1: '))
TOL = float(input('Entre com a tolerancia: '))
N = int(input("Entre com o numero maximo de iteracoes: "))

print(secante(p0,p1,TOL,N))