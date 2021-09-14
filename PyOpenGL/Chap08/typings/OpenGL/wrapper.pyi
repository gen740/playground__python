"""
This type stub file was generated by pyright.
"""

from OpenGL import acceleratesupport
from OpenGL._configflags import ERROR_ON_COPY, STORE_POINTERS
from OpenGL.latebind import LateBind

"""The wrapping code for providing natural ctypes-based OpenGL interface"""
_log = ...
cWrapper = ...
if acceleratesupport.ACCELERATE_AVAILABLE:
    ...
if not STORE_POINTERS:
    ...
def asList(o):
    """Convert to a list if not already one"""
    ...

def none_or_pass(incoming, function, arguments):
    ...

class Wrapper(LateBind):
    """Wrapper around a ctypes cFunction object providing SWIG-like hooks

    Attributes:

        wrappedOperation -- base operation, normally a ctypes function
            with data-types and error-checking specified
        pyConverters -- converters for incoming Python arguments,
            provide 1:1 mapping to incoming Python arguments, can
            suppress an argument from the argument-set as well
                see setPyConverter
        pyConverterNames -- caching/storage of the argument names
            for the Python converters
        cConverters -- converters for incoming C-level arguments
            produce Python-level objects in 1:1 mapping to ctypes
            arguments from pyConverters results
                see setCConverter
        cResolvers -- converters turning Python-level objects into
            ctypes-compatible data-types
                see setCResolver

    Generic Attributes:

        {ARG1}_LOOKUP_{ARG2} -- lookup dictionaries to provide sizes for
            ARG1 output value from the value of ARG2, provided for
            documentation/reference
        {ARG1}_FROM_{ARG2} -- lookup functions to provide sizes for ARG1
            output value from the value of ARG2, provided for
            documentation/reference
    """
    localProperties = ...
    def __init__(self, wrappedOperation) -> None:
        """Initialise the wrapper, storing wrappedOperation"""
        ...
    
    def __getattr__(self, key):
        """Delegate attribute lookup to our wrappedOperation"""
        ...
    
    def __nonzero__(self):
        """Is this function/wrapper available?"""
        ...
    
    __bool__ = ...
    def __setattr__(self, key, value):
        """Forward attribute setting to our wrappedOperation"""
        ...
    
    def pyArgIndex(self, argName):
        """Return the Python-argument index for the given argument name"""
        ...
    
    def cArgIndex(self, argName):
        """Return the C-argument index for the given argument name"""
        ...
    
    def setOutput(self, outArg, size=..., pnameArg=..., arrayType=..., oldStyleReturn=..., orPassIn=...):
        """Set the given argName to be an output array

        size -- either a tuple compatible with arrayType.zeros or
            a function taking pname to produce such a value.
        arrayType -- array data-type used to generate the output
            array using the zeros class method...
        pnameArg -- optional argument passed into size function, that
            is, the name of the argument whose *value* will be passed
            to the size function, often the name of an input argument
            to be "sized" to match the output argument.
        """
        ...
    
    def typeOfArg(self, outArg):
        """Retrieve the defined data-type for the given outArg (name)"""
        ...
    
    if not ERROR_ON_COPY:
        def setInputArraySize(self, argName, size=...):
            """Decorate function with vector-handling code for a single argument
            
            if OpenGL.ERROR_ON_COPY is False, then we return the 
            named argument, converting to the passed array type,
            optionally checking that the array matches size.
            
            if OpenGL.ERROR_ON_COPY is True, then we will dramatically 
            simplify this function, only wrapping if size is True, i.e.
            only wrapping if we intend to do a size check on the array.
            """
            ...
        
    else:
        def setInputArraySize(self, argName, size=...):
            """Decorate function with vector-handling code for a single argument
            
            if OpenGL.ERROR_ON_COPY is False, then we return the 
            named argument, converting to the passed array type,
            optionally checking that the array matches size.
            
            if OpenGL.ERROR_ON_COPY is True, then we will dramatically 
            simplify this function, only wrapping if size is True, i.e.
            only wrapping if we intend to do a size check on the array.
            """
            ...
        
    def setPyConverter(self, argName, function=...):
        """Set Python-argument converter for given argument

        argName -- the argument name which will be coerced to a usable internal
            format using the function provided.
        function -- None (indicating a simple copy), NULL (default) to eliminate
            the argument from the Python argument-list, or a callable object with
            the signature:

                converter(arg, wrappedOperation, args)

            where arg is the particular argument on which the convert is working,
            wrappedOperation is the underlying wrapper, and args is the set of
            original Python arguments to the function.

        Note that you need exactly the same number of pyConverters as Python
        arguments.
        """
        ...
    
    def setCConverter(self, argName, function):
        """Set C-argument converter for a given argument

        argName -- the argument name whose C-compatible representation will
            be calculated with the passed function.
        function -- None (indicating a simple copy), a non-callable object to
            be copied into the result-list itself, or a callable object with
            the signature:

                converter( pyArgs, index, wrappedOperation )

            where pyArgs is the set of passed Python arguments, with the
            pyConverters already applied, index is the index of the C argument
            and wrappedOperation is the underlying function.

        C-argument converters are your chance to expand/contract a Python
        argument list (pyArgs) to match the number of arguments expected by
        the ctypes baseOperation.  You can't have a "null" C-argument converter,
        as *something* has to be passed to the C-level function in the
        parameter.
        """
        ...
    
    def setCResolver(self, argName, function=...):
        """Set C-argument converter for a given argument"""
        ...
    
    def setStoreValues(self, function=...):
        """Set the storage-of-arguments function for the whole wrapper"""
        ...
    
    def setReturnValues(self, function=...):
        """Set the return-of-results function for the whole wrapper"""
        ...
    
    def finalise(self):
        """Finalise our various elements into simple index-based operations"""
        ...
    
    def finaliseCall(self):
        """Produce specialised versions of call for finalised wrapper object

        This returns a version of __call__ that only does that work which is
        required by the particular wrapper object

        This is essentially a huge set of expanded nested functions, very
        inelegant...
        """
        ...
    


class MultiReturn(object):
    def __init__(self, *children) -> None:
        ...
    
    def append(self, child):
        ...
    
    def __call__(self, *args, **named):
        ...
    


def wrapper(wrappedOperation):
    """Create a Wrapper sub-class instance for the given wrappedOperation

    The purpose of this function is to create a subclass of Wrapper which
    has the __doc__ and __name__ of the wrappedOperation so that the instance of
    the wrapper will show up as <functionname instance @ address> by default,
    and will have the docstring available naturally in pydoc and the like.
    """
    ...
