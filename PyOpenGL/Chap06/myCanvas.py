from tkinter import *
import math
import numpy as np


class MyCanvas(object):
    def __init__(self, width=600, height=600, xo=300, yo=300, r=2.0):
        self.w, self.h = (width, height)
        self.xo, self.yo = (xo, yo)
        self.r = r
        self.s = min(self.w, self.h) / self.r
        self.mr = 2
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.w, height=self.h)
        self.canvas.pack()

    def bind(self, event, func):
        self.canvas.bind(event, func)

    def mainloop(self):
        self.root.mainloop()

    def setOrigin(self, x, y):
        self.xo, self.yo = (x, y)

    def setRange(self, r):
        self.r = r
        self.s = min(self.w, self.h) / self.r

    def point(self, x, y):
        return np.array(((x - self.xo) / self.s, (self.yo - y) / self.s))

    def x(self, p):
        return self.s * p[0] + self.xo

    def y(self, p):
        return -self.s * p[1] + self.yo

    def inside(self, p):
        return 0 <= self.x(p) <= self.w and 0 <= self.y(p) <= self.h

    def clear(self):
        self.canvas.create_rectangle((2, 2), (self.w + 3, self.h + 3),
                                     outline='', fill='white')

    def drawCircle(self, c, r, fill='', outline='black'):
        dr = self.s * r
        xc, yc = (self.x(c), self.y(c))
        self.canvas.create_oval((xc - dr, yc - dr), (xc + dr + 1, yc + dr + 1),
                                fill=fill, outline=outline)

    def drawPolyline(self, ps, color='black'):
        points = []
        for i in range(len(ps)):
            points.append((self.x(ps[i]), self.y(ps[i])))
        self.canvas.create_line(tuple(points), fill=color)

    def drawPolygon(self, ps, fill='gray90', outline='black'):
        points = []
        for i in range(len(ps)):
            points.append((self.x(ps[i]), self.y(ps[i])))
        self.canvas.create_polygon(tuple(points), fill=fill, outline=outline)

    def drawMarker(self, p, fill='black', outline=''):
        x, y = (self.x(p), self.y(p))
        self.canvas.create_rectangle((x - self.mr, y - self.mr),
                                     (x + self.mr + 1, y + self.mr + 1),
                                     fill=fill, outline=outline)
