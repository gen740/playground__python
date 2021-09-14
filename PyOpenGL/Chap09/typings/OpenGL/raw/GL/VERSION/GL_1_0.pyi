"""
This type stub file was generated by pyright.
"""

import ctypes
from OpenGL import arrays, platform as _p
from OpenGL.raw.GL import _types as _cs
from OpenGL.raw.GL._types import *

'''Autogenerated by xml_generate script, do not edit!'''
_EXTENSION_NAME = ...
GL_2D = ...
GL_2_BYTES = ...
GL_3D = ...
GL_3D_COLOR = ...
GL_3D_COLOR_TEXTURE = ...
GL_3_BYTES = ...
GL_4D_COLOR_TEXTURE = ...
GL_4_BYTES = ...
GL_ACCUM = ...
GL_ACCUM_ALPHA_BITS = ...
GL_ACCUM_BLUE_BITS = ...
GL_ACCUM_BUFFER_BIT = ...
GL_ACCUM_CLEAR_VALUE = ...
GL_ACCUM_GREEN_BITS = ...
GL_ACCUM_RED_BITS = ...
GL_ADD = ...
GL_ALL_ATTRIB_BITS = ...
GL_ALPHA = ...
GL_ALPHA_BIAS = ...
GL_ALPHA_BITS = ...
GL_ALPHA_SCALE = ...
GL_ALPHA_TEST = ...
GL_ALPHA_TEST_FUNC = ...
GL_ALPHA_TEST_REF = ...
GL_ALWAYS = ...
GL_AMBIENT = ...
GL_AMBIENT_AND_DIFFUSE = ...
GL_AND = ...
GL_AND_INVERTED = ...
GL_AND_REVERSE = ...
GL_ATTRIB_STACK_DEPTH = ...
GL_AUTO_NORMAL = ...
GL_AUX0 = ...
GL_AUX1 = ...
GL_AUX2 = ...
GL_AUX3 = ...
GL_AUX_BUFFERS = ...
GL_BACK = ...
GL_BACK_LEFT = ...
GL_BACK_RIGHT = ...
GL_BITMAP = ...
GL_BITMAP_TOKEN = ...
GL_BLEND = ...
GL_BLEND_DST = ...
GL_BLEND_SRC = ...
GL_BLUE = ...
GL_BLUE_BIAS = ...
GL_BLUE_BITS = ...
GL_BLUE_SCALE = ...
GL_BYTE = ...
GL_CCW = ...
GL_CLAMP = ...
GL_CLEAR = ...
GL_CLIP_PLANE0 = ...
GL_CLIP_PLANE1 = ...
GL_CLIP_PLANE2 = ...
GL_CLIP_PLANE3 = ...
GL_CLIP_PLANE4 = ...
GL_CLIP_PLANE5 = ...
GL_COEFF = ...
GL_COLOR = ...
GL_COLOR_BUFFER_BIT = ...
GL_COLOR_CLEAR_VALUE = ...
GL_COLOR_INDEX = ...
GL_COLOR_INDEXES = ...
GL_COLOR_MATERIAL = ...
GL_COLOR_MATERIAL_FACE = ...
GL_COLOR_MATERIAL_PARAMETER = ...
GL_COLOR_WRITEMASK = ...
GL_COMPILE = ...
GL_COMPILE_AND_EXECUTE = ...
GL_CONSTANT_ATTENUATION = ...
GL_COPY = ...
GL_COPY_INVERTED = ...
GL_COPY_PIXEL_TOKEN = ...
GL_CULL_FACE = ...
GL_CULL_FACE_MODE = ...
GL_CURRENT_BIT = ...
GL_CURRENT_COLOR = ...
GL_CURRENT_INDEX = ...
GL_CURRENT_NORMAL = ...
GL_CURRENT_RASTER_COLOR = ...
GL_CURRENT_RASTER_DISTANCE = ...
GL_CURRENT_RASTER_INDEX = ...
GL_CURRENT_RASTER_POSITION = ...
GL_CURRENT_RASTER_POSITION_VALID = ...
GL_CURRENT_RASTER_TEXTURE_COORDS = ...
GL_CURRENT_TEXTURE_COORDS = ...
GL_CW = ...
GL_DECAL = ...
GL_DECR = ...
GL_DEPTH = ...
GL_DEPTH_BIAS = ...
GL_DEPTH_BITS = ...
GL_DEPTH_BUFFER_BIT = ...
GL_DEPTH_CLEAR_VALUE = ...
GL_DEPTH_COMPONENT = ...
GL_DEPTH_FUNC = ...
GL_DEPTH_RANGE = ...
GL_DEPTH_SCALE = ...
GL_DEPTH_TEST = ...
GL_DEPTH_WRITEMASK = ...
GL_DIFFUSE = ...
GL_DITHER = ...
GL_DOMAIN = ...
GL_DONT_CARE = ...
GL_DOUBLEBUFFER = ...
GL_DRAW_BUFFER = ...
GL_DRAW_PIXEL_TOKEN = ...
GL_DST_ALPHA = ...
GL_DST_COLOR = ...
GL_EDGE_FLAG = ...
GL_EMISSION = ...
GL_ENABLE_BIT = ...
GL_EQUAL = ...
GL_EQUIV = ...
GL_EVAL_BIT = ...
GL_EXP = ...
GL_EXP2 = ...
GL_EXTENSIONS = ...
GL_EYE_LINEAR = ...
GL_EYE_PLANE = ...
GL_FALSE = ...
GL_FASTEST = ...
GL_FEEDBACK = ...
GL_FILL = ...
GL_FLAT = ...
GL_FLOAT = ...
GL_FOG = ...
GL_FOG_BIT = ...
GL_FOG_COLOR = ...
GL_FOG_DENSITY = ...
GL_FOG_END = ...
GL_FOG_HINT = ...
GL_FOG_INDEX = ...
GL_FOG_MODE = ...
GL_FOG_START = ...
GL_FRONT = ...
GL_FRONT_AND_BACK = ...
GL_FRONT_FACE = ...
GL_FRONT_LEFT = ...
GL_FRONT_RIGHT = ...
GL_GEQUAL = ...
GL_GREATER = ...
GL_GREEN = ...
GL_GREEN_BIAS = ...
GL_GREEN_BITS = ...
GL_GREEN_SCALE = ...
GL_HINT_BIT = ...
GL_INCR = ...
GL_INDEX_BITS = ...
GL_INDEX_CLEAR_VALUE = ...
GL_INDEX_MODE = ...
GL_INDEX_OFFSET = ...
GL_INDEX_SHIFT = ...
GL_INDEX_WRITEMASK = ...
GL_INT = ...
GL_INVALID_ENUM = ...
GL_INVALID_OPERATION = ...
GL_INVALID_VALUE = ...
GL_INVERT = ...
GL_KEEP = ...
GL_LEFT = ...
GL_LEQUAL = ...
GL_LESS = ...
GL_LIGHT0 = ...
GL_LIGHT1 = ...
GL_LIGHT2 = ...
GL_LIGHT3 = ...
GL_LIGHT4 = ...
GL_LIGHT5 = ...
GL_LIGHT6 = ...
GL_LIGHT7 = ...
GL_LIGHTING = ...
GL_LIGHTING_BIT = ...
GL_LIGHT_MODEL_AMBIENT = ...
GL_LIGHT_MODEL_LOCAL_VIEWER = ...
GL_LIGHT_MODEL_TWO_SIDE = ...
GL_LINE = ...
GL_LINEAR = ...
GL_LINEAR_ATTENUATION = ...
GL_LINEAR_MIPMAP_LINEAR = ...
GL_LINEAR_MIPMAP_NEAREST = ...
GL_LINES = ...
GL_LINE_BIT = ...
GL_LINE_LOOP = ...
GL_LINE_RESET_TOKEN = ...
GL_LINE_SMOOTH = ...
GL_LINE_SMOOTH_HINT = ...
GL_LINE_STIPPLE = ...
GL_LINE_STIPPLE_PATTERN = ...
GL_LINE_STIPPLE_REPEAT = ...
GL_LINE_STRIP = ...
GL_LINE_TOKEN = ...
GL_LINE_WIDTH = ...
GL_LINE_WIDTH_GRANULARITY = ...
GL_LINE_WIDTH_RANGE = ...
GL_LIST_BASE = ...
GL_LIST_BIT = ...
GL_LIST_INDEX = ...
GL_LIST_MODE = ...
GL_LOAD = ...
GL_LOGIC_OP = ...
GL_LOGIC_OP_MODE = ...
GL_LUMINANCE = ...
GL_LUMINANCE_ALPHA = ...
GL_MAP1_COLOR_4 = ...
GL_MAP1_GRID_DOMAIN = ...
GL_MAP1_GRID_SEGMENTS = ...
GL_MAP1_INDEX = ...
GL_MAP1_NORMAL = ...
GL_MAP1_TEXTURE_COORD_1 = ...
GL_MAP1_TEXTURE_COORD_2 = ...
GL_MAP1_TEXTURE_COORD_3 = ...
GL_MAP1_TEXTURE_COORD_4 = ...
GL_MAP1_VERTEX_3 = ...
GL_MAP1_VERTEX_4 = ...
GL_MAP2_COLOR_4 = ...
GL_MAP2_GRID_DOMAIN = ...
GL_MAP2_GRID_SEGMENTS = ...
GL_MAP2_INDEX = ...
GL_MAP2_NORMAL = ...
GL_MAP2_TEXTURE_COORD_1 = ...
GL_MAP2_TEXTURE_COORD_2 = ...
GL_MAP2_TEXTURE_COORD_3 = ...
GL_MAP2_TEXTURE_COORD_4 = ...
GL_MAP2_VERTEX_3 = ...
GL_MAP2_VERTEX_4 = ...
GL_MAP_COLOR = ...
GL_MAP_STENCIL = ...
GL_MATRIX_MODE = ...
GL_MAX_ATTRIB_STACK_DEPTH = ...
GL_MAX_CLIP_PLANES = ...
GL_MAX_EVAL_ORDER = ...
GL_MAX_LIGHTS = ...
GL_MAX_LIST_NESTING = ...
GL_MAX_MODELVIEW_STACK_DEPTH = ...
GL_MAX_NAME_STACK_DEPTH = ...
GL_MAX_PIXEL_MAP_TABLE = ...
GL_MAX_PROJECTION_STACK_DEPTH = ...
GL_MAX_TEXTURE_SIZE = ...
GL_MAX_TEXTURE_STACK_DEPTH = ...
GL_MAX_VIEWPORT_DIMS = ...
GL_MODELVIEW = ...
GL_MODELVIEW_MATRIX = ...
GL_MODELVIEW_STACK_DEPTH = ...
GL_MODULATE = ...
GL_MULT = ...
GL_NAME_STACK_DEPTH = ...
GL_NAND = ...
GL_NEAREST = ...
GL_NEAREST_MIPMAP_LINEAR = ...
GL_NEAREST_MIPMAP_NEAREST = ...
GL_NEVER = ...
GL_NICEST = ...
GL_NONE = ...
GL_NOOP = ...
GL_NOR = ...
GL_NORMALIZE = ...
GL_NOTEQUAL = ...
GL_NO_ERROR = ...
GL_OBJECT_LINEAR = ...
GL_OBJECT_PLANE = ...
GL_ONE = ...
GL_ONE_MINUS_DST_ALPHA = ...
GL_ONE_MINUS_DST_COLOR = ...
GL_ONE_MINUS_SRC_ALPHA = ...
GL_ONE_MINUS_SRC_COLOR = ...
GL_OR = ...
GL_ORDER = ...
GL_OR_INVERTED = ...
GL_OR_REVERSE = ...
GL_OUT_OF_MEMORY = ...
GL_PACK_ALIGNMENT = ...
GL_PACK_LSB_FIRST = ...
GL_PACK_ROW_LENGTH = ...
GL_PACK_SKIP_PIXELS = ...
GL_PACK_SKIP_ROWS = ...
GL_PACK_SWAP_BYTES = ...
GL_PASS_THROUGH_TOKEN = ...
GL_PERSPECTIVE_CORRECTION_HINT = ...
GL_PIXEL_MAP_A_TO_A = ...
GL_PIXEL_MAP_A_TO_A_SIZE = ...
GL_PIXEL_MAP_B_TO_B = ...
GL_PIXEL_MAP_B_TO_B_SIZE = ...
GL_PIXEL_MAP_G_TO_G = ...
GL_PIXEL_MAP_G_TO_G_SIZE = ...
GL_PIXEL_MAP_I_TO_A = ...
GL_PIXEL_MAP_I_TO_A_SIZE = ...
GL_PIXEL_MAP_I_TO_B = ...
GL_PIXEL_MAP_I_TO_B_SIZE = ...
GL_PIXEL_MAP_I_TO_G = ...
GL_PIXEL_MAP_I_TO_G_SIZE = ...
GL_PIXEL_MAP_I_TO_I = ...
GL_PIXEL_MAP_I_TO_I_SIZE = ...
GL_PIXEL_MAP_I_TO_R = ...
GL_PIXEL_MAP_I_TO_R_SIZE = ...
GL_PIXEL_MAP_R_TO_R = ...
GL_PIXEL_MAP_R_TO_R_SIZE = ...
GL_PIXEL_MAP_S_TO_S = ...
GL_PIXEL_MAP_S_TO_S_SIZE = ...
GL_PIXEL_MODE_BIT = ...
GL_POINT = ...
GL_POINTS = ...
GL_POINT_BIT = ...
GL_POINT_SIZE = ...
GL_POINT_SIZE_GRANULARITY = ...
GL_POINT_SIZE_RANGE = ...
GL_POINT_SMOOTH = ...
GL_POINT_SMOOTH_HINT = ...
GL_POINT_TOKEN = ...
GL_POLYGON = ...
GL_POLYGON_BIT = ...
GL_POLYGON_MODE = ...
GL_POLYGON_SMOOTH = ...
GL_POLYGON_SMOOTH_HINT = ...
GL_POLYGON_STIPPLE = ...
GL_POLYGON_STIPPLE_BIT = ...
GL_POLYGON_TOKEN = ...
GL_POSITION = ...
GL_PROJECTION = ...
GL_PROJECTION_MATRIX = ...
GL_PROJECTION_STACK_DEPTH = ...
GL_Q = ...
GL_QUADRATIC_ATTENUATION = ...
GL_QUADS = ...
GL_QUAD_STRIP = ...
GL_R = ...
GL_READ_BUFFER = ...
GL_RED = ...
GL_RED_BIAS = ...
GL_RED_BITS = ...
GL_RED_SCALE = ...
GL_RENDER = ...
GL_RENDERER = ...
GL_RENDER_MODE = ...
GL_REPEAT = ...
GL_REPLACE = ...
GL_RETURN = ...
GL_RGB = ...
GL_RGBA = ...
GL_RGBA_MODE = ...
GL_RIGHT = ...
GL_S = ...
GL_SCISSOR_BIT = ...
GL_SCISSOR_BOX = ...
GL_SCISSOR_TEST = ...
GL_SELECT = ...
GL_SET = ...
GL_SHADE_MODEL = ...
GL_SHININESS = ...
GL_SHORT = ...
GL_SMOOTH = ...
GL_SPECULAR = ...
GL_SPHERE_MAP = ...
GL_SPOT_CUTOFF = ...
GL_SPOT_DIRECTION = ...
GL_SPOT_EXPONENT = ...
GL_SRC_ALPHA = ...
GL_SRC_ALPHA_SATURATE = ...
GL_SRC_COLOR = ...
GL_STACK_OVERFLOW = ...
GL_STACK_UNDERFLOW = ...
GL_STENCIL = ...
GL_STENCIL_BITS = ...
GL_STENCIL_BUFFER_BIT = ...
GL_STENCIL_CLEAR_VALUE = ...
GL_STENCIL_FAIL = ...
GL_STENCIL_FUNC = ...
GL_STENCIL_INDEX = ...
GL_STENCIL_PASS_DEPTH_FAIL = ...
GL_STENCIL_PASS_DEPTH_PASS = ...
GL_STENCIL_REF = ...
GL_STENCIL_TEST = ...
GL_STENCIL_VALUE_MASK = ...
GL_STENCIL_WRITEMASK = ...
GL_STEREO = ...
GL_SUBPIXEL_BITS = ...
GL_T = ...
GL_TEXTURE = ...
GL_TEXTURE_1D = ...
GL_TEXTURE_2D = ...
GL_TEXTURE_BIT = ...
GL_TEXTURE_BORDER = ...
GL_TEXTURE_BORDER_COLOR = ...
GL_TEXTURE_COMPONENTS = ...
GL_TEXTURE_ENV = ...
GL_TEXTURE_ENV_COLOR = ...
GL_TEXTURE_ENV_MODE = ...
GL_TEXTURE_GEN_MODE = ...
GL_TEXTURE_GEN_Q = ...
GL_TEXTURE_GEN_R = ...
GL_TEXTURE_GEN_S = ...
GL_TEXTURE_GEN_T = ...
GL_TEXTURE_HEIGHT = ...
GL_TEXTURE_MAG_FILTER = ...
GL_TEXTURE_MATRIX = ...
GL_TEXTURE_MIN_FILTER = ...
GL_TEXTURE_STACK_DEPTH = ...
GL_TEXTURE_WIDTH = ...
GL_TEXTURE_WRAP_S = ...
GL_TEXTURE_WRAP_T = ...
GL_TRANSFORM_BIT = ...
GL_TRIANGLES = ...
GL_TRIANGLE_FAN = ...
GL_TRIANGLE_STRIP = ...
GL_TRUE = ...
GL_UNPACK_ALIGNMENT = ...
GL_UNPACK_LSB_FIRST = ...
GL_UNPACK_ROW_LENGTH = ...
GL_UNPACK_SKIP_PIXELS = ...
GL_UNPACK_SKIP_ROWS = ...
GL_UNPACK_SWAP_BYTES = ...
GL_UNSIGNED_BYTE = ...
GL_UNSIGNED_INT = ...
GL_UNSIGNED_SHORT = ...
GL_VENDOR = ...
GL_VERSION = ...
GL_VIEWPORT = ...
GL_VIEWPORT_BIT = ...
GL_XOR = ...
GL_ZERO = ...
GL_ZOOM_X = ...
GL_ZOOM_Y = ...
@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat)
def glAccum(op, value):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat)
def glAlphaFunc(func, ref):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glBegin(mode):
    ...

