from scipy import integrate
import numpy as np


def f1(x, y):
    return (
        (np.sin(x)**2 * np.sin(y) * np.cos(y) + np.sin(y) * np.cos(x)**2 * np.cos(y)) * np.sin(x) * np.cos(y) +
        (np.sin(y) - 2) * np.cos(x) * np.cos(y)**2 +
        (np.sin(y) + 3 * np.cos(x) * np.cos(y) - 2) * np.sin(x) * np.cos(y)**2
    )


def f2(x, y):
    return (
        y * np.cos(x) + (y + 3 * np.cos(x)) * np.sin(x)
    )


def f3(x, y):
    return (
        (-y * np.sin(x)**2 - y * np.cos(x)**2) * np.sin(x)
    )


def g1(x, y):
    return (
        (np.sin(x)**2 * np.sin(y) * np.cos(y) + np.sin(y)
         * np.cos(x)**2 * np.cos(y)) * (np.sin(y) - 2)
        / (4 * np.pi * ((np.sin(y) - 2)**2 +
                        np.sin(x)**2 * np.cos(y)**2 + np.cos(x)**2 * np.cos(y)**2)**(3 / 2)) +
        np.sin(x)**2 * np.cos(y)**3
        / (4 * np.pi * ((np.sin(y) - 2)**2 +
                        np.sin(x)**2 * np.cos(y)**2 + np.cos(x)**2 * np.cos(y)**2)**(3 / 2)) +
        np.cos(x)**2 * np.cos(y)**3
        / (4 * np.pi * ((np.sin(y) - 2)**2 + np.sin(x) **
                        2 * np.cos(y)**2 + np.cos(x)**2 * np.cos(y)**2)**(3 / 2))
    )


def g2(x, y):
    return (
        np.sin(x)**2 * np.cos(y)
        / (4 * np.pi * ((np.sin(y) - 2)**2 +
                        np.sin(x)**2 * np.cos(y)**2 + np.cos(x)**2 * np.cos(y)**2)**(3 / 2)) +
        np.cos(x)**2 * np.cos(y)
        / (4 * np.pi * ((np.sin(y) - 2)**2 +
                        np.sin(x)**2 * np.cos(y)**2 + np.cos(x)**2 * np.cos(y)**2)**(3 / 2))
    )


def g3(x, y):
    return (
        (-y * np.sin(x)**2 - y * np.cos(x)**2) * (np.sin(y) - 2)
        / (4 * np.pi *
           ((np.sin(y) - 2)**2 + np.sin(x)**2 * np.cos(y)**2 + np.cos(x)**2 * np.cos(y)**2)**(3 / 2))
    )


# def f(x, y):
#     return ((np.sin(x)**2 * np.sin(y) * np.cos(y) + np.sin(y) * np.cos(x)**2 * np.cos(y)) * (np.sin(y) - 2) /
#             (4 * np.pi * (np.sin(x)**2 * np.cos(y)**2 + 2 * np.sin(y) + np.cos(x)**2 * np.cos(y)**2 - 4)**(3 / 2)) + np.sin(x)**2 * np.cos(y)**3 /
#             (4 * np.pi * (np.sin(x)**2 * np.cos(y)**2 + 2 * np.sin(y) + np.cos(x)**2 * np.cos(y)**2 - 4)**(3 / 2)) + np.cos(x)**2 *
#             np.cos(y)**3 / (4 * np.pi * (np.sin(x)**2 * np.cos(y)**2 + 2 *
# np.sin(y) + np.cos(x)**2 * np.cos(y)**2 - 4)**(3 / 2)))
val1, _ = integrate.dblquad(f1, 0, 2 * np.pi, 0, np.pi / 2)
val2, _ = integrate.dblquad(f2, 0, 2 * np.pi, -2, 2)
val3, _ = integrate.dblquad(f3, 0, 2 * np.pi, 0, 1)

# val4, _ = integrate.dblquad(g1, 0, 2 * np.pi, 0, np.pi / 2)
# val5, _ = integrate.dblquad(g2, 0, 2 * np.pi, -2, 2)
# val6, _ = integrate.dblquad(g3, 0, 2 * np.pi, 0, 1)

val4, _ = integrate.dblquad(g1, 0, 2 * np.pi, 0, np.pi / 2)
val5, _ = integrate.dblquad(g2, 0, 2 * np.pi, -2, 2)
val6, _ = integrate.dblquad(g3, 0, 2 * np.pi, 0, 1)

print('S', val1)
print('S', val2)
print('S', val3)
print(f'Sum = {val2 + val3}')

print('S', val4)
print('S', val5)
print('S', val6)
print(f'Sum = {- val4 + val5 + val6}')
print(1 / np.pi)
