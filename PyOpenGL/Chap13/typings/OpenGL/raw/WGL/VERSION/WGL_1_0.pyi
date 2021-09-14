"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import platform as _p
from OpenGL.raw.WGL import _types as _cs
from OpenGL.raw.WGL._types import *

"""
This type stub file was generated by pyright.
"""
_EXTENSION_NAME = ...
WGL_FONT_LINES = ...
WGL_FONT_POLYGONS = ...
WGL_SWAP_MAIN_PLANE = ...
WGL_SWAP_OVERLAY1 = ...
WGL_SWAP_OVERLAY10 = ...
WGL_SWAP_OVERLAY11 = ...
WGL_SWAP_OVERLAY12 = ...
WGL_SWAP_OVERLAY13 = ...
WGL_SWAP_OVERLAY14 = ...
WGL_SWAP_OVERLAY15 = ...
WGL_SWAP_OVERLAY2 = ...
WGL_SWAP_OVERLAY3 = ...
WGL_SWAP_OVERLAY4 = ...
WGL_SWAP_OVERLAY5 = ...
WGL_SWAP_OVERLAY6 = ...
WGL_SWAP_OVERLAY7 = ...
WGL_SWAP_OVERLAY8 = ...
WGL_SWAP_OVERLAY9 = ...
WGL_SWAP_UNDERLAY1 = ...
WGL_SWAP_UNDERLAY10 = ...
WGL_SWAP_UNDERLAY11 = ...
WGL_SWAP_UNDERLAY12 = ...
WGL_SWAP_UNDERLAY13 = ...
WGL_SWAP_UNDERLAY14 = ...
WGL_SWAP_UNDERLAY15 = ...
WGL_SWAP_UNDERLAY2 = ...
WGL_SWAP_UNDERLAY3 = ...
WGL_SWAP_UNDERLAY4 = ...
WGL_SWAP_UNDERLAY5 = ...
WGL_SWAP_UNDERLAY6 = ...
WGL_SWAP_UNDERLAY7 = ...
WGL_SWAP_UNDERLAY8 = ...
WGL_SWAP_UNDERLAY9 = ...
@_f
@_p.types(_cs.c_int, _cs.HDC, ctypes.POINTER(_cs.PIXELFORMATDESCRIPTOR))
def ChoosePixelFormat(hDc, pPfd):
    ...

@_f
@_p.types(_cs.c_int, _cs.HDC, _cs.c_int, _cs.UINT, ctypes.POINTER(_cs.PIXELFORMATDESCRIPTOR))
def DescribePixelFormat(hdc, ipfd, cjpfd, ppfd):
    ...

@_f
@_p.types(_cs.UINT, _cs.HENHMETAFILE, ctypes.POINTER(_cs.PIXELFORMATDESCRIPTOR))
def GetEnhMetaFilePixelFormat(hemf, ppfd):
    ...

@_f
@_p.types(_cs.c_int, _cs.HDC)
def GetPixelFormat(hdc):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.c_int, ctypes.POINTER(_cs.PIXELFORMATDESCRIPTOR))
def SetPixelFormat(hdc, ipfd, ppfd):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC)
def SwapBuffers(hdc):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HGLRC, _cs.HGLRC, _cs.UINT)
def wglCopyContext(hglrcSrc, hglrcDst, mask):
    ...

@_f
@_p.types(_cs.HGLRC, _cs.HDC)
def wglCreateContext(hDc):
    ...

@_f
@_p.types(_cs.HGLRC, _cs.HDC, _cs.c_int)
def wglCreateLayerContext(hDc, level):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HGLRC)
def wglDeleteContext(oldContext):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.c_int, _cs.c_int, _cs.UINT, ctypes.POINTER(_cs.LAYERPLANEDESCRIPTOR))
def wglDescribeLayerPlane(hDc, pixelFormat, layerPlane, nBytes, plpd):
    ...

@_f
@_p.types(_cs.HGLRC)
def wglGetCurrentContext():
    ...

@_f
@_p.types(_cs.HDC)
def wglGetCurrentDC():
    ...

@_f
@_p.types(_cs.c_int, _cs.HDC, _cs.c_int, _cs.c_int, _cs.c_int, ctypes.POINTER(_cs.COLORREF))
def wglGetLayerPaletteEntries(hdc, iLayerPlane, iStart, cEntries, pcr):
    ...

@_f
@_p.types(_cs.PROC, _cs.LPCSTR)
def wglGetProcAddress(lpszProc):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.HGLRC)
def wglMakeCurrent(hDc, newContext):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.c_int, _cs.BOOL)
def wglRealizeLayerPalette(hdc, iLayerPlane, bRealize):
    ...

@_f
@_p.types(_cs.c_int, _cs.HDC, _cs.c_int, _cs.c_int, _cs.c_int, ctypes.POINTER(_cs.COLORREF))
def wglSetLayerPaletteEntries(hdc, iLayerPlane, iStart, cEntries, pcr):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HGLRC, _cs.HGLRC)
def wglShareLists(hrcSrvShare, hrcSrvSource):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.UINT)
def wglSwapLayerBuffers(hdc, fuFlags):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.DWORD, _cs.DWORD, _cs.DWORD)
def wglUseFontBitmaps(hDC, first, count, listBase):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.DWORD, _cs.DWORD, _cs.DWORD)
def wglUseFontBitmapsA(hDC, first, count, listBase):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.DWORD, _cs.DWORD, _cs.DWORD)
def wglUseFontBitmapsW(hDC, first, count, listBase):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.DWORD, _cs.DWORD, _cs.DWORD, _cs.FLOAT, _cs.FLOAT, _cs.c_int, _cs.LPGLYPHMETRICSFLOAT)
def wglUseFontOutlines(hDC, first, count, listBase, deviation, extrusion, format, lpgmf):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.DWORD, _cs.DWORD, _cs.DWORD, _cs.FLOAT, _cs.FLOAT, _cs.c_int, _cs.LPGLYPHMETRICSFLOAT)
def wglUseFontOutlinesA(hDC, first, count, listBase, deviation, extrusion, format, lpgmf):
    ...

@_f
@_p.types(_cs.BOOL, _cs.HDC, _cs.DWORD, _cs.DWORD, _cs.DWORD, _cs.FLOAT, _cs.FLOAT, _cs.c_int, _cs.LPGLYPHMETRICSFLOAT)
def wglUseFontOutlinesW(hDC, first, count, listBase, deviation, extrusion, format, lpgmf):
    ...