@_f
@_p.types(None, _cs.GLsizei, _cs.GLsizei, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, arrays.GLubyteArray)
def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum)
def glBlendFunc(sfactor, dfactor):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glCallList(list):
    ...

@_f
@_p.types(None, _cs.GLsizei, _cs.GLenum, ctypes.c_void_p)
def glCallLists(n, type, lists):
    ...

@_f
@_p.types(None, _cs.GLbitfield)
def glClear(mask):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glClearAccum(red, green, blue, alpha):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glClearColor(red, green, blue, alpha):
    ...

@_f
@_p.types(None, _cs.GLdouble)
def glClearDepth(depth):
    ...

@_f
@_p.types(None, _cs.GLfloat)
def glClearIndex(c):
    ...

@_f
@_p.types(None, _cs.GLint)
def glClearStencil(s):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLdoubleArray)
def glClipPlane(plane, equation):
    ...

@_f
@_p.types(None, _cs.GLbyte, _cs.GLbyte, _cs.GLbyte)
def glColor3b(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLbyteArray)
def glColor3bv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glColor3d(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glColor3dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glColor3f(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glColor3fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint)
def glColor3i(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glColor3iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glColor3s(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glColor3sv(v):
    ...

@_f
@_p.types(None, _cs.GLubyte, _cs.GLubyte, _cs.GLubyte)
def glColor3ub(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLubyteArray)
def glColor3ubv(v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glColor3ui(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLuintArray)
def glColor3uiv(v):
    ...

@_f
@_p.types(None, _cs.GLushort, _cs.GLushort, _cs.GLushort)
def glColor3us(red, green, blue):
    ...

@_f
@_p.types(None, arrays.GLushortArray)
def glColor3usv(v):
    ...

@_f
@_p.types(None, _cs.GLbyte, _cs.GLbyte, _cs.GLbyte, _cs.GLbyte)
def glColor4b(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLbyteArray)
def glColor4bv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glColor4d(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glColor4dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glColor4f(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glColor4fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glColor4i(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glColor4iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glColor4s(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glColor4sv(v):
    ...

@_f
@_p.types(None, _cs.GLubyte, _cs.GLubyte, _cs.GLubyte, _cs.GLubyte)
def glColor4ub(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLubyteArray)
def glColor4ubv(v):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLuint, _cs.GLuint, _cs.GLuint)
def glColor4ui(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLuintArray)
def glColor4uiv(v):
    ...

@_f
@_p.types(None, _cs.GLushort, _cs.GLushort, _cs.GLushort, _cs.GLushort)
def glColor4us(red, green, blue, alpha):
    ...

@_f
@_p.types(None, arrays.GLushortArray)
def glColor4usv(v):
    ...

@_f
@_p.types(None, _cs.GLboolean, _cs.GLboolean, _cs.GLboolean, _cs.GLboolean)
def glColorMask(red, green, blue, alpha):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum)
def glColorMaterial(face, mode):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei, _cs.GLenum)
def glCopyPixels(x, y, width, height, type):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glCullFace(mode):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLsizei)
def glDeleteLists(list, range):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glDepthFunc(func):
    ...

@_f
@_p.types(None, _cs.GLboolean)
def glDepthMask(flag):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble)
def glDepthRange(n, f):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glDisable(cap):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glDrawBuffer(buf):
    ...

@_f
@_p.types(None, _cs.GLsizei, _cs.GLsizei, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glDrawPixels(width, height, format, type, pixels):
    ...

@_f
@_p.types(None, _cs.GLboolean)
def glEdgeFlag(flag):
    ...

@_f
@_p.types(None, arrays.GLbooleanArray)
def glEdgeFlagv(flag):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glEnable(cap):
    ...

@_f
@_p.types(None)
def glEnd():
    ...

@_f
@_p.types(None)
def glEndList():
    ...

@_f
@_p.types(None, _cs.GLdouble)
def glEvalCoord1d(u):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glEvalCoord1dv(u):
    ...

@_f
@_p.types(None, _cs.GLfloat)
def glEvalCoord1f(u):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glEvalCoord1fv(u):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble)
def glEvalCoord2d(u, v):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glEvalCoord2dv(u):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat)
def glEvalCoord2f(u, v):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glEvalCoord2fv(u):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint)
def glEvalMesh1(mode, i1, i2):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glEvalMesh2(mode, i1, i2, j1, j2):
    ...

@_f
@_p.types(None, _cs.GLint)
def glEvalPoint1(i):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint)
def glEvalPoint2(i, j):
    ...

