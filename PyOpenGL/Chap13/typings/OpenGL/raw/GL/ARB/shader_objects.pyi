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
GL_BOOL_ARB = ...
GL_BOOL_VEC2_ARB = ...
GL_BOOL_VEC3_ARB = ...
GL_BOOL_VEC4_ARB = ...
GL_FLOAT_MAT2_ARB = ...
GL_FLOAT_MAT3_ARB = ...
GL_FLOAT_MAT4_ARB = ...
GL_FLOAT_VEC2_ARB = ...
GL_FLOAT_VEC3_ARB = ...
GL_FLOAT_VEC4_ARB = ...
GL_INT_VEC2_ARB = ...
GL_INT_VEC3_ARB = ...
GL_INT_VEC4_ARB = ...
GL_OBJECT_ACTIVE_UNIFORMS_ARB = ...
GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = ...
GL_OBJECT_ATTACHED_OBJECTS_ARB = ...
GL_OBJECT_COMPILE_STATUS_ARB = ...
GL_OBJECT_DELETE_STATUS_ARB = ...
GL_OBJECT_INFO_LOG_LENGTH_ARB = ...
GL_OBJECT_LINK_STATUS_ARB = ...
GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = ...
GL_OBJECT_SUBTYPE_ARB = ...
GL_OBJECT_TYPE_ARB = ...
GL_OBJECT_VALIDATE_STATUS_ARB = ...
GL_PROGRAM_OBJECT_ARB = ...
GL_SAMPLER_1D_ARB = ...
GL_SAMPLER_1D_SHADOW_ARB = ...
GL_SAMPLER_2D_ARB = ...
GL_SAMPLER_2D_RECT_ARB = ...
GL_SAMPLER_2D_RECT_SHADOW_ARB = ...
GL_SAMPLER_2D_SHADOW_ARB = ...
GL_SAMPLER_3D_ARB = ...
GL_SAMPLER_CUBE_ARB = ...
GL_SHADER_OBJECT_ARB = ...
@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLhandleARB)
def glAttachObjectARB(containerObj, obj):
    ...

@_f
@_p.types(None, _cs.GLhandleARB)
def glCompileShaderARB(shaderObj):
    ...

@_f
@_p.types(_cs.GLhandleARB)
def glCreateProgramObjectARB():
    ...

@_f
@_p.types(_cs.GLhandleARB, _cs.GLenum)
def glCreateShaderObjectARB(shaderType):
    ...

@_f
@_p.types(None, _cs.GLhandleARB)
def glDeleteObjectARB(obj):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLhandleARB)
def glDetachObjectARB(containerObj, attachedObj):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLintArray, arrays.GLuintArray, arrays.GLcharARBArray)
def glGetActiveUniformARB(programObj, index, maxLength, length, size, type, name):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLuintArray)
def glGetAttachedObjectsARB(containerObj, maxCount, count, obj):
    ...

@_f
@_p.types(_cs.GLhandleARB, _cs.GLenum)
def glGetHandleARB(pname):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharARBArray)
def glGetInfoLogARB(obj, maxLength, length, infoLog):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLenum, arrays.GLfloatArray)
def glGetObjectParameterfvARB(obj, pname, params):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLenum, arrays.GLintArray)
def glGetObjectParameterivARB(obj, pname, params):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharARBArray)
def glGetShaderSourceARB(obj, maxLength, length, source):
    ...

@_f
@_p.types(_cs.GLint, _cs.GLhandleARB, arrays.GLcharARBArray)
def glGetUniformLocationARB(programObj, name):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLint, arrays.GLfloatArray)
def glGetUniformfvARB(programObj, location, params):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLint, arrays.GLintArray)
def glGetUniformivARB(programObj, location, params):
    ...

@_f
@_p.types(None, _cs.GLhandleARB)
def glLinkProgramARB(programObj):
    ...

@_f
@_p.types(None, _cs.GLhandleARB, _cs.GLsizei, ctypes.POINTER(ctypes.POINTER(_cs.GLchar)), arrays.GLintArray)
def glShaderSourceARB(shaderObj, count, string, length):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat)
def glUniform1fARB(location, v0):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform1fvARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint)
def glUniform1iARB(location, v0):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform1ivARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat)
def glUniform2fARB(location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform2fvARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint)
def glUniform2iARB(location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform2ivARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glUniform3fARB(location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform3fvARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glUniform3iARB(location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform3ivARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glUniform4fARB(location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glUniform4fvARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glUniform4iARB(location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glUniform4ivARB(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix2fvARB(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix3fvARB(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glUniformMatrix4fvARB(location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLhandleARB)
def glUseProgramObjectARB(programObj):
    ...

@_f
@_p.types(None, _cs.GLhandleARB)
def glValidateProgramARB(programObj):
    ...

