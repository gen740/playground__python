import math
from vectorMatrix import rotMatrix, scaleMatrix
import numpy as np
from myCanvas import MyCanvas
from fractal import Fractal


class Koch(Fractal):
    def __init__(self, canvas):
        base = [np.array((0, 0)), np.array((1, 0))]
        mats = [(scaleMatrix(1 / np.sqrt(2.))).dot(rotMatrix(math.pi / 4))]
        mats.append(
            scaleMatrix(1 / np.sqrt(2.)).dot(rotMatrix(3 * math.pi / 4)))
        vecs = [0 * base[0]]
        vecs.append(base[1])
        super().__init__(canvas, base, mats, vecs)

    def drawObject(self, pnts):
        self.canvas.drawPolyline(pnts)


def main():
    canvas = MyCanvas(xo=160, yo=340, r=1.7)
    Koch(canvas).drawFractal()
    canvas.mainloop()


if __name__ == '__main__':
    main()