@_f
@_p.types(None, _cs.GLsizei, _cs.GLenum, arrays.GLfloatArray)
def glFeedbackBuffer(size, type, buffer):
    ...

@_f
@_p.types(None)
def glFinish():
    ...

@_f
@_p.types(None)
def glFlush():
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat)
def glFogf(pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLfloatArray)
def glFogfv(pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint)
def glFogi(pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLintArray)
def glFogiv(pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glFrontFace(mode):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glFrustum(left, right, bottom, top, zNear, zFar):
    ...

@_f
@_p.types(_cs.GLuint, _cs.GLsizei)
def glGenLists(range):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLbooleanArray)
def glGetBooleanv(pname, data):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLdoubleArray)
def glGetClipPlane(plane, equation):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLdoubleArray)
def glGetDoublev(pname, data):
    ...

@_f
@_p.types(_cs.GLenum)
def glGetError():
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLfloatArray)
def glGetFloatv(pname, data):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLintArray)
def glGetIntegerv(pname, data):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glGetLightfv(light, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetLightiv(light, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLdoubleArray)
def glGetMapdv(target, query, v):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glGetMapfv(target, query, v):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetMapiv(target, query, v):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glGetMaterialfv(face, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetMaterialiv(face, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLfloatArray)
def glGetPixelMapfv(map, values):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLuintArray)
def glGetPixelMapuiv(map, values):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLushortArray)
def glGetPixelMapusv(map, values):
    ...

