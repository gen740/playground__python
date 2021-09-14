"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GLUT.constants import *
from ctypes import *
from OpenGL._bytes import unicode
from OpenGL import arrays, platform
from OpenGL.constant import Constant
from OpenGL.raw.GL import _types as GL_types
from OpenGL.raw.GL._types import GLdouble, GLenum, GLfloat, GLint

"""
This type stub file was generated by pyright.
"""
GLvoid = ...
if hasattr(platform.PLATFORM, 'GLUT_CALLBACK_TYPE'):
    CALLBACK_FUNCTION_TYPE = ...
else:
    CALLBACK_FUNCTION_TYPE = ...
class STRING(c_char_p):
    @classmethod
    def from_param(cls, value):
        ...
    


glutAddMenuEntry = ...
glutAddSubMenu = ...
glutAttachMenu = ...
glutBitmapCharacter = ...
glutBitmapLength = ...
glutBitmapWidth = ...
glutButtonBoxFunc = ...
glutChangeToMenuEntry = ...
glutChangeToSubMenu = ...
glutCopyColormap = ...
glutCreateMenu = ...
glutCreateSubWindow = ...
glutCreateWindow = ...
glutDestroyMenu = ...
glutDestroyWindow = ...
glutDetachMenu = ...
glutDeviceGet = ...
glutDialsFunc = ...
glutDisplayFunc = ...
glutEnterGameMode = ...
glutEntryFunc = ...
glutEstablishOverlay = ...
glutExtensionSupported = ...
glutForceJoystickFunc = ...
glutFullScreen = ...
glutGameModeGet = ...
glutGameModeString = ...
glutGet = ...
glutGetColor = ...
glutGetMenu = ...
glutGetModifiers = ...
glutGetWindow = ...
glutHideOverlay = ...
glutHideWindow = ...
glutIconifyWindow = ...
glutIdleFunc = ...
glutIgnoreKeyRepeat = ...
glutInit = ...
glutInitDisplayMode = ...
glutInitDisplayString = ...
glutInitWindowPosition = ...
glutInitWindowSize = ...
glutJoystickFunc = ...
glutKeyboardFunc = ...
glutKeyboardUpFunc = ...
glutLayerGet = ...
glutLeaveGameMode = ...
glutMainLoop = ...
glutMenuStateFunc = ...
glutMenuStatusFunc = ...
glutMotionFunc = ...
glutMouseFunc = ...
glutOverlayDisplayFunc = ...
glutPassiveMotionFunc = ...
glutPopWindow = ...
glutPositionWindow = ...
glutPostOverlayRedisplay = ...
glutPostRedisplay = ...
glutPostWindowOverlayRedisplay = ...
glutPostWindowRedisplay = ...
glutPushWindow = ...
glutRemoveMenuItem = ...
glutRemoveOverlay = ...
glutReportErrors = ...
glutReshapeFunc = ...
glutReshapeWindow = ...
glutSetColor = ...
glutSetCursor = ...
glutSetIconTitle = ...
glutSetKeyRepeat = ...
glutSetMenu = ...
glutSetWindow = ...
glutSetWindowTitle = ...
glutSetupVideoResizing = ...
glutShowOverlay = ...
glutShowWindow = ...
glutSolidCone = ...
glutSolidCube = ...
glutSolidDodecahedron = ...
glutSolidIcosahedron = ...
glutSolidOctahedron = ...
glutSolidSphere = ...
glutSolidTeapot = ...
glutSolidTetrahedron = ...
glutSolidTorus = ...
glutSpaceballButtonFunc = ...
glutSpaceballMotionFunc = ...
glutSpaceballRotateFunc = ...
glutSpecialFunc = ...
glutSpecialUpFunc = ...
glutStopVideoResizing = ...
glutStrokeCharacter = ...
glutStrokeLength = ...
glutStrokeWidth = ...
glutSwapBuffers = ...
glutTabletButtonFunc = ...
glutTabletMotionFunc = ...
glutTimerFunc = ...
glutUseLayer = ...
glutVideoPan = ...
glutVideoResize = ...
glutVideoResizeGet = ...
glutVisibilityFunc = ...
glutWarpPointer = ...
glutWindowStatusFunc = ...
glutWireCone = ...
glutWireCube = ...
glutWireDodecahedron = ...
glutWireIcosahedron = ...
glutWireOctahedron = ...
glutWireSphere = ...
glutWireTeapot = ...
glutWireTetrahedron = ...
glutWireTorus = ...