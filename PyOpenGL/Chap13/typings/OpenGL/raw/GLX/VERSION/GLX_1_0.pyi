"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import platform as _p
from OpenGL.raw.GLX import _types as _cs
from OpenGL.raw.GLX._types import *

"""
This type stub file was generated by pyright.
"""
_EXTENSION_NAME = ...
GLX_ACCUM_ALPHA_SIZE = ...
GLX_ACCUM_BLUE_SIZE = ...
GLX_ACCUM_GREEN_SIZE = ...
GLX_ACCUM_RED_SIZE = ...
GLX_ALPHA_SIZE = ...
GLX_AUX_BUFFERS = ...
GLX_BAD_ATTRIBUTE = ...
GLX_BAD_CONTEXT = ...
GLX_BAD_ENUM = ...
GLX_BAD_SCREEN = ...
GLX_BAD_VALUE = ...
GLX_BAD_VISUAL = ...
GLX_BLUE_SIZE = ...
GLX_BUFFER_SIZE = ...
GLX_BufferSwapComplete = ...
GLX_DEPTH_SIZE = ...
GLX_DOUBLEBUFFER = ...
GLX_GREEN_SIZE = ...
GLX_LEVEL = ...
GLX_NO_EXTENSION = ...
GLX_PbufferClobber = ...
GLX_RED_SIZE = ...
GLX_RGBA = ...
GLX_STENCIL_SIZE = ...
GLX_STEREO = ...
GLX_USE_GL = ...
__GLX_NUMBER_EVENTS = ...
@_f
@_p.types(ctypes.POINTER(_cs.XVisualInfo), ctypes.POINTER(_cs.Display), _cs.c_int, ctypes.POINTER(_cs.c_int))
def glXChooseVisual(dpy, screen, attribList):
    ...

@_f
@_p.types(None, ctypes.POINTER(_cs.Display), _cs.GLXContext, _cs.GLXContext, _cs.c_ulong)
def glXCopyContext(dpy, src, dst, mask):
    ...

@_f
@_p.types(_cs.GLXContext, ctypes.POINTER(_cs.Display), ctypes.POINTER(_cs.XVisualInfo), _cs.GLXContext, _cs.Bool)
def glXCreateContext(dpy, vis, shareList, direct):
    ...

@_f
@_p.types(_cs.GLXPixmap, ctypes.POINTER(_cs.Display), ctypes.POINTER(_cs.XVisualInfo), _cs.Pixmap)
def glXCreateGLXPixmap(dpy, visual, pixmap):
    ...

@_f
@_p.types(None, ctypes.POINTER(_cs.Display), _cs.GLXContext)
def glXDestroyContext(dpy, ctx):
    ...

@_f
@_p.types(None, ctypes.POINTER(_cs.Display), _cs.GLXPixmap)
def glXDestroyGLXPixmap(dpy, pixmap):
    ...

@_f
@_p.types(_cs.c_int, ctypes.POINTER(_cs.Display), ctypes.POINTER(_cs.XVisualInfo), _cs.c_int, ctypes.POINTER(_cs.c_int))
def glXGetConfig(dpy, visual, attrib, value):
    ...

@_f
@_p.types(_cs.GLXContext)
def glXGetCurrentContext():
    ...

@_f
@_p.types(_cs.GLXDrawable)
def glXGetCurrentDrawable():
    ...

@_f
@_p.types(_cs.Bool, ctypes.POINTER(_cs.Display), _cs.GLXContext)
def glXIsDirect(dpy, ctx):
    ...

@_f
@_p.types(_cs.Bool, ctypes.POINTER(_cs.Display), _cs.GLXDrawable, _cs.GLXContext)
def glXMakeCurrent(dpy, drawable, ctx):
    ...

@_f
@_p.types(_cs.Bool, ctypes.POINTER(_cs.Display), ctypes.POINTER(_cs.c_int), ctypes.POINTER(_cs.c_int))
def glXQueryExtension(dpy, errorb, event):
    ...

@_f
@_p.types(_cs.Bool, ctypes.POINTER(_cs.Display), ctypes.POINTER(_cs.c_int), ctypes.POINTER(_cs.c_int))
def glXQueryVersion(dpy, maj, min):
    ...

@_f
@_p.types(None, ctypes.POINTER(_cs.Display), _cs.GLXDrawable)
def glXSwapBuffers(dpy, drawable):
    ...

@_f
@_p.types(None, _cs.Font, _cs.c_int, _cs.c_int, _cs.c_int)
def glXUseXFont(font, first, count, list):
    ...

@_f
@_p.types(None)
def glXWaitGL():
    ...

@_f
@_p.types(None)
def glXWaitX():
    ...