@_f
@_p.types(None, arrays.GLubyteArray)
def glGetPolygonStipple(mask):
    ...

@_f
@_p.types(arrays.GLubyteArray, _cs.GLenum)
def glGetString(name):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glGetTexEnvfv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetTexEnviv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLdoubleArray)
def glGetTexGendv(coord, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glGetTexGenfv(coord, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetTexGeniv(coord, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glGetTexImage(target, level, format, type, pixels):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLenum, arrays.GLfloatArray)
def glGetTexLevelParameterfv(target, level, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLenum, arrays.GLintArray)
def glGetTexLevelParameteriv(target, level, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glGetTexParameterfv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glGetTexParameteriv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum)
def glHint(target, mode):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glIndexMask(mask):
    ...

@_f
@_p.types(None, _cs.GLdouble)
def glIndexd(c):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glIndexdv(c):
    ...

@_f
@_p.types(None, _cs.GLfloat)
def glIndexf(c):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glIndexfv(c):
    ...

@_f
@_p.types(None, _cs.GLint)
def glIndexi(c):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glIndexiv(c):
    ...

@_f
@_p.types(None, _cs.GLshort)
def glIndexs(c):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glIndexsv(c):
    ...

@_f
@_p.types(None)
def glInitNames():
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLenum)
def glIsEnabled(cap):
    ...

@_f
@_p.types(_cs.GLboolean, _cs.GLuint)
def glIsList(list):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat)
def glLightModelf(pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLfloatArray)
def glLightModelfv(pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint)
def glLightModeli(pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, arrays.GLintArray)
def glLightModeliv(pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLfloat)
def glLightf(light, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glLightfv(light, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLint)
def glLighti(light, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glLightiv(light, pname, params):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLushort)
def glLineStipple(factor, pattern):
    ...

@_f
@_p.types(None, _cs.GLfloat)
def glLineWidth(width):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glListBase(base):
    ...

@_f
@_p.types(None)
def glLoadIdentity():
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glLoadMatrixd(m):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glLoadMatrixf(m):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glLoadName(name):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glLogicOp(opcode):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLdouble, _cs.GLdouble, _cs.GLint, _cs.GLint, arrays.GLdoubleArray)
def glMap1d(target, u1, u2, stride, order, points):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat, _cs.GLfloat, _cs.GLint, _cs.GLint, arrays.GLfloatArray)
def glMap1f(target, u1, u2, stride, order, points):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLdouble, _cs.GLdouble, _cs.GLint, _cs.GLint, _cs.GLdouble, _cs.GLdouble, _cs.GLint, _cs.GLint, arrays.GLdoubleArray)
def glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat, _cs.GLfloat, _cs.GLint, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLint, _cs.GLint, arrays.GLfloatArray)
def glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLdouble, _cs.GLdouble)
def glMapGrid1d(un, u1, u2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat)
def glMapGrid1f(un, u1, u2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLdouble, _cs.GLdouble, _cs.GLint, _cs.GLdouble, _cs.GLdouble)
def glMapGrid2d(un, u1, u2, vn, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLfloat, _cs.GLfloat, _cs.GLint, _cs.GLfloat, _cs.GLfloat)
def glMapGrid2f(un, u1, u2, vn, v1, v2):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLfloat)
def glMaterialf(face, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glMaterialfv(face, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLint)
def glMateriali(face, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glMaterialiv(face, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glMatrixMode(mode):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glMultMatrixd(m):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glMultMatrixf(m):
    ...

@_f
@_p.types(None, _cs.GLuint, _cs.GLenum)
def glNewList(list, mode):
    ...

@_f
@_p.types(None, _cs.GLbyte, _cs.GLbyte, _cs.GLbyte)
def glNormal3b(nx, ny, nz):
    ...

@_f
@_p.types(None, arrays.GLbyteArray)
def glNormal3bv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glNormal3d(nx, ny, nz):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glNormal3dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glNormal3f(nx, ny, nz):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glNormal3fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint)
def glNormal3i(nx, ny, nz):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glNormal3iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glNormal3s(nx, ny, nz):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glNormal3sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glOrtho(left, right, bottom, top, zNear, zFar):
    ...

@_f
@_p.types(None, _cs.GLfloat)
def glPassThrough(token):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, arrays.GLfloatArray)
def glPixelMapfv(map, mapsize, values):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, arrays.GLuintArray)
def glPixelMapuiv(map, mapsize, values):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLsizei, arrays.GLushortArray)
def glPixelMapusv(map, mapsize, values):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat)
def glPixelStoref(pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint)
def glPixelStorei(pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLfloat)
def glPixelTransferf(pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint)
def glPixelTransferi(pname, param):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat)
def glPixelZoom(xfactor, yfactor):
    ...

