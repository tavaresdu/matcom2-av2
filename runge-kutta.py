from tabulate import tabulate
import time
import csv

algs = {
    'euler': euler,
    'runge-kutta-2': rk2,
    'runge-kutta-4': rk4
}

def func(x,y):
    pass

def euler():
    pass

def rk4(f, x, y, h):
    h = 0.1

    k1 = f(x, y)
    k2 = f(x + (h/2), y + h/2 * k1)
    k3 = f(x + (h/2), y + h/2 * k2)
    k4 = f(x + h, y + h * k3)

    print()

    x = x + h
    y = y + (h/6) * (k1 + (2*k2) + (2*k3) + k4)

def rk2(f, x, y, h)):

    k1 = f(x, y)
    k2 = f(x, y + h*k1)

    print()

    x = x + h
    y = y + h/2 * (k1 + k2)
