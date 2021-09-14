"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.ARB.shader_atomic_counters import *

'''OpenGL extension ARB.shader_atomic_counters

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_atomic_counters to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a set of atomic counters.
	
	This extension provides GLSL built-in functions to
	query and increment/decrement these atomic counters.
	
	This enables a shader to write to unique offsets
	(append to a buffer object) or read from unique offsets
	(consume from a buffer object).
	
	Opaque handles to atomic counters are declared
	at global scope and are qualified with the uniform qualifier.
	
	Unlike other user-defined uniforms declared at global scope,
	they take NO storage from the default partition, they have
	NO location, and they may NOT be set with the Uniform* commands.
	Atomic counters may also NOT be grouped into uniform blocks.
	
	Active atomic counters can be discovered by the commands
	GetUniformIndices, GetActiveUniformName, GetActiveUniform
	and GetActiveUniformsiv.
	
	Like samplers, the opaque handles of the atomic counters
	and are ONLY used in some GLSL built-in functions.
	
	The atomic counters pointed to by the opaque handles
	are bound to buffer binding points and buffer offsets
	through the layout qualifiers in the shading language,
	or they are implicitly assigned by the compiler.
	
	Through the OpenGL API, buffer objects may be
	bound to these binding points with BindBufferBase
	or BindBufferRange.
	
	The contents of the atomic counters are stored
	in the buffer objects.  The contents of atomic
	counters may be set and queried with buffer object
	manipulation functions (e.g. BufferData,
	BufferSubData, MapBuffer or MapBufferRange).
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shader_atomic_counters.txt
'''
def glInitShaderAtomicCountersARB():
    '''Return boolean indicating whether this extension is available'''
    ...

glGetActiveAtomicCounterBufferiv = ...
