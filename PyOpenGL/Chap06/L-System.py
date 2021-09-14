import math
from vectorMatrix import rotMatrix, scaleMatrix
import numpy as np
from myCanvas import MyCanvas
from fractal import Fractal


class Koch(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((0, 1))]
        mats = []
        mats.append(
            scaleMatrix(2 / 3).dot(rotMatrix(3/5)))
        mats.append(
            scaleMatrix(2 / 3).dot(rotMatrix(-3/5)))
        vecs = [base[1]]
        vecs.append(base[1])
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolyline(pnts)


def main():
    canvas = MyCanvas(xo=300, yo=600, r=3.3)
    Koch(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
