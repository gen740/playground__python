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
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER = ...
GL_COMPUTE_SHADER = ...
GL_COMPUTE_SHADER_BIT = ...
GL_COMPUTE_WORK_GROUP_SIZE = ...
GL_DISPATCH_INDIRECT_BUFFER = ...
GL_DISPATCH_INDIRECT_BUFFER_BINDING = ...
GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = ...
GL_MAX_COMPUTE_ATOMIC_COUNTERS = ...
GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = ...
GL_MAX_COMPUTE_IMAGE_UNIFORMS = ...
GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = ...
GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = ...
GL_MAX_COMPUTE_UNIFORM_BLOCKS = ...
GL_MAX_COMPUTE_UNIFORM_COMPONENTS = ...
GL_MAX_COMPUTE_WORK_GROUP_COUNT = ...
GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS = ...
GL_MAX_COMPUTE_WORK_GROUP_SIZE = ...
GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER = ...
@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glDispatchCompute(num_groups_x, num_groups_y, num_groups_z):
    ...

@_f
@_p.types(None, _cs.GLintptr)
def glDispatchComputeIndirect(indirect):
    ...

