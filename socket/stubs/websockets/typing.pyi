import logging
from _typeshed import Incomplete
from typing import List, Optional, Tuple, Union

Data = Union[str, bytes]
LoggerLike = Union[logging.Logger, logging.LoggerAdapter]
Origin: Incomplete
Subprotocol: Incomplete
ExtensionName: Incomplete
ExtensionParameter = Tuple[str, Optional[str]]
ExtensionHeader = Tuple[ExtensionName, List[ExtensionParameter]]
