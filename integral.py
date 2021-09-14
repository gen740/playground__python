import sympy as sym
import numpy as np

x = sym.symbols('x')
y = sym.symbols('y')

f = (x + y) * sym.exp(-(x ** 2 + y ** 2) / 4)
A = sym.diff(f, x)
B = sym.diff(f, y)
S = sym.sqrt(1 + A ** 2 + B ** 2)
Sx = -A
Sy = -B
Sz = 1
Vx = x*A
Vy = -y*B
Vz = 1

print(A)
print(B)
print(S)
print(sym.integrate(S, (x, -4, 4),(y, -4, 4)).evalf())

print(sym.integrate(Sx, (x, -4, 4),(y, -4, 4)).evalf())
print(sym.integrate(Sy, (x, -4, 4),(y, -4, 4)).evalf())
print(sym.integrate(Sz, (x, -4, 4),(y, -4, 4)).evalf())

print(sym.integrate(Vx, (x, -4, 4),(y, -4, 4)).evalf())
print(sym.integrate(Vy, (x, -4, 4),(y, -4, 4)).evalf())
print(sym.integrate(Vz, (x, -4, 4),(y, -4, 4)).evalf())

