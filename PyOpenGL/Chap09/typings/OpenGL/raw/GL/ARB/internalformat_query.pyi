"""
This type stub file was generated by pyright.
"""

from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_NUM_SAMPLE_COUNTS = ...
@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLenum, _cs.GLsizei, arrays.GLintArray)
def glGetInternalformativ(target, internalformat, pname, bufSize, params):
    ...

