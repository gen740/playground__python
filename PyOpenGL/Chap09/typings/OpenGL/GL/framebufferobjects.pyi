"""
This type stub file was generated by pyright.
"""

from OpenGL.GL.ARB.framebuffer_object import *
from OpenGL.GL.EXT.framebuffer_object import *
from OpenGL.GL.EXT.framebuffer_multisample import *
from OpenGL.GL.EXT.framebuffer_blit import *

"""Convenience API for using Frame Buffer Objects"""
glBindFramebuffer = ...
glBindRenderbuffer = ...
glCheckFramebufferStatus = ...
glDeleteFramebuffers = ...
glDeleteRenderbuffers = ...
glFramebufferRenderbuffer = ...
glFramebufferTexture1D = ...
glFramebufferTexture2D = ...
glFramebufferTexture3D = ...
glGenFramebuffers = ...
glGenRenderbuffers = ...
glGenerateMipmap = ...
glGetFramebufferAttachmentParameteriv = ...
glGetRenderbufferParameteriv = ...
glIsFramebuffer = ...
glIsRenderbuffer = ...
glRenderbufferStorage = ...
glBlitFramebuffer = ...
glRenderbufferStorageMultisample = ...
def checkFramebufferStatus():
    """Utility method to check status and raise errors"""
    ...
