"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.GLES3 import _types as _cs
from OpenGL.raw.GLES3._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_ACTIVE_UNIFORM_BLOCKS = ...
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = ...
GL_ALREADY_SIGNALED = ...
GL_ANY_SAMPLES_PASSED = ...
GL_ANY_SAMPLES_PASSED_CONSERVATIVE = ...
GL_BLUE = ...
GL_BUFFER_ACCESS_FLAGS = ...
GL_BUFFER_MAPPED = ...
GL_BUFFER_MAP_LENGTH = ...
GL_BUFFER_MAP_OFFSET = ...
GL_BUFFER_MAP_POINTER = ...
GL_COLOR = ...
GL_COLOR_ATTACHMENT1 = ...
GL_COLOR_ATTACHMENT10 = ...
GL_COLOR_ATTACHMENT11 = ...
GL_COLOR_ATTACHMENT12 = ...
GL_COLOR_ATTACHMENT13 = ...
GL_COLOR_ATTACHMENT14 = ...
GL_COLOR_ATTACHMENT15 = ...
GL_COLOR_ATTACHMENT16 = ...
GL_COLOR_ATTACHMENT17 = ...
GL_COLOR_ATTACHMENT18 = ...
GL_COLOR_ATTACHMENT19 = ...
GL_COLOR_ATTACHMENT2 = ...
GL_COLOR_ATTACHMENT20 = ...
GL_COLOR_ATTACHMENT21 = ...
GL_COLOR_ATTACHMENT22 = ...
GL_COLOR_ATTACHMENT23 = ...
GL_COLOR_ATTACHMENT24 = ...
GL_COLOR_ATTACHMENT25 = ...
GL_COLOR_ATTACHMENT26 = ...
GL_COLOR_ATTACHMENT27 = ...
GL_COLOR_ATTACHMENT28 = ...
GL_COLOR_ATTACHMENT29 = ...
GL_COLOR_ATTACHMENT3 = ...
GL_COLOR_ATTACHMENT30 = ...
GL_COLOR_ATTACHMENT31 = ...
GL_COLOR_ATTACHMENT4 = ...
GL_COLOR_ATTACHMENT5 = ...
GL_COLOR_ATTACHMENT6 = ...
GL_COLOR_ATTACHMENT7 = ...
GL_COLOR_ATTACHMENT8 = ...
GL_COLOR_ATTACHMENT9 = ...
GL_COMPARE_REF_TO_TEXTURE = ...
GL_COMPRESSED_R11_EAC = ...
GL_COMPRESSED_RG11_EAC = ...
GL_COMPRESSED_RGB8_ETC2 = ...
GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = ...
GL_COMPRESSED_RGBA8_ETC2_EAC = ...
GL_COMPRESSED_SIGNED_R11_EAC = ...
GL_COMPRESSED_SIGNED_RG11_EAC = ...
GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = ...
GL_COMPRESSED_SRGB8_ETC2 = ...
GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = ...
GL_CONDITION_SATISFIED = ...
GL_COPY_READ_BUFFER = ...
GL_COPY_READ_BUFFER_BINDING = ...
GL_COPY_WRITE_BUFFER = ...
GL_COPY_WRITE_BUFFER_BINDING = ...
GL_CURRENT_QUERY = ...
GL_DEPTH = ...
GL_DEPTH24_STENCIL8 = ...
GL_DEPTH32F_STENCIL8 = ...
GL_DEPTH_COMPONENT24 = ...
GL_DEPTH_COMPONENT32F = ...
GL_DEPTH_STENCIL = ...
GL_DEPTH_STENCIL_ATTACHMENT = ...
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
GL_DRAW_FRAMEBUFFER = ...
GL_DRAW_FRAMEBUFFER_BINDING = ...
GL_DYNAMIC_COPY = ...
GL_DYNAMIC_READ = ...
GL_FLOAT_32_UNSIGNED_INT_24_8_REV = ...
GL_FLOAT_MAT2x3 = ...
GL_FLOAT_MAT2x4 = ...
GL_FLOAT_MAT3x2 = ...
GL_FLOAT_MAT3x4 = ...
GL_FLOAT_MAT4x2 = ...
GL_FLOAT_MAT4x3 = ...
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = ...
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = ...
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = ...
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = ...
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = ...
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = ...
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = ...
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = ...
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = ...
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = ...
GL_FRAMEBUFFER_DEFAULT = ...
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = ...
GL_FRAMEBUFFER_UNDEFINED = ...
GL_GREEN = ...
GL_HALF_FLOAT = ...
GL_INTERLEAVED_ATTRIBS = ...
GL_INT_2_10_10_10_REV = ...
GL_INT_SAMPLER_2D = ...
GL_INT_SAMPLER_2D_ARRAY = ...
GL_INT_SAMPLER_3D = ...
GL_INT_SAMPLER_CUBE = ...
GL_INVALID_INDEX = ...
GL_MAJOR_VERSION = ...
GL_MAP_FLUSH_EXPLICIT_BIT = ...
GL_MAP_INVALIDATE_BUFFER_BIT = ...
GL_MAP_INVALIDATE_RANGE_BIT = ...
GL_MAP_READ_BIT = ...
GL_MAP_UNSYNCHRONIZED_BIT = ...
GL_MAP_WRITE_BIT = ...
GL_MAX = ...
GL_MAX_3D_TEXTURE_SIZE = ...
GL_MAX_ARRAY_TEXTURE_LAYERS = ...
GL_MAX_COLOR_ATTACHMENTS = ...
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = ...
GL_MAX_COMBINED_UNIFORM_BLOCKS = ...
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = ...
GL_MAX_DRAW_BUFFERS = ...
GL_MAX_ELEMENTS_INDICES = ...
GL_MAX_ELEMENTS_VERTICES = ...
GL_MAX_ELEMENT_INDEX = ...
GL_MAX_FRAGMENT_INPUT_COMPONENTS = ...
GL_MAX_FRAGMENT_UNIFORM_BLOCKS = ...
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = ...
GL_MAX_PROGRAM_TEXEL_OFFSET = ...
GL_MAX_SAMPLES = ...
GL_MAX_SERVER_WAIT_TIMEOUT = ...
GL_MAX_TEXTURE_LOD_BIAS = ...
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = ...
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = ...
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = ...
GL_MAX_UNIFORM_BLOCK_SIZE = ...
GL_MAX_UNIFORM_BUFFER_BINDINGS = ...
GL_MAX_VARYING_COMPONENTS = ...
GL_MAX_VERTEX_OUTPUT_COMPONENTS = ...
GL_MAX_VERTEX_UNIFORM_BLOCKS = ...
GL_MAX_VERTEX_UNIFORM_COMPONENTS = ...
GL_MIN = ...
GL_MINOR_VERSION = ...
GL_MIN_PROGRAM_TEXEL_OFFSET = ...
GL_NUM_EXTENSIONS = ...
GL_NUM_PROGRAM_BINARY_FORMATS = ...
GL_NUM_SAMPLE_COUNTS = ...
GL_OBJECT_TYPE = ...
GL_PACK_ROW_LENGTH = ...
GL_PACK_SKIP_PIXELS = ...
GL_PACK_SKIP_ROWS = ...
GL_PIXEL_PACK_BUFFER = ...
GL_PIXEL_PACK_BUFFER_BINDING = ...
GL_PIXEL_UNPACK_BUFFER = ...
GL_PIXEL_UNPACK_BUFFER_BINDING = ...
GL_PRIMITIVE_RESTART_FIXED_INDEX = ...
GL_PROGRAM_BINARY_FORMATS = ...
GL_PROGRAM_BINARY_LENGTH = ...
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = ...
GL_QUERY_RESULT = ...
GL_QUERY_RESULT_AVAILABLE = ...
GL_R11F_G11F_B10F = ...
GL_R16F = ...
GL_R16I = ...
GL_R16UI = ...
GL_R32F = ...
GL_R32I = ...
GL_R32UI = ...
GL_R8 = ...
GL_R8I = ...
GL_R8UI = ...
GL_R8_SNORM = ...
GL_RASTERIZER_DISCARD = ...
GL_READ_BUFFER = ...
GL_READ_FRAMEBUFFER = ...
GL_READ_FRAMEBUFFER_BINDING = ...
GL_RED = ...
GL_RED_INTEGER = ...
GL_RENDERBUFFER_SAMPLES = ...
GL_RG = ...
GL_RG16F = ...
GL_RG16I = ...
GL_RG16UI = ...
GL_RG32F = ...
GL_RG32I = ...
GL_RG32UI = ...
GL_RG8 = ...
GL_RG8I = ...
GL_RG8UI = ...
GL_RG8_SNORM = ...
GL_RGB10_A2 = ...
GL_RGB10_A2UI = ...
GL_RGB16F = ...
GL_RGB16I = ...
GL_RGB16UI = ...
GL_RGB32F = ...
GL_RGB32I = ...
GL_RGB32UI = ...
GL_RGB8 = ...
GL_RGB8I = ...
GL_RGB8UI = ...
GL_RGB8_SNORM = ...
GL_RGB9_E5 = ...
GL_RGBA16F = ...
GL_RGBA16I = ...
GL_RGBA16UI = ...
GL_RGBA32F = ...
GL_RGBA32I = ...
GL_RGBA32UI = ...
GL_RGBA8 = ...
GL_RGBA8I = ...
GL_RGBA8UI = ...
GL_RGBA8_SNORM = ...
GL_RGBA_INTEGER = ...
GL_RGB_INTEGER = ...
GL_RG_INTEGER = ...
GL_SAMPLER_2D_ARRAY = ...
GL_SAMPLER_2D_ARRAY_SHADOW = ...
GL_SAMPLER_2D_SHADOW = ...
GL_SAMPLER_3D = ...
GL_SAMPLER_BINDING = ...
GL_SAMPLER_CUBE_SHADOW = ...
GL_SEPARATE_ATTRIBS = ...
GL_SIGNALED = ...
GL_SIGNED_NORMALIZED = ...
GL_SRGB = ...
GL_SRGB8 = ...
GL_SRGB8_ALPHA8 = ...
GL_STATIC_COPY = ...
GL_STATIC_READ = ...
GL_STENCIL = ...
GL_STREAM_COPY = ...
GL_STREAM_READ = ...
GL_SYNC_CONDITION = ...
GL_SYNC_FENCE = ...
GL_SYNC_FLAGS = ...
GL_SYNC_FLUSH_COMMANDS_BIT = ...
GL_SYNC_GPU_COMMANDS_COMPLETE = ...
GL_SYNC_STATUS = ...
GL_TEXTURE_2D_ARRAY = ...
GL_TEXTURE_3D = ...
GL_TEXTURE_BASE_LEVEL = ...
GL_TEXTURE_BINDING_2D_ARRAY = ...
GL_TEXTURE_BINDING_3D = ...
GL_TEXTURE_COMPARE_FUNC = ...
GL_TEXTURE_COMPARE_MODE = ...
GL_TEXTURE_IMMUTABLE_FORMAT = ...
GL_TEXTURE_IMMUTABLE_LEVELS = ...
GL_TEXTURE_MAX_LEVEL = ...
GL_TEXTURE_MAX_LOD = ...
GL_TEXTURE_MIN_LOD = ...
GL_TEXTURE_SWIZZLE_A = ...
GL_TEXTURE_SWIZZLE_B = ...
GL_TEXTURE_SWIZZLE_G = ...
GL_TEXTURE_SWIZZLE_R = ...
GL_TEXTURE_WRAP_R = ...
GL_TIMEOUT_EXPIRED = ...
GL_TIMEOUT_IGNORED = ...
GL_TRANSFORM_FEEDBACK = ...
GL_TRANSFORM_FEEDBACK_ACTIVE = ...
GL_TRANSFORM_FEEDBACK_BINDING = ...
GL_TRANSFORM_FEEDBACK_BUFFER = ...
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = ...
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = ...
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = ...
GL_TRANSFORM_FEEDBACK_BUFFER_START = ...
GL_TRANSFORM_FEEDBACK_PAUSED = ...
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = ...
GL_TRANSFORM_FEEDBACK_VARYINGS = ...
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = ...
GL_UNIFORM_ARRAY_STRIDE = ...
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = ...
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = ...
GL_UNIFORM_BLOCK_BINDING = ...
GL_UNIFORM_BLOCK_DATA_SIZE = ...
GL_UNIFORM_BLOCK_INDEX = ...
GL_UNIFORM_BLOCK_NAME_LENGTH = ...
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = ...
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = ...
GL_UNIFORM_BUFFER = ...
GL_UNIFORM_BUFFER_BINDING = ...
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = ...
GL_UNIFORM_BUFFER_SIZE = ...
GL_UNIFORM_BUFFER_START = ...
GL_UNIFORM_IS_ROW_MAJOR = ...
GL_UNIFORM_MATRIX_STRIDE = ...
GL_UNIFORM_NAME_LENGTH = ...
GL_UNIFORM_OFFSET = ...
GL_UNIFORM_SIZE = ...
GL_UNIFORM_TYPE = ...
GL_UNPACK_IMAGE_HEIGHT = ...
GL_UNPACK_ROW_LENGTH = ...
GL_UNPACK_SKIP_IMAGES = ...
GL_UNPACK_SKIP_PIXELS = ...
GL_UNPACK_SKIP_ROWS = ...
GL_UNSIGNALED = ...
GL_UNSIGNED_INT_10F_11F_11F_REV = ...
GL_UNSIGNED_INT_24_8 = ...
GL_UNSIGNED_INT_2_10_10_10_REV = ...
GL_UNSIGNED_INT_5_9_9_9_REV = ...
GL_UNSIGNED_INT_SAMPLER_2D = ...
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = ...
GL_UNSIGNED_INT_SAMPLER_3D = ...
GL_UNSIGNED_INT_SAMPLER_CUBE = ...
GL_UNSIGNED_INT_VEC2 = ...
GL_UNSIGNED_INT_VEC3 = ...
GL_UNSIGNED_INT_VEC4 = ...
GL_UNSIGNED_NORMALIZED = ...
GL_VERTEX_ARRAY_BINDING = ...
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = ...
GL_VERTEX_ATTRIB_ARRAY_INTEGER = ...
GL_WAIT_FAILED = ...
@_f
@_p.types(None, _cs.GLenum, _cs.GLuint)
def glBeginQuery(target, id):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glBeginTransformFeedback(primitiveMode):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLuint)
def glBindBufferBase(target, index, buffer):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLuint, _cs.GLintptr, _cs.GLsizeiptr)
def glBindBufferRange(target, index, buffer, offset, size):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glBindSampler(unit, sampler):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint)
def glBindTransformFeedback(target, id):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glBindVertexArray(array):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLbitfield, _cs.GLenum)
def glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLfloat, _cs.GLint)
def glClearBufferfi(buffer, drawbuffer, depth, stencil):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, arrays.GLfloatArray)
def glClearBufferfv(buffer, drawbuffer, value):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, arrays.GLintArray)
def glClearBufferiv(buffer, drawbuffer, value):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, arrays.GLuintArray)
def glClearBufferuiv(buffer, drawbuffer, value):
    ...

