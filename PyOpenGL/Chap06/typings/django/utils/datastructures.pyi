"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping

class OrderedSet:
    """
    A set which keeps the ordering of the inserted items.
    """
    def __init__(self, iterable=...) -> None:
        ...
    
    def add(self, item):
        ...
    
    def remove(self, item):
        ...
    
    def discard(self, item):
        ...
    
    def __iter__(self):
        ...
    
    def __contains__(self, item):
        ...
    
    def __bool__(self):
        ...
    
    def __len__(self):
        ...
    


class MultiValueDictKeyError(KeyError):
    ...


class MultiValueDict(dict):
    """
    A subclass of dictionary customized to handle multiple values for the
    same key.

    >>> d = MultiValueDict({'name': ['Adrian', 'Simon'], 'position': ['Developer']})
    >>> d['name']
    'Simon'
    >>> d.getlist('name')
    ['Adrian', 'Simon']
    >>> d.getlist('doesnotexist')
    []
    >>> d.getlist('doesnotexist', ['Adrian', 'Simon'])
    ['Adrian', 'Simon']
    >>> d.get('lastname', 'nonexistent')
    'nonexistent'
    >>> d.setlist('lastname', ['Holovaty', 'Willison'])

    This class exists to solve the irritating problem raised by cgi.parse_qs,
    which returns a list for every key, even though most Web forms submit
    single name-value pairs.
    """
    def __init__(self, key_to_list_mapping=...) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def __getitem__(self, key):
        """
        Return the last data value for this key, or [] if it's an empty list;
        raise KeyError if not found.
        """
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __copy__(self):
        ...
    
    def __deepcopy__(self, memo):
        ...
    
    def __getstate__(self):
        ...
    
    def __setstate__(self, obj_dict):
        ...
    
    def get(self, key, default=...):
        """
        Return the last data value for the passed key. If key doesn't exist
        or value is an empty list, return `default`.
        """
        ...
    
    def getlist(self, key, default=...):
        """
        Return the list of values for the key. If key doesn't exist, return a
        default value.
        """
        ...
    
    def setlist(self, key, list_):
        ...
    
    def setdefault(self, key, default=...):
        ...
    
    def setlistdefault(self, key, default_list=...):
        ...
    
    def appendlist(self, key, value):
        """Append an item to the internal list associated with key."""
        ...
    
    def items(self):
        """
        Yield (key, value) pairs, where value is the last item in the list
        associated with the key.
        """
        ...
    
    def lists(self):
        """Yield (key, list) pairs."""
        ...
    
    def values(self):
        """Yield the last value on every key list."""
        ...
    
    def copy(self):
        """Return a shallow copy of this object."""
        ...
    
    def update(self, *args, **kwargs):
        """Extend rather than replace existing key lists."""
        ...
    
    def dict(self):
        """Return current object as a dict with singular values."""
        ...
    


class ImmutableList(tuple):
    """
    A tuple-like object that raises useful errors when it is asked to mutate.

    Example::

        >>> a = ImmutableList(range(5), warning="You cannot mutate this.")
        >>> a[3] = '4'
        Traceback (most recent call last):
            ...
        AttributeError: You cannot mutate this.
    """
    def __new__(cls, *args, warning=..., **kwargs):
        ...
    
    def complain(self, *args, **kwargs):
        ...
    
    __delitem__ = ...
    __delslice__ = ...
    __iadd__ = ...
    __imul__ = ...
    __setitem__ = ...
    __setslice__ = ...
    append = ...
    extend = ...
    insert = ...
    pop = ...
    remove = ...
    sort = ...
    reverse = ...


class DictWrapper(dict):
    """
    Wrap accesses to a dictionary so that certain values (those starting with
    the specified prefix) are passed through a function before being returned.
    The prefix is removed before looking up the real value.

    Used by the SQL construction code to ensure that values are correctly
    quoted before being used.
    """
    def __init__(self, data, func, prefix) -> None:
        ...
    
    def __getitem__(self, key):
        """
        Retrieve the real value after stripping the prefix string (if
        present). If the prefix is present, pass the value through self.func
        before returning, otherwise return the raw value.
        """
        ...
    


class CaseInsensitiveMapping(Mapping):
    """
    Mapping allowing case-insensitive key lookups. Original case of keys is
    preserved for iteration and string representation.

    Example::

        >>> ci_map = CaseInsensitiveMapping({'name': 'Jane'})
        >>> ci_map['Name']
        Jane
        >>> ci_map['NAME']
        Jane
        >>> ci_map['name']
        Jane
        >>> ci_map  # original case preserved
        {'name': 'Jane'}
    """
    def __init__(self, data) -> None:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __len__(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __iter__(self):
        ...
    
    def __repr__(self):
        ...
    
    def copy(self):
        ...
    


