"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.ARB.explicit_uniform_location import *

'''OpenGL extension ARB.explicit_uniform_location

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.explicit_uniform_location to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a method to pre-assign uniform locations to
	uniform variables in the default uniform block, including subroutine
	uniforms. This allows an application to modify the uniform values without
	requiring a GL query like GetUniformLocation, GetSubroutineUniformLocation
	and GetSubroutineIndex.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/explicit_uniform_location.txt
'''
def glInitExplicitUniformLocationARB():
    '''Return boolean indicating whether this extension is available'''
    ...
