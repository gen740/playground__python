import numpy as np
import sys
import math
from myCanvas import MyCanvas


def circle(cen=(0, 0), r=0.8):
    if len(sys.argv) > 1:
        num = sys.argv[1]
    else:
        num = input('# of points -> ')
    n = int(num)
    p = []
    for i in range(n):
        t = 2 * math.pi * i / n
        p.append(np.array(
                (r * math.cos(t) + cen[0],
                    r * math.sin(t) + cen[1])))
    return tuple(p)


def display(canvas, points):
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            print(i, j)
            canvas.drawPolyline([points[i], points[j]])


def main():
    canvas = MyCanvas()
    points = circle()
    display(canvas, points)
    canvas.mainloop()


if __name__ == '__main__':
    main()
