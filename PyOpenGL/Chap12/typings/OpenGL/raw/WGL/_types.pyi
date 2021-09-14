"""
This type stub file was generated by pyright.
"""

from ctypes import *
from ctypes import _SimpleCData
from OpenGL import extensions
from OpenGL.raw.GL._types import *
from OpenGL._opaque import opaque_pointer_cls as _opaque_pointer_cls

c_void = ...
class _WGLQuerier(extensions.ExtensionQuerier):
    prefix = ...
    assumed_version = ...
    version_prefix = ...
    def pullVersion(self):
        ...
    
    def pullExtensions(self):
        ...
    


WGLQuerier = ...
INT8 = c_char
PINT8 = c_char_p
INT16 = c_short
PINT16 = POINTER(c_short)
INT32 = c_int
PINT32 = POINTER(c_int)
UINT8 = c_ubyte
PUINT8 = POINTER(c_ubyte)
UINT16 = c_ushort
PUINT16 = POINTER(c_ushort)
UINT32 = c_uint
PUINT32 = POINTER(c_uint)
LONG32 = c_int
PLONG32 = POINTER(c_int)
ULONG32 = c_uint
PULONG32 = POINTER(c_uint)
DWORD32 = c_uint
PDWORD32 = POINTER(c_uint)
INT64 = c_longlong
PINT64 = POINTER(c_longlong)
UINT64 = c_ulonglong
PUINT64 = POINTER(c_ulonglong)
VOID = ...
LPVOID = ...
LPCSTR = c_char_p
CHAR = c_char
BYTE = c_ubyte
WORD = c_ushort
USHORT = c_ushort
UINT = c_uint
INT = c_int
INT_PTR = POINTER(c_int)
BOOL = c_long
LONG = c_long
DWORD = c_ulong
FLOAT = c_float
COLORREF = DWORD
LPCOLORREF = POINTER(DWORD)
class HANDLE(_SimpleCData):
    """Github Issue #8 CTypes shares all references to c_void_p
    
    We have to have a separate type to avoid short-circuiting all
    of the array-handling machinery for real c_void_p arguments.
    """
    _type_ = ...


HGLRC = HANDLE
HDC = HANDLE
PROC = ...
HPBUFFERARB = HANDLE
HPBUFFEREXT = HANDLE
class struct__POINTFLOAT(Structure):
    __slots__ = ...


POINTFLOAT = struct__POINTFLOAT
PPOINTFLOAT = POINTER(struct__POINTFLOAT)
class struct__GLYPHMETRICSFLOAT(Structure):
    __slots__ = ...


GLYPHMETRICSFLOAT = struct__GLYPHMETRICSFLOAT
PGLYPHMETRICSFLOAT = POINTER(struct__GLYPHMETRICSFLOAT)
LPGLYPHMETRICSFLOAT = POINTER(struct__GLYPHMETRICSFLOAT)
class struct_tagLAYERPLANEDESCRIPTOR(Structure):
    __slots__ = ...


LAYERPLANEDESCRIPTOR = struct_tagLAYERPLANEDESCRIPTOR
PLAYERPLANEDESCRIPTOR = POINTER(struct_tagLAYERPLANEDESCRIPTOR)
LPLAYERPLANEDESCRIPTOR = POINTER(struct_tagLAYERPLANEDESCRIPTOR)
class struct__WGLSWAP(Structure):
    __slots__ = ...


WGLSWAP = struct__WGLSWAP
PWGLSWAP = POINTER(struct__WGLSWAP)
LPWGLSWAP = POINTER(struct__WGLSWAP)
class struct_tagRECT(Structure):
    __slots__ = ...


RECT = struct_tagRECT
PRECT = POINTER(struct_tagRECT)
NPRECT = POINTER(struct_tagRECT)
LPRECT = POINTER(struct_tagRECT)
class PIXELFORMATDESCRIPTOR(Structure):
    _fields_ = ...


HENHMETAFILE = _opaque_pointer_cls('HENHMETAFILE')
