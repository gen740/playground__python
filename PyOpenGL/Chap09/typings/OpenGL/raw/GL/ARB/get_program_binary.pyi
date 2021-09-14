"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_NUM_PROGRAM_BINARY_FORMATS = ...
GL_PROGRAM_BINARY_FORMATS = ...
GL_PROGRAM_BINARY_LENGTH = ...
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = ...
@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLuintArray, ctypes.c_void_p)
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, ctypes.c_void_p, _cs.GLsizei)
def glProgramBinary(program, binaryFormat, binary, length):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLint)
def glProgramParameteri(program, pname, value):
    ...

