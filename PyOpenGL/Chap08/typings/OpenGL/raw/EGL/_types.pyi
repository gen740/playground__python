"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL._opaque import opaque_pointer_cls as _opaque_pointer_cls
from OpenGL import extensions

"""Data-type definitions for EGL/GLES"""
class _EGLQuerier(extensions.ExtensionQuerier):
    prefix = ...
    assumed_version = ...
    version_prefix = ...
    def getDisplay(self):
        """Retrieve the currently-bound, or the default, display"""
        ...
    
    def pullVersion(self):
        ...
    
    def pullExtensions(self):
        ...
    


EGLQuerier = ...
EGLBoolean = ctypes.c_uint32
EGLenum = ctypes.c_uint32
EGLint = c_int = ctypes.c_int32
EGLConfig = _opaque_pointer_cls('EGLConfig')
EGLContext = _opaque_pointer_cls('EGLContext')
EGLDisplay = _opaque_pointer_cls('EGLDisplay')
EGLSurface = _opaque_pointer_cls('EGLSurface')
EGLClientBuffer = _opaque_pointer_cls('EGLClientBuffer')
EGLImageKHR = EGLImage = _opaque_pointer_cls('EGLImageKHR')
EGLDeviceEXT = _opaque_pointer_cls('EGLDeviceEXT')
EGLOutputLayerEXT = _opaque_pointer_cls('EGLOutputLayerEXT')
EGLOutputPortEXT = _opaque_pointer_cls('EGLOutputPortEXT')
EGLScreenMESA = ctypes.c_ulong
EGLModeMESA = ctypes.c_ulong
EGLNativeFileDescriptorKHR = ctypes.c_int
EGLSyncKHR = EGLSyncNV = EGLSync = _opaque_pointer_cls('EGLSync')
EGLTimeKHR = EGLTimeNV = EGLTime = ctypes.c_ulonglong
EGLuint64KHR = EGLuint64NV = ctypes.c_ulonglong
EGLStreamKHR = _opaque_pointer_cls('EGLStream')
EGLsizeiANDROID = ctypes.c_size_t
EGLAttribKHR = EGLAttrib = ctypes.POINTER(ctypes.c_int32)
class EGLClientPixmapHI(ctypes.Structure):
    _fields_ = ...


class wl_display(ctypes.Structure):
    """Opaque structure from Mesa Wayland API"""
    _fields_ = ...


EGLNativeDisplayType = _opaque_pointer_cls('EGLNativeDisplayType')
EGLNativePixmapType = _opaque_pointer_cls('EGLNativePixmapType')
EGLNativeWindowType = _opaque_pointer_cls('EGLNativeWindowType')
NativeDisplayType = EGLNativeDisplayType
NativePixmapType = EGLNativePixmapType
NativeWindowType = EGLNativeWindowType
CALLBACK_TYPE = ...
EGLSetBlobFuncANDROID = ...
EGLGetBlobFuncANDROID = ...
EGL_DEFAULT_DISPLAY = EGLNativeDisplayType()
EGL_NO_CONTEXT = EGLContext()
EGL_NO_DISPLAY = EGLDisplay()
EGL_NO_SURFACE = EGLSurface()
EGL_DONT_CARE = ...
raw_eglQueryString = ...
_VERSION_PREFIX = ...
