from .. import extensions as extensions, frames as frames
from ..exceptions import PayloadTooBig as PayloadTooBig, ProtocolError as ProtocolError
from ..frames import Close as Close, prepare_data as prepare_data
from ..utils import apply_mask as apply_mask
from typing import Any, Awaitable, Callable, NamedTuple, Optional, Sequence, Tuple

class Frame(NamedTuple):
    fin: bool
    opcode: frames.Opcode
    data: bytes
    rsv1: bool
    rsv2: bool
    rsv3: bool
    @property
    def new_frame(self) -> frames.Frame: ...
    def check(self) -> None: ...
    @classmethod
    async def read(cls, reader: Callable[[int], Awaitable[bytes]], *, mask: bool, max_size: Optional[int] = ..., extensions: Optional[Sequence[extensions.Extension]] = ...) -> Frame: ...
    def write(self, write: Callable[[bytes], Any], *, mask: bool, extensions: Optional[Sequence[extensions.Extension]] = ...) -> None: ...

def parse_close(data: bytes) -> Tuple[int, str]: ...
def serialize_close(code: int, reason: str) -> bytes: ...