@_f
@_p.types(_cs.GLenum, _cs.GLsync, _cs.GLbitfield, _cs.GLuint64)
def glClientWaitSync(sync, flags, timeout):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLenum, _cs.GLsizei, _cs.GLsizei, _cs.GLsizei, _cs.GLint, _cs.GLsizei, ctypes.c_void_p)
def glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei, _cs.GLsizei, _cs.GLenum, _cs.GLsizei, ctypes.c_void_p)
def glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLintptr, _cs.GLintptr, _cs.GLsizeiptr)
def glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei)
def glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDeleteQueries(n, ids):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDeleteSamplers(count, samplers):
    ...

@_f
@_p.types(None, _cs.GLsync)
def glDeleteSync(sync):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDeleteTransformFeedbacks(n, ids):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDeleteVertexArrays(n, arrays):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLsizei, _cs.GLsizei)
def glDrawArraysInstanced(mode, first, count, instancecount):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glDrawBuffers(n, bufs):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, ctypes.c_void_p, _cs.GLsizei)
def glDrawElementsInstanced(mode, count, type, indices, instancecount):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, _cs.GLuint, _cs.GLsizei, _cs.GLenum, ctypes.c_void_p)
def glDrawRangeElements(mode, start, end, count, type, indices):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glEndQuery(target):
    ...

