from . import datastructures as datastructures, exceptions as exceptions
from _typeshed import Incomplete
from typing import Callable, Generator, Optional

MAX_HEADERS: int
MAX_LINE: int
MAX_BODY: Incomplete

def d(value: bytes) -> str: ...

class Request:
    path: str
    headers: datastructures.Headers
    @property
    def exception(self) -> Optional[Exception]: ...
    @classmethod
    def parse(cls, read_line: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, Request]: ...
    def serialize(self) -> bytes: ...
    def __init__(self, path, headers, _exception) -> None: ...

class Response:
    status_code: int
    reason_phrase: str
    headers: datastructures.Headers
    body: Optional[bytes]
    @property
    def exception(self) -> Optional[Exception]: ...
    @classmethod
    def parse(cls, read_line: Callable[[int], Generator[None, None, bytes]], read_exact: Callable[[int], Generator[None, None, bytes]], read_to_eof: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, Response]: ...
    def serialize(self) -> bytes: ...
    def __init__(self, status_code, reason_phrase, headers, body, _exception) -> None: ...

def parse_headers(read_line: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, datastructures.Headers]: ...
def parse_line(read_line: Callable[[int], Generator[None, None, bytes]]) -> Generator[None, None, bytes]: ...
