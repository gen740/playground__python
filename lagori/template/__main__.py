# pyrigt: strict
# This is main python file if you want to make library only please remove this file

import numpy as np


ro = 14

def Inertia_matrix(R: float, h: float):
    M: float = ro * np.pi * R ** 2 * h
    Ixx: float = 1/4 * M * R ** 2 + 1/12* M * h ** 2
    Iyy: float = 1/4 * M * R ** 2 + 1/12* M * h ** 2
    Izz: float = 1/2 * M * R ** 2
    return (Ixx, Iyy, Izz, M)

def main():
    lagoris = [(0.1, 0.2), (0.1375, 0.2), (0.175, 0.2), (0.2125, 0.2), (0.25, 0.2)]
    for i in lagoris:
        print(f'{Inertia_matrix(*i)}')


if __name__ == "__main__":
    main()
