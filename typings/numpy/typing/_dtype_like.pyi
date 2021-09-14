"""
This type stub file was generated by pyright.
"""

import sys
from typing import Any, Protocol, Sequence, TYPE_CHECKING, TypedDict

"""
This type stub file was generated by pyright.
"""
if sys.version_info >= (3, 8):
    HAVE_PROTOCOL = ...
else:
    ...
_DTypeLikeNested = Any
if TYPE_CHECKING or HAVE_PROTOCOL:
    class _DTypeDictBase(TypedDict):
        names: Sequence[str]
        formats: Sequence[_DTypeLikeNested]
        ...
    
    
    class _DTypeDict(_DTypeDictBase, total=False):
        offsets: Sequence[int]
        titles: Sequence[Any]
        itemsize: int
        aligned: bool
        ...
    
    
    _DType_co = ...
    class _SupportsDType(Protocol[_DType_co]):
        @property
        def dtype(self) -> _DType_co:
            ...
        
    
    
else:
    ...
_VoidDTypeLike = ...
DTypeLike = ...
_DTypeLikeBool = ...
_DTypeLikeUInt = ...
_DTypeLikeInt = ...
_DTypeLikeFloat = ...
_DTypeLikeComplex = ...
_DTypeLikeDT64 = ...
_DTypeLikeTD64 = ...
_DTypeLikeStr = ...
_DTypeLikeBytes = ...
_DTypeLikeVoid = ...
_DTypeLikeObject = ...
_DTypeLikeComplex_co = ...