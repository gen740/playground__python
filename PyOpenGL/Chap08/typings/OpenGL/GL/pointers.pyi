"""
This type stub file was generated by pyright.
"""

import ctypes

"""
This type stub file was generated by pyright.
"""
GLsizei = ctypes.c_int
GLenum = ctypes.c_uint
GLint = ctypes.c_int
GL_INTERLEAVED_ARRAY_POINTER = ...
POINTER_FUNCTION_DATA = ...
def wrapPointerFunction(name, baseFunction, glType, arrayType, startArgs, defaultSize):
    """Wrap the given pointer-setting function"""
    ...

glVertexPointer = ...
glTexCoordPointer = ...
glNormalPointer = ...
glIndexPointer = ...
glEdgeFlagPointer = ...
glColorPointer = ...
glInterleavedArrays = ...
glDrawElements = ...
def glDrawElementsTyped(type, suffix):
    ...

def glSelectBuffer(size, buffer=...):
    """Create a selection buffer of the given size
    """
    ...

def glFeedbackBuffer(size, type, buffer=...):
    """Create a selection buffer of the given size
    """
    ...

def glRenderMode(newMode):
    """Change to the given rendering mode

    If the current mode is GL_FEEDBACK or GL_SELECT, return
    the current buffer appropriate to the mode
    """
    ...

def glGetPointerv(constant):
    """Retrieve a stored pointer constant"""
    ...
