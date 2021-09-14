"""
This type stub file was generated by pyright.
"""

from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

"""
This type stub file was generated by pyright.
"""
_EXTENSION_NAME = ...
GL_COMPRESSED_SLUMINANCE = ...
GL_COMPRESSED_SLUMINANCE_ALPHA = ...
GL_COMPRESSED_SRGB = ...
GL_COMPRESSED_SRGB_ALPHA = ...
GL_CURRENT_RASTER_SECONDARY_COLOR = ...
GL_FLOAT_MAT2x3 = ...
GL_FLOAT_MAT2x4 = ...
GL_FLOAT_MAT3x2 = ...
GL_FLOAT_MAT3x4 = ...
GL_FLOAT_MAT4x2 = ...
GL_FLOAT_MAT4x3 = ...
GL_PIXEL_PACK_BUFFER = ...
GL_PIXEL_PACK_BUFFER_BINDING = ...
GL_PIXEL_UNPACK_BUFFER = ...
GL_PIXEL_UNPACK_BUFFER_BINDING = ...
GL_SLUMINANCE = ...
GL_SLUMINANCE8 = ...
GL_SLUMINANCE8_ALPHA8 = ...
GL_SLUMINANCE_ALPHA = ...
GL_SRGB = ...
GL_SRGB8 = ...
GL_SRGB8_ALPHA8 = ...
GL_SRGB_ALPHA = ...
@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix2x3fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix2x4fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix3x2fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix3x4fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix4x2fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix4x3fv(location, count, transpose, value):
    ...

