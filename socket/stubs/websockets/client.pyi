from .legacy.client import *
from .connection import Connection, State
from .datastructures import Headers
from .extensions import ClientExtensionFactory, Extension
from .http11 import Request, Response
from .typing import LoggerLike, Origin, Subprotocol
from .uri import WebSocketURI
from _typeshed import Incomplete
from typing import Generator, List, Optional, Sequence

class ClientConnection(Connection):
    wsuri: Incomplete
    origin: Incomplete
    available_extensions: Incomplete
    available_subprotocols: Incomplete
    key: Incomplete
    def __init__(self, wsuri: WebSocketURI, origin: Optional[Origin] = ..., extensions: Optional[Sequence[ClientExtensionFactory]] = ..., subprotocols: Optional[Sequence[Subprotocol]] = ..., state: State = ..., max_size: Optional[int] = ..., logger: Optional[LoggerLike] = ...) -> None: ...
    def connect(self) -> Request: ...
    extensions: Incomplete
    subprotocol: Incomplete
    def process_response(self, response: Response) -> None: ...
    def process_extensions(self, headers: Headers) -> List[Extension]: ...
    def process_subprotocol(self, headers: Headers) -> Optional[Subprotocol]: ...
    def send_request(self, request: Request) -> None: ...
    handshake_exc: Incomplete
    parser: Incomplete
    state: Incomplete
    def parse(self) -> Generator[None, None, None]: ...
