from tabulate import tabulate
import math
import sys

def euler():
    pass

def rungekutta2(f, x, xn, y, h):

    k1 = f(x, y)
    k2 = f(x, y + h*k1)

    print()

    x = x + h
    y = y + h/2 * (k1 + k2)

def rungekutta4(f, x, xn, y, h):
    h = 0.1

    k1 = f(x, y)
    k2 = f(x + (h/2), y + h/2 * k1)
    k3 = f(x + (h/2), y + h/2 * k2)
    k4 = f(x + h, y + h * k3)

    print()

    x = x + h
    y = y + (h/6) * (k1 + (2*k2) + (2*k3) + k4)

if __name__ == '__main__' and len(sys.argv) == 3:
    algs = {
        'e': euler,
        'rk2': rungekutta2,
        'rk4': rungekutta4
    }

    alg_func = algs[sys.argv[1]]

    with open(sys.argv[2], 'r') as f:
        equation = f.readline()
        values = f.readline().split(',')

        for i, value in enumerate(values):
            values[i] = float(value)

    def f(x, y=None):
        return eval(equation)

    alg_func(f, values[0], values[1], values[2], values[3])
else:
    print('''
Como usar:
python av2.py [sigla do algoritmo] [nome do arquivo de texto de entrada]

Ex. comando:
python av2.py rk2 input.txt

Algorítmos suportados e suas siglas:
- Método de Euler (e)
- Método de Runge Kutta de 2ª ordem (rk2)
- Método de Runge Kutta de 4ª ordem (rk4)

Os arquivos de texto devem ter a seguinte estrutura:
Linha 1: Equação (com sintaxe do python)
Linha 2: X inicial, X final, Y inicial e H (separados por virgula)
(H = o intervalo entre cada valor de X)

Ex. input.txt:
2x - 3
0, 4, 1, 0.1''')
