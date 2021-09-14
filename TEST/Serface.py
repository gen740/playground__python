from sympy import symbols, pi, sin, cos, Matrix, sqrt
import sympy as sym
from scipy import integrate

u = symbols('u')
v = symbols('v')


def S(X, U, V):
    x = X[0]
    y = X[1]
    z = X[2]
    A = Matrix([
        z,
        3 * x + z,
        y
    ])
    # A = Matrix([
    #     x / (4 * pi * (x**2 + y**2 + z**2)**(3 / 2)),
    #     y / (4 * pi * (x**2 + y**2 + z**2)**(3 / 2)),
    #     z / (4 * pi * (x**2 + y**2 + z**2)**(3 / 2))
    # ])
    F = Matrix([x, y, z])
    dFdU = F.diff(u)
    dFdV = F.diff(v)
    Cls = dFdV.cross(dFdU)
    S = A.dot(Cls)
    val1 = 0
    err = 0
    print(U[0], U[1], V[0], V[1])
    # print(sym.integrate(S, (u, U[0], U[1]), (v, V[0], V[1])))
    val1, err = integrate.dblquad(lambda a, b: S.evalf(
        subs={u: a, v: b}), U[0], U[1], V[0], V[1])
    print(f'\
        F             = {F}\n\
        A             = {A}\n\
        dF/dU         = {dFdU}\n\
        dF/dV         = {dFdV}\n\
        dF/dU x dF/dV = {Cls}\n\
        A.dS          = {S} dudv\n\
        val1          = {val1}\n\
        err           = {err}\n')
    return val1


def main():
    X1 = [
        cos(u) * sin(v),
        sin(u) * sin(v),
        cos(v)
    ]
    U1 = [0, 2 * pi]
    V1 = [0, pi / 2]

    X2 = [
        sin(u),
        cos(u),
        v
    ]
    U2 = [0, 2 * pi]
    V2 = [-2, 2]

    X3 = [
        v * cos(u),
        v * sin(u),
        2
    ]
    U3 = [0, 2 * pi]
    V3 = [0, 1]

#     X1 = [
#         u,
#         v,
#         -2 + sqrt(1 - u**2 - v**2)
#     ]
#     U1 = [-1, 1]
#     V1 = [-sqrt(1 - u**2), sqrt(1 - u**2)]

#     X2 = [
#         sin(u),
#         cos(u),
#         v
#     ]
#     U2 = [0, 2 * pi]
#     V2 = [-2, 2]

#     X3 = [
#         v * cos(u),
#         v * sin(u),
#         2
#     ]
#     U3 = [0, 2 * pi]
#     V3 = [0, 1]

    # print(S(X1, U1, V1))
    print('result = ',
          - S(X1, U1, V1)
          + S(X2, U2, V2)
          + S(X3, U3, V3)
          )


if __name__ == "__main__":
    main()
