"""
This type stub file was generated by pyright.
"""

from OpenGL import platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

"""
This type stub file was generated by pyright.
"""
_EXTENSION_NAME = ...
@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, _cs.GLsizei, _cs.GLsizei, _cs.GLboolean)
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, _cs.GLsizei, _cs.GLsizei, _cs.GLsizei, _cs.GLboolean)
def glTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations):
    ...

