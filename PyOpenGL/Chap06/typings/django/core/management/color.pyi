"""
This type stub file was generated by pyright.
"""

import functools

"""
Sets up the terminal color scheme.
"""
def supports_color():
    """
    Return True if the running system's terminal supports color,
    and False otherwise.
    """
    ...

class Style:
    ...


def make_style(config_string=...):
    """
    Create a Style object from the given config_string.

    If config_string is empty django.utils.termcolors.DEFAULT_PALETTE is used.
    """
    ...

@functools.lru_cache(maxsize=None)
def no_style():
    """
    Return a Style object with no color scheme.
    """
    ...

def color_style(force_color=...):
    """
    Return a Style object from the Django color scheme.
    """
    ...

