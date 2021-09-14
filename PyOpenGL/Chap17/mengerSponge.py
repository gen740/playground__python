import numpy as np
from myShadeCanvas import MyShadeCanvas
from fractal import Fractal, getArgs
from shadedCube import ShadedCube


class MengerSponge(Fractal):
    def __init__(self, times):
        cube = ShadedCube()
        edges = ((0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 5),
             (2, 6), (3, 7), (4, 5), (5, 6), (6, 7), (7, 4))
        nv = len(cube.vertices)
        ne = len(edges)
        SCL = 1 / 3
        vecs = []
        for i in range(nv):
            vecs.append(np.array(cube.vertices[i]) * (1 - SCL))
        for i in range(ne):
            mid = (np.array(cube.vertices[edges[i][0]]) +
                   np.array(cube.vertices[edges[i][1]])) / 2
            vecs.append(mid * (1 - SCL))
        super().__init__(cube, SCL, vecs, times)


def main():
    times, args = getArgs()
    canvas = MyShadeCanvas()
    dispObj = MengerSponge(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()


if __name__ == '__main__':
    main()
