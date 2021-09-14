import math
from OpenGL.GL import *
from myRotateCanvas import MyRotateCanvas
from cube import Cube


class WireCube(Cube):
    def __init__(self):
        super().__init__()
        self.apex = (0, 1, 0)

    def display(self):
        self.displayEdges()

    def displayEdges(self):
        glColor3dv((1, 1, 0))
        glBegin(GL_LINES)
        for i in self.edges:
            glVertex3dv(self.vertices[i[0]])
            glVertex3dv(self.vertices[i[1]])
        glEnd()


def main():
    canvas = MyRotateCanvas()
    dispObj = WireCube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
