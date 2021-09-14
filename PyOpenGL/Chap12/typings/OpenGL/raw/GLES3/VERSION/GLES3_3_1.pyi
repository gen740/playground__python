"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.GLES3 import _types as _cs
from OpenGL.raw.GLES3._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_ACTIVE_ATOMIC_COUNTER_BUFFERS = ...
GL_ACTIVE_PROGRAM = ...
GL_ACTIVE_RESOURCES = ...
GL_ACTIVE_VARIABLES = ...
GL_ALL_BARRIER_BITS = ...
GL_ALL_SHADER_BITS = ...
GL_ARRAY_SIZE = ...
GL_ARRAY_STRIDE = ...
GL_ATOMIC_COUNTER_BARRIER_BIT = ...
GL_ATOMIC_COUNTER_BUFFER = ...
GL_ATOMIC_COUNTER_BUFFER = ...
GL_ATOMIC_COUNTER_BUFFER_BINDING = ...
GL_ATOMIC_COUNTER_BUFFER_INDEX = ...
GL_ATOMIC_COUNTER_BUFFER_SIZE = ...
GL_ATOMIC_COUNTER_BUFFER_START = ...
GL_BLOCK_INDEX = ...
GL_BUFFER_BINDING = ...
GL_BUFFER_DATA_SIZE = ...
GL_BUFFER_UPDATE_BARRIER_BIT = ...
GL_BUFFER_VARIABLE = ...
GL_COMMAND_BARRIER_BIT = ...
GL_COMPUTE_SHADER = ...
GL_COMPUTE_SHADER_BIT = ...
GL_COMPUTE_WORK_GROUP_SIZE = ...
GL_DEPTH_STENCIL_TEXTURE_MODE = ...
GL_DISPATCH_INDIRECT_BUFFER = ...
GL_DISPATCH_INDIRECT_BUFFER_BINDING = ...
GL_DRAW_INDIRECT_BUFFER = ...
GL_DRAW_INDIRECT_BUFFER_BINDING = ...
GL_ELEMENT_ARRAY_BARRIER_BIT = ...
GL_FRAGMENT_SHADER_BIT = ...
GL_FRAMEBUFFER_BARRIER_BIT = ...
GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = ...
GL_FRAMEBUFFER_DEFAULT_HEIGHT = ...
GL_FRAMEBUFFER_DEFAULT_SAMPLES = ...
GL_FRAMEBUFFER_DEFAULT_WIDTH = ...
GL_IMAGE_2D = ...
GL_IMAGE_2D_ARRAY = ...
GL_IMAGE_3D = ...
GL_IMAGE_BINDING_ACCESS = ...
GL_IMAGE_BINDING_FORMAT = ...
GL_IMAGE_BINDING_LAYER = ...
GL_IMAGE_BINDING_LAYERED = ...
GL_IMAGE_BINDING_LEVEL = ...
GL_IMAGE_BINDING_NAME = ...
GL_IMAGE_CUBE = ...
GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS = ...
GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE = ...
GL_IMAGE_FORMAT_COMPATIBILITY_TYPE = ...
GL_INT_IMAGE_2D = ...
GL_INT_IMAGE_2D_ARRAY = ...
GL_INT_IMAGE_3D = ...
GL_INT_IMAGE_CUBE = ...
GL_INT_SAMPLER_2D_MULTISAMPLE = ...
GL_IS_ROW_MAJOR = ...
GL_LOCATION = ...
GL_MATRIX_STRIDE = ...
GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS = ...
GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE = ...
GL_MAX_COLOR_TEXTURE_SAMPLES = ...
GL_MAX_COMBINED_ATOMIC_COUNTERS = ...
GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS = ...
GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = ...
GL_MAX_COMBINED_IMAGE_UNIFORMS = ...
GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES = ...
GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS = ...
GL_MAX_COMPUTE_ATOMIC_COUNTERS = ...
GL_MAX_COMPUTE_ATOMIC_COUNTERS = ...
GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = ...
GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = ...
GL_MAX_COMPUTE_IMAGE_UNIFORMS = ...
GL_MAX_COMPUTE_IMAGE_UNIFORMS = ...
GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS = ...
GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = ...
GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = ...
GL_MAX_COMPUTE_UNIFORM_BLOCKS = ...
GL_MAX_COMPUTE_UNIFORM_COMPONENTS = ...
GL_MAX_COMPUTE_WORK_GROUP_COUNT = ...
GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS = ...
GL_MAX_COMPUTE_WORK_GROUP_SIZE = ...
GL_MAX_DEPTH_TEXTURE_SAMPLES = ...
GL_MAX_FRAGMENT_ATOMIC_COUNTERS = ...
GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS = ...
GL_MAX_FRAGMENT_IMAGE_UNIFORMS = ...
GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = ...
GL_MAX_FRAMEBUFFER_HEIGHT = ...
GL_MAX_FRAMEBUFFER_SAMPLES = ...
GL_MAX_FRAMEBUFFER_WIDTH = ...
GL_MAX_IMAGE_UNITS = ...
GL_MAX_INTEGER_SAMPLES = ...
GL_MAX_NAME_LENGTH = ...
GL_MAX_NUM_ACTIVE_VARIABLES = ...
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = ...
GL_MAX_SAMPLE_MASK_WORDS = ...
GL_MAX_SHADER_STORAGE_BLOCK_SIZE = ...
GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS = ...
GL_MAX_UNIFORM_LOCATIONS = ...
GL_MAX_VERTEX_ATOMIC_COUNTERS = ...
GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS = ...
GL_MAX_VERTEX_ATTRIB_BINDINGS = ...
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = ...
GL_MAX_VERTEX_ATTRIB_STRIDE = ...
GL_MAX_VERTEX_IMAGE_UNIFORMS = ...
GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS = ...
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = ...
GL_NAME_LENGTH = ...
GL_NUM_ACTIVE_VARIABLES = ...
GL_OFFSET = ...
GL_PIXEL_BUFFER_BARRIER_BIT = ...
GL_PROGRAM_INPUT = ...
GL_PROGRAM_OUTPUT = ...
GL_PROGRAM_PIPELINE_BINDING = ...
GL_PROGRAM_SEPARABLE = ...
GL_READ_ONLY = ...
GL_READ_WRITE = ...
GL_REFERENCED_BY_COMPUTE_SHADER = ...
GL_REFERENCED_BY_FRAGMENT_SHADER = ...
GL_REFERENCED_BY_VERTEX_SHADER = ...
GL_SAMPLER_2D_MULTISAMPLE = ...
GL_SAMPLE_MASK = ...
GL_SAMPLE_MASK_VALUE = ...
GL_SAMPLE_POSITION = ...
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT = ...
GL_SHADER_STORAGE_BARRIER_BIT = ...
GL_SHADER_STORAGE_BLOCK = ...
GL_SHADER_STORAGE_BUFFER = ...
GL_SHADER_STORAGE_BUFFER_BINDING = ...
GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = ...
GL_SHADER_STORAGE_BUFFER_SIZE = ...
GL_SHADER_STORAGE_BUFFER_START = ...
GL_STENCIL_INDEX = ...
GL_TEXTURE_2D_MULTISAMPLE = ...
GL_TEXTURE_ALPHA_SIZE = ...
GL_TEXTURE_ALPHA_TYPE = ...
GL_TEXTURE_BINDING_2D_MULTISAMPLE = ...
GL_TEXTURE_BLUE_SIZE = ...
GL_TEXTURE_BLUE_TYPE = ...
GL_TEXTURE_COMPRESSED = ...
GL_TEXTURE_DEPTH = ...
GL_TEXTURE_DEPTH_SIZE = ...
GL_TEXTURE_DEPTH_TYPE = ...
GL_TEXTURE_FETCH_BARRIER_BIT = ...
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = ...
GL_TEXTURE_GREEN_SIZE = ...
GL_TEXTURE_GREEN_TYPE = ...
GL_TEXTURE_HEIGHT = ...
GL_TEXTURE_INTERNAL_FORMAT = ...
GL_TEXTURE_RED_SIZE = ...
GL_TEXTURE_RED_TYPE = ...
GL_TEXTURE_SAMPLES = ...
GL_TEXTURE_SHARED_SIZE = ...
GL_TEXTURE_STENCIL_SIZE = ...
GL_TEXTURE_UPDATE_BARRIER_BIT = ...
GL_TEXTURE_WIDTH = ...
GL_TOP_LEVEL_ARRAY_SIZE = ...
GL_TOP_LEVEL_ARRAY_STRIDE = ...
GL_TRANSFORM_FEEDBACK_BARRIER_BIT = ...
GL_TRANSFORM_FEEDBACK_VARYING = ...
GL_TYPE = ...
GL_UNIFORM = ...
GL_UNIFORM_BARRIER_BIT = ...
GL_UNIFORM_BLOCK = ...
GL_UNSIGNED_INT_ATOMIC_COUNTER = ...
GL_UNSIGNED_INT_IMAGE_2D = ...
GL_UNSIGNED_INT_IMAGE_2D_ARRAY = ...
GL_UNSIGNED_INT_IMAGE_3D = ...
GL_UNSIGNED_INT_IMAGE_CUBE = ...
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = ...
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT = ...
GL_VERTEX_ATTRIB_BINDING = ...
GL_VERTEX_ATTRIB_RELATIVE_OFFSET = ...
GL_VERTEX_BINDING_BUFFER = ...
GL_VERTEX_BINDING_DIVISOR = ...
GL_VERTEX_BINDING_OFFSET = ...
GL_VERTEX_BINDING_STRIDE = ...
GL_VERTEX_SHADER_BIT = ...
GL_WRITE_ONLY = ...
@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glActiveShaderProgram(pipeline, program):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLint, _cs.GLboolean, _cs.GLint, _cs.GLenum, _cs.GLenum)
def glBindImageTexture(unit, texture, level, layered, layer, access, format):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glBindProgramPipeline(pipeline):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLintptr, _cs.GLsizei)
def glBindVertexBuffer(bindingindex, buffer, offset, stride):
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
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
    ...

