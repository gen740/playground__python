"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.ARB.base_instance import *

'''OpenGL extension ARB.base_instance

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.base_instance to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows the offset within buffer objects used for instanced
	rendering to be specified. This is congruent with the <first> parameter
	in glDrawArrays and the <basevertex> parameter in glDrawElements. When
	instanced rendering is performed (for example, through
	glDrawArraysInstanced), instanced vertex attributes whose vertex attribute
	divisors are non-zero are fetched from enabled vertex arrays per-instance
	rather than per-vertex. However, in unextended OpenGL, there is no way to
	define the offset into those arrays from which the attributes are fetched.
	This extension adds that offset in the form of a <baseinstance> parameter
	to several new procedures.
	
	The <baseinstance> parameter is added to the index of the array element,
	after division by the vertex attribute divisor. This allows several sets of
	instanced vertex attribute data to be stored in a single vertex array, and
	the base offset of that data to be specified for each draw. Further, this
	extension exposes the <baseinstance> parameter as the final and previously
	undefined structure member of the draw-indirect data structure.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/base_instance.txt
'''
def glInitBaseInstanceARB():
    '''Return boolean indicating whether this extension is available'''
    ...

glDrawElementsInstancedBaseInstance = ...
glDrawElementsInstancedBaseVertexBaseInstance = ...
