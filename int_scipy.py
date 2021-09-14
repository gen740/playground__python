from scipy import integrate
import numpy as np


def A(x, y):
    return -x * (x + y) * np.exp(-x**2 / 4 - y**2 / 4) / \
        2 + np.exp(-x**2 / 4 - y**2 / 4)


def B(x, y):
    return -y * (x + y) * np.exp(-x**2 / 4 - y**2 / 4) / \
        2 + np.exp(-x**2 / 4 - y**2 / 4)


def z(x, y):
    return (x + y) * np.exp(-(x**2 + y**2) / 4)


def f(x, y):
    return (1 + A(x, y) ** 2 + B(x, y) ** 2) ** (1 / 2)


def J(x, y):
    return (x**2 + y**2 + z(x, y) ** 2) * \
        ((1 + A(x, y) ** 2 + B(x, y) ** 2)) ** (1 / 2)


def Sx(x, y):
    return -A(x, y)


def Sy(x, y):
    return -B(x, y)


def Sz(x, y):
    return 1


def Vx(x, y):
    return -x * A(x, y)


def Vy(x, y):
    return -y * B(x, y)


def Vz(x, y):
    return z(x, y)


def n1(x, y):
    return x * Sx(x, y) / f(x, y)


def n2(x, y):
    return -y * Sy(x, y) / f(x, y)


def n3(x, y):
    return 1 * Sz(x, y) / f(x, y)


def n(x, y):
    return (n1(x, y) + n2(x, y) + n3(x, y)) * f(x, y)

val, _ = integrate.dblquad(f, -4, 4, -4, 4)
val2, _ = integrate.dblquad(J, -4, 4, -4, 4)
val3, _ = integrate.dblquad(Sx, -4, 4, -4, 4)
val4, _ = integrate.dblquad(Sy, -4, 4, -4, 4)
val5, _ = integrate.dblquad(Sz, -4, 4, -4, 4)
val6, _ = integrate.dblquad(Vx, -4, 4, -4, 4)
val7, _ = integrate.dblquad(Vy, -4, 4, -4, 4)
val8, _ = integrate.dblquad(Vz, -4, 4, -4, 4)
val9, _ = integrate.dblquad(n, -4, 4, -4, 4)

print('S', val)
print('J', val2)
print('Sx', val3)
print('Sy', val4)
print('Sz', val5)
print('Vx', val6)
print('Vy', val7)
print('Vz', val8)
print('S', val9)
print('T', val3 ** 2 + val4 ** 2 + val5 ** 2 - val ** 2)
