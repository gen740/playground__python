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
GL_MAX_VERTEX_ATTRIB_BINDINGS = ...
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = ...
GL_VERTEX_ATTRIB_BINDING = ...
GL_VERTEX_ATTRIB_RELATIVE_OFFSET = ...
GL_VERTEX_BINDING_DIVISOR = ...
GL_VERTEX_BINDING_OFFSET = ...
GL_VERTEX_BINDING_STRIDE = ...
@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLintptr, _cs.GLsizei)
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glVertexAttribBinding(attribindex, bindingindex):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLenum, _cs.GLboolean, _cs.GLuint)
def glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLenum, _cs.GLuint)
def glVertexAttribIFormat(attribindex, size, type, relativeoffset):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLenum, _cs.GLuint)
def glVertexAttribLFormat(attribindex, size, type, relativeoffset):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glVertexBindingDivisor(bindingindex, divisor):
    ...

