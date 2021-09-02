from sympy import sympify
import numpy as np

#MÉTODO DA POSIÇÃO FALSA

#f - função objetivo
#a - extremo esquerdo do intervalo de inspeção 
#b - extremo direito do intervalo de inspeção 
#TOL - tolerância (critério de parada)
#N - número máximo de iterações

def posicaofalsa(f, a, b, TOL, N):

    if a>=b or TOL<=0:
        return ('Procedimento não se aplica a a>=b ou tolerancia negativa!')

    elif f(a)==0.0:
        return a
    
    elif f(b)==0.0:
        return b

    elif np.sign(f(a)) == np.sign(f(b)):             #possuem o mesmo sinal
        return ('Não possui raiz no intervalo!')
    
    else: 
        i = 1   

        while i <= N:

            p =(a*f(b) - b*f(a))/(f(b) - f(a))

            print('Iteracao - %d, p = %.10f, f(p) = %.10f' % (i, p, f(p)))

            #condicao de parada
            if abs(f(p)) <= TOL:
                return 'Raiz aproximada = %.10f' % p

            elif np.sign(f(a)) == np.sign(f(p)):    #possuem o mesmo sinal
                a = p

            else:
                b = p

            i += 1
        
        raise NameError('\nNum. max. de iter. excedido!')


def f(x):
    return np.e**(-x**2)-np.cos(x)
    ##return x**3-x-1
    ##return 4*np.sin(x)-np.e**x
    ##return x*np.log10(x)-1

a = float(input('Entre com o valor minimo: '))
b = float(input('Entre com o valor maximo: '))
TOL = float(input('Entre com a tolerancia: '))
N = int(input("Entre com o numero maximo de iteracoes: "))

print(posicaofalsa(f,a,b,TOL,N))