@_f
@_p.types(None, _cs.GLfloat)
def glPointSize(size):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum)
def glPolygonMode(face, mode):
    ...

@_f
@_p.types(None, arrays.GLubyteArray)
def glPolygonStipple(mask):
    ...

@_f
@_p.types(None)
def glPopAttrib():
    ...

@_f
@_p.types(None)
def glPopMatrix():
    ...

@_f
@_p.types(None)
def glPopName():
    ...

@_f
@_p.types(None, _cs.GLbitfield)
def glPushAttrib(mask):
    ...

@_f
@_p.types(None)
def glPushMatrix():
    ...

@_f
@_p.types(None, _cs.GLuint)
def glPushName(name):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble)
def glRasterPos2d(x, y):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glRasterPos2dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat)
def glRasterPos2f(x, y):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glRasterPos2fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint)
def glRasterPos2i(x, y):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glRasterPos2iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort)
def glRasterPos2s(x, y):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glRasterPos2sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glRasterPos3d(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glRasterPos3dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glRasterPos3f(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glRasterPos3fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint)
def glRasterPos3i(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glRasterPos3iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glRasterPos3s(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glRasterPos3sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glRasterPos4d(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glRasterPos4dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glRasterPos4f(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glRasterPos4fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glRasterPos4i(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glRasterPos4iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glRasterPos4s(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glRasterPos4sv(v):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glReadBuffer(src):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glReadPixels(x, y, width, height, format, type, pixels):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glRectd(x1, y1, x2, y2):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray, arrays.GLdoubleArray)
def glRectdv(v1, v2):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glRectf(x1, y1, x2, y2):
    ...

@_f
@_p.types(None, arrays.GLfloatArray, arrays.GLfloatArray)
def glRectfv(v1, v2):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glRecti(x1, y1, x2, y2):
    ...

@_f
@_p.types(None, arrays.GLintArray, arrays.GLintArray)
def glRectiv(v1, v2):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glRects(x1, y1, x2, y2):
    ...

@_f
@_p.types(None, arrays.GLshortArray, arrays.GLshortArray)
def glRectsv(v1, v2):
    ...

@_f
@_p.types(_cs.GLint, _cs.GLenum)
def glRenderMode(mode):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glRotated(angle, x, y, z):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glRotatef(angle, x, y, z):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glScaled(x, y, z):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glScalef(x, y, z):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei)
def glScissor(x, y, width, height):
    ...

@_f
@_p.types(None, _cs.GLsizei, arrays.GLuintArray)
def glSelectBuffer(size, buffer):
    ...

@_f
@_p.types(None, _cs.GLenum)
def glShadeModel(mode):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLuint)
def glStencilFunc(func, ref, mask):
    ...

@_f
@_p.types(None, _cs.GLuint)
def glStencilMask(mask):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLenum)
def glStencilOp(fail, zfail, zpass):
    ...

@_f
@_p.types(None, _cs.GLdouble)
def glTexCoord1d(s):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glTexCoord1dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat)
def glTexCoord1f(s):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glTexCoord1fv(v):
    ...

@_f
@_p.types(None, _cs.GLint)
def glTexCoord1i(s):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glTexCoord1iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort)
def glTexCoord1s(s):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glTexCoord1sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble)
def glTexCoord2d(s, t):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glTexCoord2dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat)
def glTexCoord2f(s, t):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glTexCoord2fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint)
def glTexCoord2i(s, t):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glTexCoord2iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort)
def glTexCoord2s(s, t):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glTexCoord2sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glTexCoord3d(s, t, r):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glTexCoord3dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glTexCoord3f(s, t, r):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glTexCoord3fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint)
def glTexCoord3i(s, t, r):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glTexCoord3iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glTexCoord3s(s, t, r):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glTexCoord3sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glTexCoord4d(s, t, r, q):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glTexCoord4dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glTexCoord4f(s, t, r, q):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glTexCoord4fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glTexCoord4i(s, t, r, q):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glTexCoord4iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glTexCoord4s(s, t, r, q):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glTexCoord4sv(v):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLfloat)
def glTexEnvf(target, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glTexEnvfv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLint)
def glTexEnvi(target, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glTexEnviv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLdouble)
def glTexGend(coord, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLdoubleArray)
def glTexGendv(coord, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLfloat)
def glTexGenf(coord, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glTexGenfv(coord, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLint)
def glTexGeni(coord, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glTexGeniv(coord, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLint, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glTexImage1D(target, level, internalformat, width, border, format, type, pixels):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei, _cs.GLint, _cs.GLenum, _cs.GLenum, ctypes.c_void_p)
def glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLfloat)
def glTexParameterf(target, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLfloatArray)
def glTexParameterfv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, _cs.GLint)
def glTexParameteri(target, pname, param):
    ...

