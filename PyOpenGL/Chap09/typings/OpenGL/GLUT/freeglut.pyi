"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL.raw.GL._types import *

"""FreeGLUT extensions to the GLUT API

This module will provide the FreeGLUT extensions if they are available
from the GLUT module.  Note that any other implementation that also provides
these entry points will also retrieve the entry points with this module.
"""
FUNCTION_TYPE = ...
c_int = ...
c_char_p = ctypes.c_char_p
c_ubyte = ctypes.c_ubyte
c_void_p = ctypes.c_void_p
GLUT_DEBUG = ...
GLUT_FORWARD_COMPATIBLE = ...
GLUT_ACTION_EXIT = ...
GLUT_ACTION_GLUTMAINLOOP_RETURNS = ...
GLUT_ACTION_CONTINUE_EXECUTION = ...
GLUT_INIT_MAJOR_VERSION = ...
GLUT_INIT_MINOR_VERSION = ...
GLUT_INIT_FLAGS = ...
GLUT_CREATE_NEW_CONTEXT = ...
GLUT_USE_CURRENT_CONTEXT = ...
GLUT_ACTION_ON_WINDOW_CLOSE = ...
GLUT_WINDOW_BORDER_WIDTH = ...
GLUT_WINDOW_HEADER_HEIGHT = ...
GLUT_RENDERING_CONTEXT = ...
GLUT_ALLOW_DIRECT_CONTEXT = ...
GLUT_AUX = ...
GLUT_AUX1 = ...
GLUT_AUX2 = ...
GLUT_AUX3 = ...
GLUT_AUX4 = ...
GLUT_BORDERLESS = ...
GLUT_CAPTIONLESS = ...
GLUT_COMPATIBILITY_PROFILE = ...
GLUT_CORE_PROFILE = ...
GLUT_DIRECT_RENDERING = ...
GLUT_FORCE_DIRECT_CONTEXT = ...
GLUT_FORCE_INDIRECT_CONTEXT = ...
GLUT_FULL_SCREEN = ...
GLUT_INIT_PROFILE = ...
GLUT_KEY_BEGIN = ...
GLUT_KEY_DELETE = ...
GLUT_KEY_NUM_LOCK = ...
GLUT_SRGB = ...
GLUT_TRY_DIRECT_CONTEXT = ...
glutMainLoopEvent = ...
glutLeaveMainLoop = ...
glutMouseWheelFunc = ...
glutCloseFunc = ...
glutWMCloseFunc = ...
glutMenuDestroyFunc = ...
glutSetOption = ...
glutGetWindowData = ...
glutSetWindowData = ...
glutGetMenuData = ...
glutSetMenuData = ...
glutBitmapHeight = ...
glutStrokeHeight = ...
glutBitmapString = ...
glutStrokeString = ...
glutWireRhombicDodecahedron = ...
glutSolidRhombicDodecahedron = ...
glutWireSierpinskiSponge = ...
glutWireSierpinskiSponge = ...
glutSolidSierpinskiSponge = ...
glutSolidSierpinskiSponge = ...
glutWireCylinder = ...
glutSolidCylinder = ...
glutGetProcAddress = ...
glutInitContextFlags = ...
glutInitContextProfile = ...
glutInitContextVersion = ...
glutFullScreenToggle = ...
glutGetModeValues = ...
fgDeinitialize = ...