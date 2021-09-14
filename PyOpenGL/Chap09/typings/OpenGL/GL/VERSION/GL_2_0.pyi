"""
This type stub file was generated by pyright.
"""

from OpenGL import _configflags
from OpenGL.raw.GL.VERSION.GL_2_0 import *
from OpenGL.lazywrapper import lazy as _lazy

'''OpenGL extension VERSION.GL_2_0

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_2_0 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_2_0.txt
'''
def glInitGl20VERSION():
    '''Return boolean indicating whether this extension is available'''
    ...

glDrawBuffers = ...
glGetActiveAttrib = ...
glGetActiveUniform = ...
glGetAttachedShaders = ...
glGetProgramiv = ...
glGetProgramInfoLog = ...
glGetShaderiv = ...
glGetShaderInfoLog = ...
glGetShaderSource = ...
glGetVertexAttribdv = ...
glGetVertexAttribfv = ...
glGetVertexAttribiv = ...
glGetVertexAttribPointerv = ...
glShaderSource = ...
glUniform1fv = ...
glUniform2fv = ...
glUniform3fv = ...
glUniform4fv = ...
glUniform1iv = ...
glUniform2iv = ...
glUniform3iv = ...
glUniform4iv = ...
glUniformMatrix2fv = ...
glUniformMatrix3fv = ...
glUniformMatrix4fv = ...
glVertexAttrib1dv = ...
glVertexAttrib1fv = ...
glVertexAttrib1sv = ...
glVertexAttrib2dv = ...
glVertexAttrib2fv = ...
glVertexAttrib2sv = ...
glVertexAttrib3dv = ...
glVertexAttrib3fv = ...
glVertexAttrib3sv = ...
glVertexAttrib4Nbv = ...
glVertexAttrib4Niv = ...
glVertexAttrib4Nsv = ...
glVertexAttrib4Nubv = ...
glVertexAttrib4Nuiv = ...
glVertexAttrib4Nusv = ...
glVertexAttrib4bv = ...
glVertexAttrib4dv = ...
glVertexAttrib4fv = ...
glVertexAttrib4iv = ...
glVertexAttrib4sv = ...
glVertexAttrib4ubv = ...
glVertexAttrib4uiv = ...
glVertexAttrib4usv = ...
glVertexAttribPointer = ...
GL_INFO_LOG_LENGTH = ...
glShaderSource = ...
conv = ...
glShaderSource = ...
@_lazy(glGetShaderiv)
def glGetShaderiv(baseOperation, shader, pname, status=...):
    """Retrieve the integer parameter for the given shader

    shader -- shader ID to query
    pname -- parameter name
    status -- pointer to integer to receive status or None to
        return the parameter as an integer value

    returns
        integer if status parameter is None
        status if status parameter is not None
    """
    ...

if _configflags.ERROR_CHECKING:
    ...
if _configflags.ERROR_CHECKING:
    ...
@_lazy(glGetShaderInfoLog)
def glGetShaderInfoLog(baseOperation, obj):
    """Retrieve the shader's error messages as a Python string

    returns string which is '' if no message
    """
    ...

@_lazy(glGetProgramInfoLog)
def glGetProgramInfoLog(baseOperation, obj):
    """Retrieve the shader program's error messages as a Python string

    returns string which is '' if no message
    """
    ...

@_lazy(glGetAttachedShaders)
def glGetAttachedShaders(baseOperation, obj):
    """Retrieve the attached objects as an array of GLhandle instances"""
    ...

@_lazy(glGetShaderSource)
def glGetShaderSource(baseOperation, obj):
    """Retrieve the program/shader's source code as a Python string

    returns string which is '' if no source code
    """
    ...

@_lazy(glGetActiveAttrib)
def glGetActiveAttrib(baseOperation, program, index, bufSize=..., *args):
    """Retrieves information about the attribute variable.

    program -- specifies the program to be queried
    index -- index of the attribute to be queried 
    
    Following parameters are optional:
    
    bufSize -- determines the size of the buffer (limits number of bytes written),
               if not provided, will be GL_ACTIVE_ATTRIBUTE_MAX_LENGTH
    length -- pointer-to-GLsizei that will hold the resulting length of the name
    size -- pointer-to-GLint that will hold the size of the attribute
    type -- pointer-to-GLenum that will hold the type constant of the attribute
    name -- pointer-to-GLchar that will hold the (null-terminated) name string
    
    returns (bytes) name, (int)size, (enum)type
    """
    ...

@_lazy(glGetActiveUniform)
def glGetActiveUniform(baseOperation, program, index, bufSize=..., *args):
    """Retrieve the name, size and type of the uniform of the index in the program
    
    program -- specifies the program to be queried
    index -- index of the uniform to be queried 
    
    Following parameters are optional:
    
    bufSize -- determines the size of the buffer (limits number of bytes written),
               if not provided, will be GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH
    length -- pointer-to-GLsizei that will hold the resulting length of the name
    size -- pointer-to-GLint that will hold the size of the attribute
    type -- pointer-to-GLenum that will hold the type constant of the attribute
    name -- pointer-to-GLchar that will hold the (null-terminated) name string
    
    returns (bytes) name, (int)size, (enum)type
    """
    ...

@_lazy(glGetUniformLocation)
def glGetUniformLocation(baseOperation, program, name):
    """Check that name is a string with a null byte at the end of it"""
    ...

@_lazy(glGetAttribLocation)
def glGetAttribLocation(baseOperation, program, name):
    """Check that name is a string with a null byte at the end of it"""
    ...

@_lazy(glVertexAttribPointer)
def glVertexAttribPointer(baseOperation, index, size, type, normalized, stride, pointer):
    """Set an attribute pointer for a given shader (index)

    index -- the index of the generic vertex to bind, see
        glGetAttribLocation for retrieval of the value,
        note that index is a global variable, not per-shader
    size -- number of basic elements per record, 1,2,3, or 4
    type -- enum constant for data-type
    normalized -- whether to perform int to float
        normalization on integer-type values
    stride -- stride in machine units (bytes) between
        consecutive records, normally used to create
        "interleaved" arrays
    pointer -- data-pointer which provides the data-values,
        normally a vertex-buffer-object or offset into the
        same.

    This implementation stores a copy of the data-pointer
    in the contextdata structure in order to prevent null-
    reference errors in the renderer.
    """
    ...

@_lazy(glDrawBuffers)
def glDrawBuffers(baseOperation, n=..., bufs=...):
    """glDrawBuffers( bufs ) -> bufs

    Wrapper will calculate n from dims of bufs if only
    one argument is provided...
    """
    ...

