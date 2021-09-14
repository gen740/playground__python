"""
This type stub file was generated by pyright.
"""

from typing import Any
from numpy import dtype, int_, ndarray
from numpy.polynomial._polybase import ABCPolyBase

"""
This type stub file was generated by pyright.
"""
__all__: list[str]
lagtrim = ...
def poly2lag(pol):
    ...

def lag2poly(c):
    ...

lagdomain: ndarray[Any, dtype[int_]]
lagzero: ndarray[Any, dtype[int_]]
lagone: ndarray[Any, dtype[int_]]
lagx: ndarray[Any, dtype[int_]]
def lagline(off, scl):
    ...

def lagfromroots(roots):
    ...

def lagadd(c1, c2):
    ...

def lagsub(c1, c2):
    ...

def lagmulx(c):
    ...

def lagmul(c1, c2):
    ...

def lagdiv(c1, c2):
    ...

def lagpow(c, pow, maxpower=...):
    ...

def lagder(c, m=..., scl=..., axis=...):
    ...

def lagint(c, m=..., k=..., lbnd=..., scl=..., axis=...):
    ...

def lagval(x, c, tensor=...):
    ...

def lagval2d(x, y, c):
    ...

def laggrid2d(x, y, c):
    ...

def lagval3d(x, y, z, c):
    ...

def laggrid3d(x, y, z, c):
    ...

def lagvander(x, deg):
    ...

def lagvander2d(x, y, deg):
    ...

def lagvander3d(x, y, z, deg):
    ...

def lagfit(x, y, deg, rcond=..., full=..., w=...):
    ...

def lagcompanion(c):
    ...

def lagroots(c):
    ...

def laggauss(deg):
    ...

def lagweight(x):
    ...

class Laguerre(ABCPolyBase):
    domain: Any
    window: Any
    basis_name: Any
    ...