@_f
@_p.types(None, _cs.GLenum, _cs.GLenum, arrays.GLintArray)
def glTexParameteriv(target, pname, params):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glTranslated(x, y, z):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glTranslatef(x, y, z):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble)
def glVertex2d(x, y):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glVertex2dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat)
def glVertex2f(x, y):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glVertex2fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint)
def glVertex2i(x, y):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glVertex2iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort)
def glVertex2s(x, y):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glVertex2sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glVertex3d(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glVertex3dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glVertex3f(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glVertex3fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint)
def glVertex3i(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glVertex3iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glVertex3s(x, y, z):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glVertex3sv(v):
    ...

@_f
@_p.types(None, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble, _cs.GLdouble)
def glVertex4d(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLdoubleArray)
def glVertex4dv(v):
    ...

@_f
@_p.types(None, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat, _cs.GLfloat)
def glVertex4f(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLfloatArray)
def glVertex4fv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLint, _cs.GLint)
def glVertex4i(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLintArray)
def glVertex4iv(v):
    ...

@_f
@_p.types(None, _cs.GLshort, _cs.GLshort, _cs.GLshort, _cs.GLshort)
def glVertex4s(x, y, z, w):
    ...

@_f
@_p.types(None, arrays.GLshortArray)
def glVertex4sv(v):
    ...

@_f
@_p.types(None, _cs.GLint, _cs.GLint, _cs.GLsizei, _cs.GLsizei)
def glViewport(x, y, width, height):
    ...

