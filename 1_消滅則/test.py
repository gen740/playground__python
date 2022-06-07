import numpy as np


def Fcc(h, k, l):
    return 1 + np.exp(np.pi * 1j * (h + k)) + np.exp(np.pi * 1j * (k + l)) + np.exp(np.pi * 1j * (h + l))


def Fcc2(h, k, l):
    return np.exp(np.pi * 1j * (h + k + l)) + np.exp(np.pi * 1j * h) + np.exp(np.pi * 1j * k) + np.exp(np.pi * 1j * l)


def FCardon(h, k, l):
    return Fcc(h, k, l) * (1 + np.exp(np.pi / 2 * 1j * (h + k + l)))


def main():
    for i in range(4):
        for j in range(4):
            for k in range(4):
                print(f"{i=}, {j=}, {k=}",
                      round(Fcc(i, j, k), 3),
                      round(Fcc2(i, j, k), 3))


if __name__ == "__main__":
    main()
    # print(1j * 1j)
