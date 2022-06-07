import enum
from . import extensions
from .typing import Data
from _typeshed import Incomplete
from typing import Callable, Generator, Optional, Sequence, Tuple

class Opcode(enum.IntEnum):
    CONT: Incomplete
    TEXT: Incomplete
    BINARY: Incomplete
    CLOSE: Incomplete
    PING: Incomplete
    PONG: Incomplete

OP_CONT: Incomplete
OP_TEXT: Incomplete
OP_BINARY: Incomplete
OP_CLOSE: Incomplete
OP_PING: Incomplete
OP_PONG: Incomplete
DATA_OPCODES: Incomplete
CTRL_OPCODES: Incomplete

class Frame:
    opcode: Opcode
    data: bytes
    fin: bool
    rsv1: bool
    rsv2: bool
    rsv3: bool
    @classmethod
    def parse(cls, read_exact: Callable[[int], Generator[None, None, bytes]], *, mask: bool, max_size: Optional[int] = ..., extensions: Optional[Sequence[extensions.Extension]] = ...) -> Generator[None, None, Frame]: ...
    def serialize(self, *, mask: bool, extensions: Optional[Sequence[extensions.Extension]] = ...) -> bytes: ...
    def check(self) -> None: ...
    def __init__(self, opcode, data, fin, rsv1, rsv2, rsv3) -> None: ...

def prepare_data(data: Data) -> Tuple[int, bytes]: ...
def prepare_ctrl(data: Data) -> bytes: ...

class Close:
    code: int
    reason: str
    @classmethod
    def parse(cls, data: bytes) -> Close: ...
    def serialize(self) -> bytes: ...
    def check(self) -> None: ...
    def __init__(self, code, reason) -> None: ...
