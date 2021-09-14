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
GL_ACTIVE_ATTRIBUTES = ...
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = ...
GL_ACTIVE_UNIFORMS = ...
GL_ACTIVE_UNIFORM_MAX_LENGTH = ...
GL_ATTACHED_SHADERS = ...
GL_BLEND_EQUATION_ALPHA = ...
GL_BLEND_EQUATION_RGB = ...
GL_BOOL = ...
GL_BOOL_VEC2 = ...
GL_BOOL_VEC3 = ...
GL_BOOL_VEC4 = ...
GL_COMPILE_STATUS = ...
GL_COORD_REPLACE = ...
GL_CURRENT_PROGRAM = ...
GL_CURRENT_VERTEX_ATTRIB = ...
GL_DELETE_STATUS = ...
GL_DRAW_BUFFER0 = ...
GL_DRAW_BUFFER1 = ...
GL_DRAW_BUFFER10 = ...
GL_DRAW_BUFFER11 = ...
GL_DRAW_BUFFER12 = ...
GL_DRAW_BUFFER13 = ...
GL_DRAW_BUFFER14 = ...
GL_DRAW_BUFFER15 = ...
GL_DRAW_BUFFER2 = ...
GL_DRAW_BUFFER3 = ...
GL_DRAW_BUFFER4 = ...
GL_DRAW_BUFFER5 = ...
GL_DRAW_BUFFER6 = ...
GL_DRAW_BUFFER7 = ...
GL_DRAW_BUFFER8 = ...
GL_DRAW_BUFFER9 = ...
GL_FLOAT_MAT2 = ...
GL_FLOAT_MAT3 = ...
GL_FLOAT_MAT4 = ...
GL_FLOAT_VEC2 = ...
GL_FLOAT_VEC3 = ...
GL_FLOAT_VEC4 = ...
GL_FRAGMENT_SHADER = ...
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = ...
GL_INFO_LOG_LENGTH = ...
GL_INT_VEC2 = ...
GL_INT_VEC3 = ...
GL_INT_VEC4 = ...
GL_LINK_STATUS = ...
GL_LOWER_LEFT = ...
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = ...
GL_MAX_DRAW_BUFFERS = ...
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = ...
GL_MAX_TEXTURE_COORDS = ...
GL_MAX_TEXTURE_IMAGE_UNITS = ...
GL_MAX_VARYING_FLOATS = ...
GL_MAX_VERTEX_ATTRIBS = ...
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = ...
GL_MAX_VERTEX_UNIFORM_COMPONENTS = ...
GL_POINT_SPRITE = ...
GL_POINT_SPRITE_COORD_ORIGIN = ...
GL_SAMPLER_1D = ...
GL_SAMPLER_1D_SHADOW = ...
GL_SAMPLER_2D = ...
GL_SAMPLER_2D_SHADOW = ...
GL_SAMPLER_3D = ...
GL_SAMPLER_CUBE = ...
GL_SHADER_SOURCE_LENGTH = ...
GL_SHADER_TYPE = ...
GL_SHADING_LANGUAGE_VERSION = ...
GL_STENCIL_BACK_FAIL = ...
GL_STENCIL_BACK_FUNC = ...
GL_STENCIL_BACK_PASS_DEPTH_FAIL = ...
GL_STENCIL_BACK_PASS_DEPTH_PASS = ...
GL_STENCIL_BACK_REF = ...
GL_STENCIL_BACK_VALUE_MASK = ...
GL_STENCIL_BACK_WRITEMASK = ...
GL_UPPER_LEFT = ...
GL_VALIDATE_STATUS = ...
GL_VERTEX_ATTRIB_ARRAY_ENABLED = ...
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = ...
GL_VERTEX_ATTRIB_ARRAY_POINTER = ...
GL_VERTEX_ATTRIB_ARRAY_SIZE = ...
GL_VERTEX_ATTRIB_ARRAY_STRIDE = ...
GL_VERTEX_ATTRIB_ARRAY_TYPE = ...
GL_VERTEX_PROGRAM_POINT_SIZE = ...
GL_VERTEX_PROGRAM_TWO_SIDE = ...
GL_VERTEX_SHADER = ...
@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glAttachShader(program, shader):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, arrays.GLcharArray)
def glBindAttribLocation(program, index, name):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum)
def glBlendEquationSeparate(modeRGB, modeAlpha):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glCompileShader(shader):
    ...

@_f
@_p.types(_cs.GLuint)
def glCreateProgram():
    ...

