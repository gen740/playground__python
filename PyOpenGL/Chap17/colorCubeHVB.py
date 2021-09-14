from OpenGL.GL import *
import math
from myTranslateCanvas import MyTranslateCanvas
from colorsys import hsv_to_rgb

class ColorCube(object):
    def __init__(self):
        NOP = 100
        self.circle = []
        self.color = []
        for i in range(NOP + 1):
            t = 2 * math.pi * i / NOP
            self.color.append(i / (NOP + 1))
            self.circle.append((math.sin(t), 1, math.cos(t)))

    def display(self):
        glBegin(GL_POLYGON)
        glColor3dv(hsv_to_rgb(1, 1, 0))
        glVertex((0,-1,0))
        for i in range(len(self.circle)):
            glColor3dv(hsv_to_rgb(self.color[len(self.circle) - i - 1], 1, 1))
            glVertex3dv(self.circle[len(self.circle) - i - 1])
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glColor3dv(hsv_to_rgb(0.5, 1, 1))
        glVertex((0,1,0))
        for i in range(len(self.circle)):
            glColor3dv(hsv_to_rgb(self.color[i], 1, 1))
            glVertex3dv(self.circle[i])
        glEnd()


def main():
    canvas = MyTranslateCanvas()
    dispObj = ColorCube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == '__main__':
    main()
