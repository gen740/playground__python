"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.EGL import _types as _cs
from OpenGL.raw.EGL._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
EGL_ALPHA_SIZE = ...
EGL_BAD_ACCESS = ...
EGL_BAD_ALLOC = ...
EGL_BAD_ATTRIBUTE = ...
EGL_BAD_CONFIG = ...
EGL_BAD_CONTEXT = ...
EGL_BAD_CURRENT_SURFACE = ...
EGL_BAD_DISPLAY = ...
EGL_BAD_MATCH = ...
EGL_BAD_NATIVE_PIXMAP = ...
EGL_BAD_NATIVE_WINDOW = ...
EGL_BAD_PARAMETER = ...
EGL_BAD_SURFACE = ...
EGL_BLUE_SIZE = ...
EGL_BUFFER_SIZE = ...
EGL_CONFIG_CAVEAT = ...
EGL_CONFIG_ID = ...
EGL_CORE_NATIVE_ENGINE = ...
EGL_DEPTH_SIZE = ...
EGL_DRAW = ...
EGL_EXTENSIONS = ...
EGL_FALSE = ...
EGL_GREEN_SIZE = ...
EGL_HEIGHT = ...
EGL_LARGEST_PBUFFER = ...
EGL_LEVEL = ...
EGL_MAX_PBUFFER_HEIGHT = ...
EGL_MAX_PBUFFER_PIXELS = ...
EGL_MAX_PBUFFER_WIDTH = ...
EGL_NATIVE_RENDERABLE = ...
EGL_NATIVE_VISUAL_ID = ...
EGL_NATIVE_VISUAL_TYPE = ...
EGL_NONE = ...
EGL_NON_CONFORMANT_CONFIG = ...
EGL_NOT_INITIALIZED = ...
EGL_PBUFFER_BIT = ...
EGL_PIXMAP_BIT = ...
EGL_READ = ...
EGL_RED_SIZE = ...
EGL_SAMPLES = ...
EGL_SAMPLE_BUFFERS = ...
EGL_SLOW_CONFIG = ...
EGL_STENCIL_SIZE = ...
EGL_SUCCESS = ...
EGL_SURFACE_TYPE = ...
EGL_TRANSPARENT_BLUE_VALUE = ...
EGL_TRANSPARENT_GREEN_VALUE = ...
EGL_TRANSPARENT_RED_VALUE = ...
EGL_TRANSPARENT_RGB = ...
EGL_TRANSPARENT_TYPE = ...
EGL_TRUE = ...
EGL_VENDOR = ...
EGL_VERSION = ...
EGL_WIDTH = ...
EGL_WINDOW_BIT = ...
@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, arrays.GLintArray, arrays.GLvoidpArray, _cs.EGLint, arrays.GLintArray)
def eglChooseConfig(dpy, attrib_list, configs, config_size, num_config):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLSurface, _cs.EGLNativePixmapType)
def eglCopyBuffers(dpy, surface, target):
    ...

@_f
@_p.types(_cs.EGLContext, _cs.EGLDisplay, _cs.EGLConfig, _cs.EGLContext, arrays.GLintArray)
def eglCreateContext(dpy, config, share_context, attrib_list):
    ...

@_f
@_p.types(_cs.EGLSurface, _cs.EGLDisplay, _cs.EGLConfig, arrays.GLintArray)
def eglCreatePbufferSurface(dpy, config, attrib_list):
    ...

@_f
@_p.types(_cs.EGLSurface, _cs.EGLDisplay, _cs.EGLConfig, _cs.EGLNativePixmapType, arrays.GLintArray)
def eglCreatePixmapSurface(dpy, config, pixmap, attrib_list):
    ...

@_f
@_p.types(_cs.EGLSurface, _cs.EGLDisplay, _cs.EGLConfig, _cs.EGLNativeWindowType, arrays.GLintArray)
def eglCreateWindowSurface(dpy, config, win, attrib_list):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLContext)
def eglDestroyContext(dpy, ctx):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLSurface)
def eglDestroySurface(dpy, surface):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLConfig, _cs.EGLint, arrays.GLintArray)
def eglGetConfigAttrib(dpy, config, attribute, value):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, arrays.GLvoidpArray, _cs.EGLint, arrays.GLintArray)
def eglGetConfigs(dpy, configs, config_size, num_config):
    ...

@_f
@_p.types(_cs.EGLDisplay)
def eglGetCurrentDisplay():
    ...

@_f
@_p.types(_cs.EGLSurface, _cs.EGLint)
def eglGetCurrentSurface(readdraw):
    ...

@_f
@_p.types(_cs.EGLDisplay, _cs.EGLNativeDisplayType)
def eglGetDisplay(display_id):
    ...

@_f
@_p.types(_cs.EGLint)
def eglGetError():
    ...

@_f
@_p.types(ctypes.c_void_p, arrays.GLbyteArray)
def eglGetProcAddress(procname):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, arrays.GLintArray, arrays.GLintArray)
def eglInitialize(dpy, major, minor):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLSurface, _cs.EGLSurface, _cs.EGLContext)
def eglMakeCurrent(dpy, draw, read, ctx):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLContext, _cs.EGLint, arrays.GLintArray)
def eglQueryContext(dpy, ctx, attribute, value):
    ...

@_f
@_p.types(ctypes.c_char_p, _cs.EGLDisplay, _cs.EGLint)
def eglQueryString(dpy, name):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLSurface, _cs.EGLint, arrays.GLintArray)
def eglQuerySurface(dpy, surface, attribute, value):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay, _cs.EGLSurface)
def eglSwapBuffers(dpy, surface):
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLDisplay)
def eglTerminate(dpy):
    ...

@_f
@_p.types(_cs.EGLBoolean)
def eglWaitGL():
    ...

@_f
@_p.types(_cs.EGLBoolean, _cs.EGLint)
def eglWaitNative(engine):
    ...

