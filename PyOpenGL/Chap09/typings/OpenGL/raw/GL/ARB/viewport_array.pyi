"""
This type stub file was generated by pyright.
"""

from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_DEPTH_RANGE = ...
GL_FIRST_VERTEX_CONVENTION = ...
GL_LAST_VERTEX_CONVENTION = ...
GL_LAYER_PROVOKING_VERTEX = ...
GL_MAX_VIEWPORTS = ...
GL_PROVOKING_VERTEX = ...
GL_SCISSOR_BOX = ...
GL_SCISSOR_TEST = ...
GL_UNDEFINED_VERTEX = ...
GL_VIEWPORT = ...
GL_VIEWPORT_BOUNDS_RANGE = ...
GL_VIEWPORT_INDEX_PROVOKING_VERTEX = ...
GL_VIEWPORT_SUBPIXEL_BITS = ...
@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLdoubleArray)
def glDepthRangeArrayv(first, count, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLdouble, _cs.GLdouble)
def glDepthRangeIndexed(index, n, f):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, arrays.GLdoubleArray)
def glGetDoublei_v(target, index, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, arrays.GLfloatArray)
def glGetFloati_v(target, index, data):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLintArray)
def glScissorArrayv(first, count, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei)
def glScissorIndexed(index, left, bottom, width, height):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLintArray)
def glScissorIndexedv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLfloatArray)
def glViewportArrayv(first, count, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glViewportIndexedf(index, x, y, w, h):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLfloatArray)
def glViewportIndexedfv(index, v):
    ...

