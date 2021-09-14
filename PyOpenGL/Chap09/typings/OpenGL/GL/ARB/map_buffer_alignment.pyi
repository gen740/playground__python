"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.ARB.map_buffer_alignment import *

'''OpenGL extension ARB.map_buffer_alignment

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.map_buffer_alignment to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds a requirement to the pointer returned by MapBuffer
	and MapBufferRange that they provide a minimum of 64 byte alignment to
	support processing of the data directly with special CPU instructions
	like SSE and AVX.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/map_buffer_alignment.txt
'''
def glInitMapBufferAlignmentARB():
    '''Return boolean indicating whether this extension is available'''
    ...

