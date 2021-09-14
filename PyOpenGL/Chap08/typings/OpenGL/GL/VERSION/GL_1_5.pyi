"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.VERSION.GL_1_5 import *
from OpenGL.lazywrapper import lazy as _lazy

"""
This type stub file was generated by pyright.
"""
def glInitGl15VERSION():
    '''Return boolean indicating whether this extension is available'''
    ...

glGenQueries = ...
glDeleteQueries = ...
glGetQueryiv = ...
glGetQueryObjectiv = ...
glGetQueryObjectuiv = ...
glDeleteBuffers = ...
glGenBuffers = ...
glBufferData = ...
glBufferSubData = ...
glGetBufferSubData = ...
glGetBufferParameteriv = ...
glGetBufferPointerv = ...
@_lazy(glBufferData)
def glBufferData(baseOperation, target, size, data=..., usage=...):
    """Copy given data into the currently bound vertex-buffer-data object

    target -- the symbolic constant indicating which buffer type is intended
    size -- if provided, the count-in-bytes of the array
    data -- data-pointer to be used, may be None to initialize without
        copying over a data-set
    usage -- hint to the driver as to how to set up access to the buffer

    Note: parameter "size" can be omitted, which makes the signature
        glBufferData( target, data, usage )
    instead of:
        glBufferData( target, size, data, usage )
    """
    ...

@_lazy(glBufferSubData)
def glBufferSubData(baseOperation, target, offset, size=..., data=...):
    """Copy subset of data into the currently bound vertex-buffer-data object

    target -- the symbolic constant indicating which buffer type is intended
    offset -- offset from beginning of buffer at which to copy bytes
    size -- the count-in-bytes of the array (if an int/long), if None,
        calculate size from data, if an array and data is None, use as
        data (i.e. the parameter can be omitted and calculated)
    data -- data-pointer to be used, may be None to initialize without
        copying over a data-set

    Note that if size is not an int/long it is considered to be data
    *iff* data is None
    """
    ...

@_lazy(glGetBufferPointerv)
def glGetBufferPointerv(baseOperation, target, pname, params=...):
    """Retrieve a ctypes pointer to buffer's data"""
    ...

@_lazy(glDeleteQueries)
def glDeleteQueries(baseOperation, n, ids=...):
    ...

@_lazy(glGenQueries)
def glGenQueries(baseOperation, n, ids=...):
    """Generate n queries, if ids is None, is allocated

    returns array of ids
    """
    ...