@_f
@_p.types(None)
def glEndTransformFeedback():
    ...

@_f
@_p.types(_cs.GLsync, _cs.GLenum, _cs.GLbitfield)
def glFenceSync(condition, flags):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLintptr, _cs.GLsizeiptr)
def glFlushMappedBufferRange(target, offset, length):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLuint, _cs.GLint, _cs.GLint)
def glFramebufferTextureLayer(target, attachment, texture, level, layer):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenQueries(n, ids):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenSamplers(count, samplers):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenTransformFeedbacks(n, ids):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glGenVertexArrays(n, arrays):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLcharArray)
def glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLuintArray, _cs.GLenum, arrays.GLintArray)
def glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLint64Array)
def glGetBufferParameteri64v(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLvoidpArray)
def glGetBufferPointerv(target, pname, params):
    ...

@_f
@_p.types(_cs.GLint, _cs.GLuint, arrays.GLcharArray)
def glGetFragDataLocation(program, name):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, arrays.GLint64Array)
def glGetInteger64i_v(target, index, data):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLint64Array)
def glGetInteger64v(pname, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLuint, arrays.GLintArray)
def glGetIntegeri_v(target, index, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLenum, _cs.GLsizei, arrays.GLintArray)
def glGetInternalformativ(target, internalformat, pname, bufSize, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLuintArray, ctypes.c_void_p)
def glGetProgramBinary(program, bufSize, length, binaryFormat, binary):
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
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLfloatArray)
def glGetSamplerParameterfv(sampler, pname, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetSamplerParameteriv(sampler, pname, params):
    ...

@_f
@_p.types(arrays.GLubyteArray, _cs.GLenum, _cs.GLuint)
def glGetStringi(name, index):
    ...

@_f
@_p.types(None, _cs.GLsync, _cs.GLenum, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLintArray)
def glGetSynciv(sync, pname, bufSize, length, values):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLsizei, arrays.GLsizeiArray, arrays.GLsizeiArray, arrays.GLuintArray, arrays.GLcharArray)
def glGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name):
    ...

