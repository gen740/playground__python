import math
import numpy as np


def norm(v):
    """ベクトルの大きさを返す
    """
    v = np.array(v)
    return (v.dot(v))**0.5


def rotMatrix(t):
    """回転行列
    """
    return np.array(((math.cos(t), -math.sin(t)), (math.sin(t), math.cos(t))))


def scaleMatrix(s):
    """拡大縮小の行列
    """
    return np.array(((s, 0), (0, s)))


def main():
    vec1 = np.array((1, 1))
    vec2 = np.array((3, 4))
    rot = rotMatrix(math.pi / 2.)
    inv = rotMatrix(-math.pi / 2.)
    scl = scaleMatrix(2.)
    print('|', vec2, '| =', norm(vec2))
    print(vec1, '+', vec2, '=', vec1 + vec2)
    print(vec1, '-', vec2, '=', vec1 - vec2)
    print(vec1, '* 2 =', vec1 * 2)
    print(vec1, '*', vec2, '=', vec1 * vec2)
    print(vec1, '.', vec2, '=', vec1.dot(vec2))
    print('rotate (', vec2, ') =', rot.dot(vec2))
    print('scale&rot(', vec2, ') =', scl.dot(rot).dot(vec2))
    print('inv&rot (', vec2, ') =', inv.dot(rot).dot(vec2))
    print(vec1, '/', vec2, '=', vec1 / vec2)


if __name__ == "__main__":
    main()
