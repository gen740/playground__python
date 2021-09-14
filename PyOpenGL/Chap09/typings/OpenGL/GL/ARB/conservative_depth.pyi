"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.ARB.conservative_depth import *

'''OpenGL extension ARB.conservative_depth

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.conservative_depth to provide a more 
Python-friendly API

Overview (from the spec)
	
	There is a common optimization for hardware accelerated implementation of
	OpenGL which relies on an early depth test to be run before the fragment
	shader so that the shader evaluation can be skipped if the fragment ends
	up being discarded because it is occluded.
	
	This optimization does not affect the final rendering, and is typically
	possible when the fragment does not change the depth programmatically.
	(i.e.: it does not write to the built-in gl_FragDepth output). There are,
	however a class of operations on the depth in the shader which could
	still be performed while allowing the early depth test to operate.
	
	This extension allows the application to pass enough information to the
	GL implementation to activate such optimizations safely.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/conservative_depth.txt
'''
def glInitConservativeDepthARB():
    '''Return boolean indicating whether this extension is available'''
    ...

