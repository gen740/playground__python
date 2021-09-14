import math  # math モジュールの import
from OpenGL.GL import *  # GL モジュールの import
from myRotateCanvas import MyRotateCanvas  # myRotateCanvas モジュールの import
from wireCube import WireCube
from cube import Cube


class HiddenCube(WireCube):
    def __init__(self):
        super().__init__()

    def display(self):
        self.displayEdges()
        glColor3dv((0, 0, 0))
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1, 1)
        for i in self.faces:
            glBegin(GL_POLYGON)
            for j in i:
                glVertex3dv(self.vertices[j])
            glEnd()


def main():
    canvas = MyRotateCanvas()
    dispObj = HiddenCube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
