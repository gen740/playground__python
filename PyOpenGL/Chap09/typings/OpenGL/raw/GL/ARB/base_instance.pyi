"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLsizei, _cs.GLsizei, _cs.GLuint)
def glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, ctypes.c_void_p, _cs.GLsizei, _cs.GLuint)
def glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, ctypes.c_void_p, _cs.GLsizei, _cs.GLint, _cs.GLuint)
def glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance):
    ...

