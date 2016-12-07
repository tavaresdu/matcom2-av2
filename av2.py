from sympy import Symbol, integrate, lambdify
from tabulate import tabulate
from math import *
import sys

def print_table(header, rows):
    print(tabulate(rows, headers=header, tablefmt='grid'))

def euler(fd, f, x, xn, y, h, err):
    header = ['X', 'Y Real', 'Y', 'Erro']
    rows = list()

    while round(xn, err) >= round(x, err):
        yo = f(x, 0)
        g_err = ((yo - y) / yo) * 100

        rows.append([round(x, err), round(yo, err),
            round(y, err), round(g_err, err)])

        y = y + h * fd(x)
        x = x + h


    print_table(header, rows)

def rungekutta2(fd, f, x, xn, y, h, err):
    header = ['X', 'Y Real', 'Y (Heun)', 'Y (Ponto Médio)', 'Y (Ralston)',
        'K1', 'K2 (Heun)', 'K2 (Ponto Médio)', 'K2 (Ralston)', 'Erro (Heun)',
        'Erro (Ponto Médio)', 'Erro (Ralston)']
    rows = list()

    yh = y
    ym = y
    yr = y

    while round(xn, err) >= round(x, err):
        k1 = fd(x, 0)
        k2h = fd(x + h, y + k1*h)
        k2m = fd(x + h/2, y + k1*(h/2))
        k2r = fd(x + 3*h/4, y + k1*(3*h/4))
        yo = f(x, y)
        g_err_h = ((yo - yh) / yo) * 100
        g_err_m = ((yo - ym) / yo) * 100
        g_err_r = ((yo - yr) / yo) * 100

        rows.append([round(x, err), round(yo, err), round(yh, err),
            round(ym, err), round(yr, err), round(k1, err), round(k2h, err),
            round(k2m, err), round(k2r, err), round(g_err_h, err),
            round(g_err_m, err), round(g_err_r, err)])

        x = x + h
        yh = yh + (k1/2 + k2h/2) * h
        ym = ym + k2m * h
        yr = yr + (k1/3 + 2*k2r/3) * h

    print_table(header, rows)

def rungekutta4(fd, f, x, xn, y, h, err):
    header = ['X', 'Y Real', 'Y', 'K1', 'K2', 'K3', 'K4', 'Erro']
    rows = list()

    while round(xn, err) >= round(x, err):
        k1 = fd(x, 0)
        k2 = fd(x + (h/2), y + h/2 * k1)
        k3 = fd(x + (h/2), y + h/2 * k2)
        k4 = fd(x + h, y + h * k3)
        yo = f(x, 0)
        g_err = ((yo - y) / yo) * 100

        rows.append([round(x, err), round(yo, err), round(y, err),
            round(k1, err), round(k2, err), round(k3, err),
            round(k4, err), round(g_err, err)])

        x = x + h
        y = y + (h/6) * (k1 + (2*k2) + (2*k3) + k4)

    print_table(header, rows)

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

    icogx = Symbol('x')
    icogy = Symbol('y')
    integral = integrate(equation, icogx)
    f = lambdify((icogx, icogy), integral)
    result = float(f(values[0], 0))
    diff = values[2] - result
    fl = lambda x, y: f(x, y) + diff

    def fd(x, y=None):
        return eval(equation)

    alg_func(fd, fl, values[0], values[1], values[2], values[3], 4)
else:
    print('''\
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
-2*x**3 + 12*x**2 - 20*x + 8.5
0, 4, 1, 0.5''')
