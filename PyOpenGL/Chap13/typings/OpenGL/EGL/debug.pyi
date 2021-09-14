"""
This type stub file was generated by pyright.
"""

from OpenGL.EGL import *

"""Debug utilities for EGL operations"""
def eglErrorName(value):
    """Returns error constant if known, otherwise returns value"""
    ...

KNOWN_ERRORS = ...
def write_ppm(buf, filename):
    """Write height * width * 3-component buffer as ppm to filename
    
    This lets us write a simple image format without
    using any libraries that can be viewed on most
    linux workstations.
    """
    ...

def debug_config(display, config):
    """Get debug display for the given configuration"""
    ...

def debug_configs(display, configs=..., max_count=...):
    """Present a formatted list of configs for the display"""
    ...

SURFACE_TYPE_BITS = ...
RENDERABLE_TYPE_BITS = ...
CAVEAT_BITS = ...
TRANSPARENT_BITS = ...
CONFIG_ATTRS = ...
BITMASK_FIELDS = ...
def bit_renderer(bit):
    ...

CONFIG_FORMAT = ...
def format_debug_configs(debug_configs, formats=...):
    """Format config for compact debugging display
    
    Produces a config summary display for a set of 
    debug_configs as a text-mode table.

    Uses `formats` (default `CONFIG_FORMAT`) to determine 
    which fields are extracted and how they are formatted
    along with the column/subcolum set to be rendered in
    the overall header.

    returns formatted ASCII table for display in debug
    logs or utilities
    """
    ...