@_f
@_p.types(None, _cs.GLintptr)
def glDispatchComputeIndirect(indirect):
    ...

@_f
@_p.types(None, _cs.GLenum, ctypes.c_void_p)
def glDrawArraysIndirect(mode, indirect):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glDrawElementsIndirect(mode, type, indirect):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLint)
def glFramebufferParameteri(target, pname, param):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenProgramPipelines(n, pipelines):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, arrays.GLbooleanArray)
def glGetBooleani_v(target, index, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetFramebufferParameteriv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, arrays.GLfloatArray)
def glGetMultisamplefv(pname, index, val):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetProgramInterfaceiv(program, programInterface, pname, params):
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
@_p.types(_cs.GLuint, _cs.GLuint, _cs.GLenum, arrays.GLcharArray)
def glGetProgramResourceIndex(program, programInterface, name):
    ...

@_f
@_p.types(_cs.GLint, _cs.GLuint, _cs.GLenum, arrays.GLcharArray)
def glGetProgramResourceLocation(program, programInterface, name):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetProgramResourceName(program, programInterface, index, bufSize, length, name):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLuint, _cs.GLsizei, arrays.GLuintArray, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLintArray)
def glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLenum, arrays.GLfloatArray)
def glGetTexLevelParameterfv(target, level, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLenum, arrays.GLintArray)
def glGetTexLevelParameteriv(target, level, pname, params):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsProgramPipeline(pipeline):
    ...

@_f
@_p.types(None, _cs.GLbitfield)
def glMemoryBarrier(barriers):
    ...

@_f
@_p.types(None, _cs.GLbitfield)
def glMemoryBarrierByRegion(barriers):
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
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix2fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix2x3fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix2x4fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix3fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix3x2fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix3x4fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix4fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix4x2fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLsizei, _cs.GLboolean, arrays.GLfloatArray)
def glProgramUniformMatrix4x3fv(program, location, count, transpose, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLbitfield)
def glSampleMaski(maskNumber, mask):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, _cs.GLsizei, _cs.GLsizei, _cs.GLboolean)
def glTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLbitfield, _cs.GLuint)
def glUseProgramStages(pipeline, stages, program):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glValidateProgramPipeline(pipeline):
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
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glVertexBindingDivisor(bindingindex, divisor):
    ...

