from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from myGLCanvas import MyGLCanvas


class MySpinCanvas(MyGLCanvas):
    def __init__(self):
        super().__init__()
        self.x, self.y = self.startX, self.startY = (-1, -1)
        self.buttondown = -1
        self.angle = 0
        self.total = [0, 0]
        self.axisX, self.axisY, self.axisZ = (0, 0, 1)

    def mouse(self, button, state, x, y):
        if state == GLUT_DOWN:
            self.buttondown = button
            self.x, self.y = self.startX, self.startY = (x, y)
        if state == GLUT_UP:
            self.buttondown = -1
        if button == GLUT_LEFT_BUTTON:
            glutIdleFunc(self.idle)
        if button == GLUT_RIGHT_BUTTON:
            self.angle = 0
            self.total = [0, 0]
        if button == GLUT_MIDDLE_BUTTON:
            self.angle /= 1.1
            self.total = [self.total[0] / 1.1, self.total[1] / 1.1]

    def motion(self, x, y):
        deltaX, deltaY = (x - self.x, y - self.y)
        self.total[0] += deltaX
        self.total[1] += deltaY
        if self.buttondown == GLUT_LEFT_BUTTON or self.buttondown == GLUT_RIGHT_BUTTON:
            SPINRATIO = 0.5
            self.angle = (self.total[0]**2 + self.total[1]**2)**0.5 * SPINRATIO / \
                min(self.width, self.height)
            modelMatrix = glGetDoublev(GL_MODELVIEW_MATRIX)
            projMatrix = glGetDoublev(GL_PROJECTION_MATRIX)
            viewport = glGetIntegerv(GL_VIEWPORT)
            originX, originY, originZ = \
                gluProject(0, 0, 0, modelMatrix, projMatrix, viewport)
            self.axisX, self.axisY, self.axisZ = \
                gluUnProject(originX + self.total[1], originY + self.total[0], originZ,
                             modelMatrix, projMatrix, viewport)
        self.x, self.y = (x, y)
        self.idle()

    def positionInit(self):
        glTranslated(0, 0, self.depth)
        glRotated(self.rotX, 1, 0, 0)
        glRotated(self.rotY, 0, 1, 0)
        glRotated(self.rotZ, 0, 0, 1)

    def idle(self):
        glRotated(self.angle, self.axisX, self.axisY, self.axisZ)
        self.display()

    def display(self):
        self.coredisplay()

    def loop(self):
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutIdleFunc(None)
        glutMainLoop()
