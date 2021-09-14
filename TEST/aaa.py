import sympy as sym
from scipy import integrate
import numpy as np

sym.init_printing()

x = sym.symbols('x')
y = sym.symbols('y')

u11 = sym.cos(x) * sym.sin(y)
u12 = sym.sin(x) * sym.sin(y)
u13 = -2 + sym.cos(y)
u1 = [0, 2 * np.pi]
v1 = [0, np.pi / 2]
a1 = sym.Matrix([u11, u12, u13])

u21 = sym.cos(x)
u22 = sym.sin(x)
u23 = y
u2 = [0, 2 * np.pi]
v2 = [-2, 2]
a2 = sym.Matrix([u21, u22, u23])

u31 = y * sym.cos(x)
u32 = y * sym.sin(x)
u33 = 2
u3 = [0, 2 * np.pi]
v3 = [0, 1]
a3 = sym.Matrix([u31, u32, u33])

# A = sym.Matrix([
#     u13,
#     3*u11 + u13,
#     u12])

A1 = sym.Matrix([
    u11,
    u12,
    u13
])
A1 = A1 / (4 * np.pi * (u11 ** 2 + u12 ** 2 + u13 ** 2)**(3 / 2))

A2 = sym.Matrix([
    u21,
    u22,
    u23
])
A2 = A2 / (4 * np.pi * (u21 ** 2 + u22 ** 2 + u23 ** 2)**(3 / 2))

A3 = sym.Matrix([
    u31,
    u32,
    u33
])
A3 = A3 / (4 * np.pi * (u31 ** 2 + u32 ** 2 + u33 ** 2)**(3 / 2))


U11 = a1.diff(x)
U12 = a1.diff(y)
U21 = a2.diff(x)
U22 = a2.diff(y)
U31 = a3.diff(x)
U32 = a3.diff(y)

AdS1 = A1.dot(U11.cross(U12))
AdS2 = A2.dot(U21.cross(U22))
AdS3 = A3.dot(U31.cross(U32))


def f1(a, b):
    return AdS1.evalf(subs={x: a, y: b})


def f2(a, b):
    return AdS2.evalf(subs={x: a, y: b})


def f3(a, b):
    return AdS3.evalf(subs={x: a, y: b})


val1, _ = integrate.dblquad(f1, u1[0], u1[1], v1[0], v1[1])
val2, _ = integrate.dblquad(f2, u2[0], u2[1], v2[0], v2[1])
val3, _ = integrate.dblquad(f3, u3[0], u3[1], v3[0], v3[1])

print(val1)
print(val2)
print(val3)
print(-val1 + val2 + val3)
