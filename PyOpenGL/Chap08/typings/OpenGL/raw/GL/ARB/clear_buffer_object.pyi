"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

"""
This type stub file was generated by pyright.
"""
_EXTENSION_NAME = ...
@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glClearBufferData(target, internalformat, format, type, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLintptr, _cs.GLsizeiptr, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glClearBufferSubData(target, internalformat, offset, size, format, type, data):
    ...