@_f
@_p.types(_cs.GLuint, _cs.GLuint, arrays.GLcharArray)
def glGetUniformBlockIndex(program, uniformBlockName):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, ctypes.POINTER(ctypes.POINTER(_cs.GLchar)), arrays.GLuintArray)
def glGetUniformIndices(program, uniformCount, uniformNames, uniformIndices):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, arrays.GLuintArray)
def glGetUniformuiv(program, location, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glGetVertexAttribIiv(index, pname, params):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLuintArray)
def glGetVertexAttribIuiv(index, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, arrays.GLuintArray)
def glInvalidateFramebuffer(target, numAttachments, attachments):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, arrays.GLuintArray, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei)
def glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsQuery(id):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsSampler(sampler):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLsync)
def glIsSync(sync):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsTransformFeedback(id):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsVertexArray(array):
    ...

@_f
@_p.types(ctypes.c_void_p, _cs.GLenum, _cs.GLintptr, _cs.GLsizeiptr, _cs.GLbitfield)
def glMapBufferRange(target, offset, length, access):
    ...

@_f
@_p.types(None)
def glPauseTransformFeedback():
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, ctypes.c_void_p, _cs.GLsizei)
def glProgramBinary(program, binaryFormat, binary, length):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLint)
def glProgramParameteri(program, pname, value):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glReadBuffer(src):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, _cs.GLsizei, _cs.GLsizei)
def glRenderbufferStorageMultisample(target, samples, internalformat, width, height):
    ...

