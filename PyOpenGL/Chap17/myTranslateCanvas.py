from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from mySpinCanvas import MySpinCanvas
from quaternion import Quaternion
from rotMatrix import RotMatrix


class MyTranslateCanvas(MySpinCanvas):
    def __init__(self):
        super().__init__()
        self.ident = Quaternion.identity()
        # self.ident = RotMatrix.identity()

    def motion(self, x, y):
        deltaX, deltaY = (x - self.x, y - self.y)
        TRANSRATIO = 5
        if self.buttondown == GLUT_LEFT_BUTTON:
            SPINRATIO = 50
            self.angle = (deltaX**2 + deltaY**2)**0.5 * SPINRATIO / \
                min(self.width, self.height)
            modelMatrix = glGetDoublev(GL_MODELVIEW_MATRIX)
            projMatrix = glGetDoublev(GL_PROJECTION_MATRIX)
            viewport = glGetIntegerv(GL_VIEWPORT)
            originX, originY, originZ = \
                gluProject(0, 0, 0, modelMatrix, projMatrix, viewport)
            self.axisX, self.axisY, self.axisZ = \
                gluUnProject(originX + deltaY, originY + deltaX, originZ,
                             modelMatrix, projMatrix, viewport)
        if self.buttondown == GLUT_RIGHT_BUTTON:
            self.offset[0] += deltaX * TRANSRATIO / self.height
            self.offset[1] -= deltaY * TRANSRATIO / self.height
        if self.buttondown == GLUT_MIDDLE_BUTTON:
            DEPTH_RATIO = 0.2
            self.offset[2] += deltaY * DEPTH_RATIO
        self.x, self.y = (x, y)
        self.idle()

    def positionInit(self):
        self.offset = [0, 0, self.depth]
        self.state = self.ident.rotAroundAxis(self.rotX, 1, 0, 0)\
            .rotAroundAxis(self.rotY, 0, 1, 0)\
            .rotAroundAxis(self.rotZ, 0, 0, 1)

    def idle(self):
        self.state = self.state.rotAroundAxis(
            self.angle, self.axisX, self.axisY, self.axisZ)
        self.display()

    def display(self):
        glLoadIdentity()
        glMultMatrixd(self.state.setMatrix(self.offset))
        self.coredisplay()
