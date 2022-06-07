from ..datastructures import Headers, HeadersLike
from ..extensions import ClientExtensionFactory, Extension
from ..typing import LoggerLike, Origin, Subprotocol
from ..uri import WebSocketURI
from .protocol import WebSocketCommonProtocol
from _typeshed import Incomplete
from types import TracebackType
from typing import Any, AsyncIterator, Callable, Generator, List, Optional, Sequence, Tuple, Type

class WebSocketClientProtocol(WebSocketCommonProtocol):
    is_client: bool
    side: str
    origin: Incomplete
    available_extensions: Incomplete
    available_subprotocols: Incomplete
    extra_headers: Incomplete
    def __init__(self, *, logger: Optional[LoggerLike] = ..., origin: Optional[Origin] = ..., extensions: Optional[Sequence[ClientExtensionFactory]] = ..., subprotocols: Optional[Sequence[Subprotocol]] = ..., extra_headers: Optional[HeadersLike] = ..., **kwargs: Any) -> None: ...
    path: Incomplete
    request_headers: Incomplete
    def write_http_request(self, path: str, headers: Headers) -> None: ...
    response_headers: Incomplete
    async def read_http_response(self) -> Tuple[int, Headers]: ...
    @staticmethod
    def process_extensions(headers: Headers, available_extensions: Optional[Sequence[ClientExtensionFactory]]) -> List[Extension]: ...
    @staticmethod
    def process_subprotocol(headers: Headers, available_subprotocols: Optional[Sequence[Subprotocol]]) -> Optional[Subprotocol]: ...
    extensions: Incomplete
    subprotocol: Incomplete
    async def handshake(self, wsuri: WebSocketURI, origin: Optional[Origin] = ..., available_extensions: Optional[Sequence[ClientExtensionFactory]] = ..., available_subprotocols: Optional[Sequence[Subprotocol]] = ..., extra_headers: Optional[HeadersLike] = ...) -> None: ...

class Connect:
    MAX_REDIRECTS_ALLOWED: int
    open_timeout: Incomplete
    logger: Incomplete
    def __init__(self, uri: str, *, create_protocol: Optional[Callable[[Any], WebSocketClientProtocol]] = ..., logger: Optional[LoggerLike] = ..., compression: Optional[str] = ..., origin: Optional[Origin] = ..., extensions: Optional[Sequence[ClientExtensionFactory]] = ..., subprotocols: Optional[Sequence[Subprotocol]] = ..., extra_headers: Optional[HeadersLike] = ..., open_timeout: Optional[float] = ..., ping_interval: Optional[float] = ..., ping_timeout: Optional[float] = ..., close_timeout: Optional[float] = ..., max_size: Optional[int] = ..., max_queue: Optional[int] = ..., read_limit: int = ..., write_limit: int = ..., **kwargs: Any) -> None: ...
    def handle_redirect(self, uri: str) -> None: ...
    BACKOFF_MIN: float
    BACKOFF_MAX: float
    BACKOFF_FACTOR: float
    BACKOFF_INITIAL: int
    async def __aiter__(self) -> AsyncIterator[WebSocketClientProtocol]: ...
    async def __aenter__(self) -> WebSocketClientProtocol: ...
    async def __aexit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> None: ...
    def __await__(self) -> Generator[Any, None, WebSocketClientProtocol]: ...
    async def __await_impl_timeout__(self) -> WebSocketClientProtocol: ...
    protocol: Incomplete
    async def __await_impl__(self) -> WebSocketClientProtocol: ...
    __iter__: Incomplete
connect = Connect

def unix_connect(path: Optional[str] = ..., uri: str = ..., **kwargs: Any) -> Connect: ...