@_f
@_p.types(None)
def glResumeTransformFeedback():
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLfloat)
def glSamplerParameterf(sampler, pname, param):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLfloatArray)
def glSamplerParameterfv(sampler, pname, param):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, _cs.GLint)
def glSamplerParameteri(sampler, pname, param):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum, arrays.GLintArray)
def glSamplerParameteriv(sampler, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei, _cs.GLsizei, _cs.GLint, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, _cs.GLsizei, _cs.GLsizei)
def glTexStorage2D(target, levels, internalformat, width, height):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, _cs.GLenum, _cs.GLsizei, _cs.GLsizei, _cs.GLsizei)
def glTexStorage3D(target, levels, internalformat, width, height, depth):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei, _cs.GLsizei, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei, ctypes.POINTER(ctypes.POINTER(_cs.GLchar)), _cs.GLenum)
def glTransformFeedbackVaryings(program, count, varyings, bufferMode):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLuint)
def glUniform1ui(location, v0):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glUniform1uiv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLuint, _cs.GLuint)
def glUniform2ui(location, v0, v1):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glUniform2uiv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glUniform3ui(location, v0, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glUniform3uiv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLuint, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glUniform4ui(location, v0, v1, v2, v3):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLsizei, arrays.GLuintArray)
def glUniform4uiv(location, count, value):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding):
    ...

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

@_f
@_p.types(_cs.GLboolean, _cs.GLenum)
def glUnmapBuffer(target):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint)
def glVertexAttribDivisor(index, divisor):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glVertexAttribI4i(index, x, y, z, w):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLintArray)
def glVertexAttribI4iv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glVertexAttribI4ui(index, x, y, z, w):
    ...

@_f
@_p.types(None, _cs.GLuint, arrays.GLuintArray)
def glVertexAttribI4uiv(index, v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLint, _cs.GLenum, _cs.GLsizei, ctypes.c_void_p)
def glVertexAttribIPointer(index, size, type, stride, pointer):
    ...

@_f
@_p.types(None, _cs.GLsync, _cs.GLbitfield, _cs.GLuint64)
def glWaitSync(sync, flags, timeout):
    ...

