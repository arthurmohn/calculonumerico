from sympy import sympify
import numpy as np

#METODO DA BISSECÇÃO 

#f - função objetivo
#a - extremo esquerdo do intervalo de inspeção 
#b - extremo direito do intervalo de inspeção 
#TOL - tolerância (critério de parada)
#N - número máximo de iterações

def bisseccao(f, a, b, TOL, N):
    i = 1
    fa = f(a)

    if a>=b or TOL<=0:
        return ('Procedimento não se aplica a a>=b ou precisao negativa!')

    elif f(a)==0.0:
        return a
    
    elif f(b)==0.0:
        return b

    elif f(a) * f(b) > 0:          #possuem o mesmo sinal
        return ('Não possui raiz no intervalo!')
    
    else: 
        while (i <= N):
            #iteracao da bissecaop
            p = a + (b-a)/2
            fp = f(p)
            print('Iteracao - %d, p = %.10f, f(x) = %.10f' % (i, p, f(p)))

            #condicao de parada
            if ((fp == 0) or ((b-a)/2 < TOL)):
                return ('Raiz aproximada = %.10f' % p)

            #bissecta o intervalo
            i += 1
            if (fa * fp > 0):       #possuem o mesmo sinal
                a = p
                fa = fp
            else:
                b = p
    
        raise NameError('\nNum. max. de iter. excedido!')


#funcao = input('\nEntre com sua funcao: ')
#func = sympify(funcao)
#f = lambda x:func.subs({'x':x})

def f(x):
    return np.e**(-x**2)-np.cos(x)
    ##return x**3-x-1
    ##return 4*np.sin(x)-np.e**x
    ##return x*np.log10(x)-1

a = float(input('Entre com o valor minimo: '))
b = float(input('Entre com o valor maximo: '))
TOL = float(input('Entre com a tolerancia: '))
N = int(input("Entre com o numero maximo de iteracoes: "))

print(bisseccao(f,a,b,TOL,N))