@_f
@_p.types(_cs.GLuint, _cs.GLenum)
def glCreateShader(type):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glDeleteProgram(program):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glDeleteShader(shader):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glDetachShader(program, shader):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glDisableVertexAttribArray(index):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDrawBuffers(n, bufs):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glEnableVertexAttribArray(index):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLintArray, arrays.GLuintArray, arrays.GLcharArray)
def glGetActiveAttrib(program, index, bufSize, length, size, type, name):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLintArray, arrays.GLuintArray, arrays.GLcharArray)
def glGetActiveUniform(program, index, bufSize, length, size, type, name):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLuintArray)
def glGetAttachedShaders(program, maxCount, count, shaders):
    ...

@_f
@_p.types(_cs.GLint, _cs.GLuint, arrays.GLcharArray)
def glGetAttribLocation(program, name):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetProgramInfoLog(program, bufSize, length, infoLog):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetProgramiv(program, pname, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetShaderInfoLog(shader, bufSize, length, infoLog):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetShaderSource(shader, bufSize, length, source):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetShaderiv(shader, pname, params):
    ...

@_f
@_p.types(_cs.GLint, _cs.GLuint, arrays.GLcharArray)
def glGetUniformLocation(program, name):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, arrays.GLfloatArray)
def glGetUniformfv(program, location, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, arrays.GLintArray)
def glGetUniformiv(program, location, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLvoidpArray)
def glGetVertexAttribPointerv(index, pname, pointer):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLdoubleArray)
def glGetVertexAttribdv(index, pname, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLfloatArray)
def glGetVertexAttribfv(index, pname, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetVertexAttribiv(index, pname, params):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsProgram(program):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsShader(shader):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glLinkProgram(program):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, ctypes.POINTER(ctypes.POINTER(_cs.GLchar)), arrays.GLintArray)
def glShaderSource(shader, count, string, length):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLint, _cs.GLuint)
def glStencilFuncSeparate(face, func, ref, mask):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint)
def glStencilMaskSeparate(face, mask):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLenum, _cs.GLenum)
def glStencilOpSeparate(face, sfail, dpfail, dppass):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat)
def glUniform1f(location, v0):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform1fv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint)
def glUniform1i(location, v0):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform1iv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat)
def glUniform2f(location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform2fv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint)
def glUniform2i(location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform2iv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glUniform3f(location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform3fv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glUniform3i(location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform3iv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glUniform4f(location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform4fv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glUniform4i(location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform4iv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix2fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix3fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix4fv(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glUseProgram(program):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glValidateProgram(program):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLdouble)
def glVertexAttrib1d(index, x):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLdoubleArray)
def glVertexAttrib1dv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLfloat)
def glVertexAttrib1f(index, x):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLfloatArray)
def glVertexAttrib1fv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLshort)
def glVertexAttrib1s(index, x):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLshortArray)
def glVertexAttrib1sv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLdouble, _cs.GLdouble)
def glVertexAttrib2d(index, x, y):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLdoubleArray)
def glVertexAttrib2dv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLfloat, _cs.GLfloat)
def glVertexAttrib2f(index, x, y):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLfloatArray)
def glVertexAttrib2fv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLshort, _cs.GLshort)
def glVertexAttrib2s(index, x, y):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLshortArray)
def glVertexAttrib2sv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glVertexAttrib3d(index, x, y, z):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLdoubleArray)
def glVertexAttrib3dv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glVertexAttrib3f(index, x, y, z):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLfloatArray)
def glVertexAttrib3fv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glVertexAttrib3s(index, x, y, z):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLshortArray)
def glVertexAttrib3sv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLbyteArray)
def glVertexAttrib4Nbv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLintArray)
def glVertexAttrib4Niv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLshortArray)
def glVertexAttrib4Nsv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLubyte, _cs.GLubyte, _cs.GLubyte, _cs.GLubyte)
def glVertexAttrib4Nub(index, x, y, z, w):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLubyteArray)
def glVertexAttrib4Nubv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLuintArray)
def glVertexAttrib4Nuiv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLushortArray)
def glVertexAttrib4Nusv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLbyteArray)
def glVertexAttrib4bv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glVertexAttrib4d(index, x, y, z, w):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLdoubleArray)
def glVertexAttrib4dv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glVertexAttrib4f(index, x, y, z, w):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLfloatArray)
def glVertexAttrib4fv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLintArray)
def glVertexAttrib4iv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLshort, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glVertexAttrib4s(index, x, y, z, w):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLshortArray)
def glVertexAttrib4sv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLubyteArray)
def glVertexAttrib4ubv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLuintArray)
def glVertexAttrib4uiv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLushortArray)
def glVertexAttrib4usv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLenum, _cs.GLboolean, _cs.GLsizei, ctypes.c_void_p)
def glVertexAttribPointer(index, size, type, normalized, stride, pointer):
    ...

