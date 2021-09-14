"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

"""
This type stub file was generated by pyright.
"""
_EXTENSION_NAME = ...
GL_FIXED = ...
GL_HIGH_FLOAT = ...
GL_HIGH_INT = ...
GL_IMPLEMENTATION_COLOR_READ_FORMAT = ...
GL_IMPLEMENTATION_COLOR_READ_TYPE = ...
GL_LOW_FLOAT = ...
GL_LOW_INT = ...
GL_MAX_FRAGMENT_UNIFORM_VECTORS = ...
GL_MAX_VARYING_VECTORS = ...
GL_MAX_VERTEX_UNIFORM_VECTORS = ...
GL_MEDIUM_FLOAT = ...
GL_MEDIUM_INT = ...
GL_NUM_SHADER_BINARY_FORMATS = ...
GL_RGB565 = ...
GL_SHADER_BINARY_FORMATS = ...
GL_SHADER_COMPILER = ...
@_f
@_p.types(None, _cs.GLfloat)
def glClearDepthf(d):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat)
def glDepthRangef(n, f):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray, arrays.GLintArray)
def glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision):
    ...

@_f
@_p.types(None)
def glReleaseShaderCompiler():
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray, _cs.GLenum, ctypes.c_void_p, _cs.GLsizei)
def glShaderBinary(count, shaders, binaryformat, binary, length):
    ...

