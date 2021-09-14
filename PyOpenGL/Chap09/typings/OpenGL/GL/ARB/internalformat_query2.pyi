"""
This type stub file was generated by pyright.
"""

from OpenGL.raw.GL.ARB.internalformat_query2 import *

'''OpenGL extension ARB.internalformat_query2

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.internalformat_query2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension extends the GetInternalformativ query that was added in
	the ARB_internalformat_query extension to provide applications with more 
	granular per-format capability information.
	
	This extension allows the remainder of the texture-style targets to
	be specified along with any possible internal format. 
	We add queries for additional properties supported for an internal
	format in addition to the multisample-related information that was
	added in ARB_internalformat_query.
	
	The goals of this extension are to: 
	
	a) provide a mechanism for implementations to declare support *above* the
	   minimum required by the specification
	
	b) provide API to allow universally constant information to be queried
	
	c) provide a user-friendly way of finding out about version- or 
	   implementation-specific limitations. 
	
	While much of this information can be determined for a single GL version
	by careful examination of the specification, support for many of these 
	properties has been gradually introduced over a number of API
	revisions. This can observed when considering the range in functionality
	between the various versions of GL 2, 3, and 4, as well as GL ES 2 and 3.
	
	In the case of an application which wishes to be scalable and able to run
	on a variety of possible GL or GL ES versions without being specifically
	tailored for each version, it must either have knowledge of the
	specifications built up into either the code or tables, or it must do
	a number of tests on startup to determine which capabilities are present.
	
	In OpenGL, other than the course-grained extension mechanism, many 
	limitations of, or limited support for, an internalformat can only 
	be signaled by failing an operation or by operating at reduced
	performance.  Thus, such tests often involve attempts to create resources,
	using them in specific ways and benchmarking the operations to
	find out if it is supported in the desired form, and at a required 
	performance level. The extension provides a way for these properties
	and caveats to be directly queried from the implementation.
	
	This extension is NOT intended to allow implementations to only support
	a subset of features that are required by a specific GL version, nor is
	it intended to replace the proper use of extension checks for optional
	functionality.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/internalformat_query2.txt
'''
def glInitInternalformatQuery2ARB():
    '''Return boolean indicating whether this extension is available'''
    ...

glGetInternalformati64v = ...
