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
GL_ARRAY_BUFFER = ...
GL_ARRAY_BUFFER_BINDING = ...
GL_BUFFER_ACCESS = ...
GL_BUFFER_MAPPED = ...
GL_BUFFER_MAP_POINTER = ...
GL_BUFFER_SIZE = ...
GL_BUFFER_USAGE = ...
GL_COLOR_ARRAY_BUFFER_BINDING = ...
GL_CURRENT_FOG_COORD = ...
GL_CURRENT_QUERY = ...
GL_DYNAMIC_COPY = ...
GL_DYNAMIC_DRAW = ...
GL_DYNAMIC_READ = ...
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = ...
GL_ELEMENT_ARRAY_BUFFER = ...
GL_ELEMENT_ARRAY_BUFFER_BINDING = ...
GL_FOG_COORD = ...
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = ...
GL_FOG_COORD_ARRAY = ...
GL_FOG_COORD_ARRAY_BUFFER_BINDING = ...
GL_FOG_COORD_ARRAY_POINTER = ...
GL_FOG_COORD_ARRAY_STRIDE = ...
GL_FOG_COORD_ARRAY_TYPE = ...
GL_FOG_COORD_SRC = ...
GL_INDEX_ARRAY_BUFFER_BINDING = ...
GL_NORMAL_ARRAY_BUFFER_BINDING = ...
GL_QUERY_COUNTER_BITS = ...
GL_QUERY_RESULT = ...
GL_QUERY_RESULT_AVAILABLE = ...
GL_READ_ONLY = ...
GL_READ_WRITE = ...
GL_SAMPLES_PASSED = ...
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = ...
GL_SRC0_ALPHA = ...
GL_SRC0_RGB = ...
GL_SRC1_ALPHA = ...
GL_SRC1_RGB = ...
GL_SRC2_ALPHA = ...
GL_SRC2_RGB = ...
GL_STATIC_COPY = ...
GL_STATIC_DRAW = ...
GL_STATIC_READ = ...
GL_STREAM_COPY = ...
GL_STREAM_DRAW = ...
GL_STREAM_READ = ...
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = ...
GL_VERTEX_ARRAY_BUFFER_BINDING = ...
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = ...
GL_WEIGHT_ARRAY_BUFFER_BINDING = ...
GL_WRITE_ONLY = ...
@_f
@_p.types(None, _cs.GLenum, _cs.GLuint)
def glBeginQuery(target, id):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint)
def glBindBuffer(target, buffer):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizeiptr, ctypes.c_void_p, _cs.GLenum)
def glBufferData(target, size, data, usage):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLintptr, _cs.GLsizeiptr, ctypes.c_void_p)
def glBufferSubData(target, offset, size, data):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDeleteBuffers(n, buffers):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDeleteQueries(n, ids):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glEndQuery(target):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenBuffers(n, buffers):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenQueries(n, ids):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetBufferParameteriv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLvoidpArray)
def glGetBufferPointerv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLintptr, _cs.GLsizeiptr, ctypes.c_void_p)
def glGetBufferSubData(target, offset, size, data):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetQueryObjectiv(id, pname, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLuintArray)
def glGetQueryObjectuiv(id, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetQueryiv(target, pname, params):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsBuffer(buffer):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsQuery(id):
    ...

@_f
@_p.types(ctypes.c_void_p, _cs.GLenum, _cs.GLenum)
def glMapBuffer(target, access):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLenum)
def glUnmapBuffer(target):
    ...

