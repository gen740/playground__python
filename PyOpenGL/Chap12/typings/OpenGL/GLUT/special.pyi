"""
This type stub file was generated by pyright.
"""

import os
from OpenGL.platform import PLATFORM

"""
This type stub file was generated by pyright.
"""
GLUT = ...
PLATFORM = ...
FUNCTION_TYPE = ...
_log = ...
if os.name == "nt":
    ...
else:
    __glutInitWithExit = ...
if __glutInitWithExit:
    _exitfunc = ...
    def glutCreateWindow(title):
        """Create window with given title
        
        This is the Win32-specific version that handles
        registration of an exit-function handler 
        """
        ...
    
    def glutCreateMenu(callback):
        """Create menu with given callback 
        
        This is the Win32-specific version that handles 
        registration of an exit-function callback.
        """
        ...
    
else:
    _base_glutInit = ...
_base_glutDestroyWindow = getattr(GLUT, 'glutDestroyWindow', None)
class GLUTCallback(object):
    """Class implementing GLUT Callback registration functions"""
    def __init__(self, typeName, parameterTypes, parameterNames) -> None:
        """Initialise the glut callback instance"""
        ...
    
    argNames = ...
    def __call__(self, function, *args):
        ...
    


class GLUTTimerCallback(GLUTCallback):
    """GLUT timer callbacks (completely nonstandard wrt other GLUT callbacks)"""
    def __call__(self, milliseconds, function, value):
        ...
    


class GLUTMenuCallback(object):
    """Place to collect the GLUT Menu manipulation special code"""
    callbackType = ...
    def glutCreateMenu(cls, func):
        """Create a new (current) menu, return small integer identifier
        
        func( int ) -- Function taking a single integer reflecting
            the user's choice, the value passed to glutAddMenuEntry
        
        return menuID (small integer)
        """
        ...
    
    glutCreateMenu = ...
    def glutDestroyMenu(cls, menu):
        """Destroy (cleanup) the given menu
        
        Deregister's the interal pointer to the menu callback 
        
        returns None
        """
        ...
    
    glutDestroyMenu = ...


glutCreateMenu = ...
glutDestroyMenu = ...
glutButtonBoxFunc = ...
glutDialsFunc = ...
glutDisplayFunc = ...
glutEntryFunc = ...
glutIdleFunc = ...
glutJoystickFunc = ...
glutKeyboardFunc = ...
glutKeyboardUpFunc = ...
glutMenuStatusFunc = ...
glutMenuStateFunc = ...
glutMotionFunc = ...
glutMouseFunc = ...
glutOverlayDisplayFunc = ...
glutPassiveMotionFunc = ...
glutReshapeFunc = ...
glutSpaceballButtonFunc = ...
glutSpaceballMotionFunc = ...
glutSpaceballRotateFunc = ...
glutSpecialFunc = ...
glutSpecialUpFunc = ...
glutTabletButtonFunc = ...
glutTabletButtonFunc = ...
glutTabletMotionFunc = ...
glutVisibilityFunc = ...
glutWindowStatusFunc = ...
glutTimerFunc = ...
INITIALIZED = ...
def glutInit(*args):
    """Initialise the GLUT library"""
    ...

def glutDestroyWindow(window):
    """Want to destroy the window, we need to do some cleanup..."""
    ...
