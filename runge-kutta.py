import time

def rk4(x, y, n):
    def f(x, y):
        return x + y + 2

    x = 0
    y = 2
    h = 0.1

    while(True):
        k1 = f(x, y)
        k2 = f(x + (h/2), y + h/2 * k1)
        k3 = f(x + (h/2), y + h/2 * k2)
        k4 = f(x + h, y + h * k3)

        print('x', x, sep=' = ')
        print('y', y, sep=' = ')
        print('k1', k1, sep=' = ')
        print('k2', k2, sep=' = ')
        print('k3', k3, sep=' = ')
        print('k4', k4, sep=' = ')
        print()

        x = x + h
        y = y + (h/6) * (k1 + (2*k2) + (2*k3) + k4)

        time.sleep(1)
        i += 1

def rk2(x, y, n):
    def f(x, y):
        return x + y + 2

    x = 0
    y = 2
    h = 0.1

    while(True):
        k1 = f(x, y)
        k2 = f(x, y + h*k1)

        print('x', x, sep=' = ')
        print('y', y, sep=' = ')
        print('k1', k1, sep=' = ')
        print('k2', k2, sep=' = ')
        print()

        x = x + h
        y = y + h/2 * (k1 + k2)

        time.sleep(1)
        i += 1
