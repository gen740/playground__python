"""
This type stub file was generated by pyright.
"""

from typing import List

"""
This type stub file was generated by pyright.
"""
__all__: List[str]
row_stack = ...
def take_along_axis(arr, indices, axis):
    ...

def put_along_axis(arr, indices, values, axis):
    ...

def apply_along_axis(func1d, axis, arr, *args, **kwargs):
    ...

def apply_over_axes(func, a, axes):
    ...

def expand_dims(a, axis):
    ...

def column_stack(tup):
    ...

def dstack(tup):
    ...

def array_split(ary, indices_or_sections, axis=...):
    ...

def split(ary, indices_or_sections, axis=...):
    ...

def hsplit(ary, indices_or_sections):
    ...

def vsplit(ary, indices_or_sections):
    ...

def dsplit(ary, indices_or_sections):
    ...

def get_array_prepare(*args):
    ...

def get_array_wrap(*args):
    ...

def kron(a, b):
    ...

def tile(A, reps):
    ...
