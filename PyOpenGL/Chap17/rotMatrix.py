import numpy as np
import math


class RotMatrix(object):
    def __init__(self, mat):
        self.mat = np.array(mat)

    def multiply(self, o):
        return RotMatrix(self.mat.dot(o.mat))

    def setMatrix(self, offset):
        return (self.mat[0, 0], self.mat[1, 0], self.mat[2, 0], 0,
                self.mat[0, 1], self.mat[1, 1], self.mat[2, 1], 0,
                self.mat[0, 2], self.mat[1, 2], self.mat[2, 2], 0,
                offset[0], offset[1], offset[2], 1)

    def rotAroundAxis(self, angle, x, y, z):
        d = (x * x + y * y + z * z)**0.5
        if d == 0:
            return self.multiply(RotMatrix.identity())
        else:
            x, y, z = (x / d, y / d, z / d)
            angle = angle * math.pi / 180
            sin, cos = (math.sin(angle), math.cos(angle))
            return self.multiply(RotMatrix(
                ((cos + x * x * (1 - cos), x * y * (1 - cos) - z * sin, x * z * (1 - cos) + y * sin),
                 (x * y * (1 - cos) + z * sin, cos + y *
                  y * (1 - cos), y * z * (1 - cos) - x * sin),
                    (x * z * (1 - cos) - y * sin, y * z * (1 - cos) + x * sin, cos + z * z * (1 - cos)))))

    @classmethod
    def identity(cls):
        return RotMatrix(((1, 0, 0), (0, 1, 0), (0, 0, 1)))


def main():
    test_data = [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]]
    r = RotMatrix(test_data)
    print(r.setMatrix([10, 10, 10]))
    print(r.rotAroundAxis(90, 1, 0, 0).mat)
    print(r.rotAroundAxis(90, 0, 1, 0).mat)
    print(r.rotAroundAxis(90, 0, 0, 1).mat)
    print(r.rotAroundAxis(90, 1, 1, 1).mat)


if __name__ == "__main__":
    main()
