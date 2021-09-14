"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.ARB.fragment_layer_viewport import *

'''OpenGL extension ARB.fragment_layer_viewport

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.fragment_layer_viewport to provide a more 
Python-friendly API

Overview (from the spec)
	
	The geometry shader has the special built-in variables gl_Layer and
	gl_ViewportIndex that specify which layer and viewport primitives
	are rendered to. Currently the fragment shader does not know which
	layer or viewport the fragments are being written to without the
	application implementing their own interface variables between
	the geometry and fragment shaders.
	
	This extension specifies that the gl_Layer and gl_ViewportIndex
	built-in variables are also available to the fragment shader so the
	application doesn't need to implement these manually.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/fragment_layer_viewport.txt
'''
def glInitFragmentLayerViewportARB():
    '''Return boolean indicating whether this extension is available'''
    ...

