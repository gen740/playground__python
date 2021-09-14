from sympy import *

x = symbols('x')
u = symbols('u')
v = symbols('v')
S = (-sin(u)**2*sin(v)*cos(v) - sin(v)*cos(u)**2*cos(v))*sin(u)*cos(v) - (sin(v) - 2)*cos(u)*cos(v)**2 - (sin(v) + 3*cos(u)*cos(v) - 2)*sin(u)*cos(v)**2
S1 = v*sin(u) + (v + 3*sin(u))*cos(u)
S2 = (-sin(u)**2*sin(v)*cos(v) - sin(v)*cos(u)**2*cos(v))*sin(u)*cos(v) - (sin(v) - 2)*cos(u)*cos(v)**2 - (sin(v) + 3*cos(u)*cos(v) - 2)*sin(u)*cos(v)**2
print(integrate(S, (u, 0, 2 * pi), (v, 0, pi / 2)))
print(integrate(S1, (u, 0, 2 * pi), (v, -2, 2)))
print(integrate(S2, (u, 0, 2 * pi), (v, 0, pi / 2)))
