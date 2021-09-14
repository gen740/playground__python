import numpy as np
from scipy import integrate

a = 2
h = 0.623
w = 1.107

def F(x, y):
    return a / (x**2 + y**2 + a**2) ** (3 / 2)


# U1 = r.diff(x)
# U2 = a.diff(y)
# print(a.diff(x))
# print(a.diff(y))
# print(f'cross = {a.diff(x).cross(a.diff(y))}')

val1, err = integrate.dblquad(F, -h/2, h/2, -w/2, w/2)

print(val1)
