"""
This type stub file was generated by pyright.
"""

from OpenGL.latebind import Curry

"""Simplistic wrapper decorator for Python-coded wrappers"""
class _LazyWrapper(Curry):
    """Marker to tell us that an object is a lazy wrapper"""
    ...


def lazy(baseFunction):
    """Produce a lazy-binding decorator that uses baseFunction

    Allows simple implementation of wrappers where the
    whole of the wrapper can be summed up as do 1 thing
    then call base function with the cleaned up result.

    Passes baseFunction in as the first argument of the
    wrapped function, all other parameters are passed
    unchanged.  The wrapper class created has __nonzero__
    and similar common wrapper entry points defined.
    """
    ...

if __name__ == "__main__":
    func = ...
    output = ...
    def testwrap(base):
        "Testing"
        ...
    
    testlazy = lazy(func)(testwrap)