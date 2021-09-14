"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_ACTIVE_PROGRAM = ...
GL_ALL_SHADER_BITS = ...
GL_FRAGMENT_SHADER_BIT = ...
GL_GEOMETRY_SHADER_BIT = ...
GL_PROGRAM_PIPELINE_BINDING = ...
GL_PROGRAM_SEPARABLE = ...
GL_TESS_CONTROL_SHADER_BIT = ...
GL_TESS_EVALUATION_SHADER_BIT = ...
GL_VERTEX_SHADER_BIT = ...
@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glActiveShaderProgram(pipeline, program):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glBindProgramPipeline(pipeline):
    ...

@_f
@_p.types(_cs.GLuint, _cs.GLenum, _cs.GLsizei, ctypes.POINTER(ctypes.POINTER(_cs.GLchar)))
def glCreateShaderProgramv(type, count, strings):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDeleteProgramPipelines(n, pipelines):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenProgramPipelines(n, pipelines):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetProgramPipelineiv(pipeline, pname, params):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsProgramPipeline(pipeline):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLint)
def glProgramParameteri(program, pname, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLdouble)
def glProgramUniform1d(program, location, v0):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLdoubleArray)
def glProgramUniform1dv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLfloat)
def glProgramUniform1f(program, location, v0):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glProgramUniform1fv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLint)
def glProgramUniform1i(program, location, v0):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glProgramUniform1iv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLuint)
def glProgramUniform1ui(program, location, v0):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glProgramUniform1uiv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLdouble, _cs.GLdouble)
def glProgramUniform2d(program, location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLdoubleArray)
def glProgramUniform2dv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLfloat, _cs.GLfloat)
def glProgramUniform2f(program, location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glProgramUniform2fv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLint, _cs.GLint)
def glProgramUniform2i(program, location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glProgramUniform2iv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLuint, _cs.GLuint)
def glProgramUniform2ui(program, location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glProgramUniform2uiv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glProgramUniform3d(program, location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLdoubleArray)
def glProgramUniform3dv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glProgramUniform3f(program, location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glProgramUniform3fv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glProgramUniform3i(program, location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glProgramUniform3iv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glProgramUniform3ui(program, location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glProgramUniform3uiv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glProgramUniform4d(program, location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLdoubleArray)
def glProgramUniform4dv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glProgramUniform4f(program, location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLfloatArray)
def glProgramUniform4fv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glProgramUniform4i(program, location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLintArray)
def glProgramUniform4iv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLuint, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glProgramUniform4ui(program, location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glProgramUniform4uiv(program, location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix2dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix2x3dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix2x4dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix3dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix3x2dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix3x4dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix4dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix4x2dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLdoubleArray)
def glProgramUniformMatrix4x3dv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLbitfield, _cs.GLuint)
def glUseProgramStages(pipeline, stages, program):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glValidateProgramPipeline(pipeline):
    ...

