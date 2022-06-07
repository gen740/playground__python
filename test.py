import numpy as np
import matplotlib.pyplot as plt

r = 75

fig, ax = plt.subplots()


def calc_d(theta, x, y):
    phi = np.arctan2(x, y)
    psi = theta - phi
    print(phi, psi)
    r2 = x**2 + y**2
    dist = np.abs(np.sin(theta) * x - np.cos(theta))
    if (np.abs(dist) > r):
        return 1200
    return np.sqrt(r2) * np.cos(psi) - np.sqrt(r2 * (np.cos(psi) ** 2 - 1) + r**2)


def calc_d_theta(a, /):
    theta_data = np.linspace(-np.pi / 2, np.pi/2, 721)
    d = []
    for i in theta_data:
        d.append([calc_d(i, a[0], a[1]), i])
    return d


def calc_data(a, /):
    result = []
    for n, i in enumerate(a):
        data = calc_d_theta(i)
        for m, j in enumerate(data):
            result.append([j[0], j[1], n * 25 + m / 720 * 25])


def main():
    data = []
    for i in range(0, 1):
        data.append([1000 + i, 1000 + i])
    data = calc_data(data)


if __name__ == "__main__":
    main()
