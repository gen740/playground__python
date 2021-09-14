"""
This type stub file was generated by pyright.
"""

"""Image-handling routines

### Unresolved:

    Following methods are not yet resolved due to my not being sure how the
    function should be wrapped:

        glCompressedTexImage3D
        glCompressedTexImage2D
        glCompressedTexImage1D
        glCompressedTexSubImage3D
        glCompressedTexSubImage2D
        glCompressedTexSubImage1D
"""
def asInt(value):
    ...

def glReadPixels(x, y, width, height, format, type, array=..., outputType=...):
    """Read specified pixels from the current display buffer

    x,y,width,height -- location and dimensions of the image to read
        from the buffer
    format -- pixel format for the resulting data
    type -- data-format for the resulting data
    array -- optional array/offset into which to store the value
    outputType -- default (bytes) provides string output of the
        results iff OpenGL.UNSIGNED_BYTE_IMAGES_AS_STRING is True
        and type == GL_UNSIGNED_BYTE.  Any other value will cause
        output in the default array output format.

    returns the pixel data array in the format defined by the
    format, type and outputType
    """
    ...

def glGetTexImage(target, level, format, type, array=..., outputType=...):
    """Get a texture-level as an image

    target -- enum constant for the texture engine to be read
    level -- the mip-map level to read
    format -- image format to read out the data
    type -- data-type into which to read the data
    array -- optional array/offset into which to store the value

    outputType -- default (bytes) provides string output of the
        results iff OpenGL.UNSIGNED_BYTE_IMAGES_AS_STRING is True
        and type == GL_UNSIGNED_BYTE.  Any other value will cause
        output in the default array output format.

    returns the pixel data array in the format defined by the
    format, type and outputType
    """
    ...

INT_DIMENSION_NAMES = ...
def asWrapper(value):
    ...

def asIntConverter(value, *args):
    ...

def setDimensionsAsInts(baseOperation):
    """Set arguments with names in INT_DIMENSION_NAMES to asInt processing"""
    ...

class ImageInputConverter(object):
    def __init__(self, rank, pixelsName=..., typeName=...) -> None:
        ...
    
    def finalise(self, wrapper):
        """Get our pixel index from the wrapper"""
        ...
    
    def __call__(self, arg, baseOperation, pyArgs):
        """pyConverter for the pixels argument"""
        ...
    


class TypedImageInputConverter(ImageInputConverter):
    def __init__(self, rank, pixelsName, arrayType, typeName=...) -> None:
        ...
    
    def __call__(self, arg, baseOperation, pyArgs):
        """The pyConverter for the pixels"""
        ...
    
    def finalise(self, wrapper):
        """Get our pixel index from the wrapper"""
        ...
    
    def width(self, pyArgs, index, wrappedOperation):
        """Extract the width from the pixels argument"""
        ...
    
    def height(self, pyArgs, index, wrappedOperation):
        """Extract the height from the pixels argument"""
        ...
    
    def depth(self, pyArgs, index, wrappedOperation):
        """Extract the depth from the pixels argument"""
        ...
    
    def type(self, pyArgs, index, wrappedOperation):
        """Provide the item-type argument from our stored value

        This is used for pre-bound processing where we want to provide
        the type by implication...
        """
        ...
    


class CompressedImageConverter(object):
    def finalise(self, wrapper):
        """Get our pixel index from the wrapper"""
        ...
    
    def __call__(self, pyArgs, index, wrappedOperation):
        """Create a data-size measurement for our image"""
        ...
    


DIMENSION_NAMES = ...
PIXEL_NAMES = ...
DATA_SIZE_NAMES = ...
def setImageInput(baseOperation, arrayType=..., dimNames=..., pixelName=..., typeName=...):
    """Determine how to convert "pixels" into an image-compatible argument"""
    ...

glDrawPixels = ...
glTexSubImage2D = ...
glTexSubImage1D = ...
glTexImage2D = ...
glTexImage1D = ...
def typedImageFunction(suffix, arrayConstant, baseFunction):
    """Produce a typed version of the given image function"""
    ...

def compressedImageFunction(baseFunction):
    """Set the imageSize and dimensions-as-ints converters for baseFunction"""
    ...

