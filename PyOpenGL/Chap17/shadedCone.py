import numpy as np
import math
from OpenGL.GL import *
from myShadeCanvas import MyShadeCanvas


class ShadedPolyhedron(object):
    def __init__(self, diffuse=(), specular=(), shininess=0):
        self.diffuse, self.specular, self.shininess = \
            (diffuse, specular, shininess)
        NOP = 100
        self.circle = []
        self.top = (0, 1, 0)
        for i in range(NOP + 1):
            t = 2 * math.pi * i / NOP
            self.circle.append((math.sin(t), -1, math.cos(t)))

    def display(self):
        self.material()
        for i in range(len(self.circle)):
            glShadeModel(GL_SMOOTH)
            glBegin(GL_POLYGON)
            glNormal3dv(normal(self.top, self.circle[i-2], self.circle[i-1]))
            glVertex3dv(self.top)
            glNormal3dv(normal(self.top, self.circle[i-3], self.circle[i-1]))
            glVertex3dv(self.circle[i-2])
            glNormal3dv(normal(self.top, self.circle[i-2], self.circle[i]))
            glVertex3dv(self.circle[i-1])
            glEnd()
        glShadeModel(GL_SMOOTH)
        glBegin(GL_POLYGON)
        glNormal3dv((0, -1, 0))
        for i in range(len(self.circle)):
            glVertex3dv(self.circle[len(self.circle) - i - 1])
        glEnd()

    def material(self):
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.specular)
        glMaterialf(GL_FRONT, GL_SHININESS, self.shininess)


def normal(p0, p1, p2):
    p0, p1, p2 = (np.array(p0), np.array(p1), np.array(p2))
    return tuple(np.cross(p1 - p0, p2 - p0))


class ShadedCube(ShadedPolyhedron):
    def __init__(self):
        super().__init__(
            (0.8, 0.8, 0.2, 1.0),
            (0.9, 0.9, 0.9, 1.0),
            100)


def main():
    canvas = MyShadeCanvas()
    dispObj = ShadedCube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
