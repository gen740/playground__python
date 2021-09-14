import sympy as sym
import numpy as np

a = sym.symbols('a')
b = sym.symbols('b')
c = sym.symbols('c')
d = sym.symbols('d')

A = (1 - a ** 2 - b ** 2) * (1 -  c ** 2 - d ** 2)
B = (1 - a * c  - b * d) ** 2
C = (A - B).expand()
print(C.factor())
