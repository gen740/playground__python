"""
This type stub file was generated by pyright.
"""

import enum

class ChoicesMeta(enum.EnumMeta):
    """A metaclass for creating a enum choices."""
    def __new__(metacls, classname, bases, classdict, **kwds):
        ...
    
    def __contains__(cls, member):
        ...
    
    @property
    def names(cls):
        ...
    
    @property
    def choices(cls):
        ...
    
    @property
    def labels(cls):
        ...
    
    @property
    def values(cls):
        ...
    


class Choices(enum.Enum, metaclass=ChoicesMeta):
    """Class for creating enumerated choices."""
    def __str__(self) -> str:
        """
        Use value when cast to str, so that Choices set as model instance
        attributes are rendered as expected in templates and similar contexts.
        """
        ...
    


class IntegerChoices(int, Choices):
    """Class for creating enumerated integer choices."""
    ...


class TextChoices(str, Choices):
    """Class for creating enumerated string choices."""
    ...

