import numpy as np
from myGLCanvas import MyGLCanvas
from fractal2 import Fractal, getArgs
from Tetra import Tetra


class Sierpinski(Fractal):
    def __init__(self, times):
        cube = Tetra()
        nv = len(cube.vertices)
        SCL = 1 / 2
        vecs = []
        for i in range(nv):
            vecs.append(np.array(cube.vertices[i]) * (1 - SCL))
        super().__init__(cube, SCL, vecs, times)


def main():
    times, args = getArgs()
    canvas = MyGLCanvas()
    dispObj = Sierpinski(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()


if __name__ == '__main__':
    main()
