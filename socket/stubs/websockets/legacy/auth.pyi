from ..datastructures import Headers
from .server import HTTPResponse, WebSocketServerProtocol
from typing import Any, Awaitable, Callable, Iterable, Optional, Tuple, Union

Credentials = Tuple[str, str]

class BasicAuthWebSocketServerProtocol(WebSocketServerProtocol):
    realm: str
    username: Optional[str]
    def __init__(self, *args: Any, realm: Optional[str] = ..., check_credentials: Optional[Callable[[str, str], Awaitable[bool]]] = ..., **kwargs: Any) -> None: ...
    async def check_credentials(self, username: str, password: str) -> bool: ...
    async def process_request(self, path: str, request_headers: Headers) -> Optional[HTTPResponse]: ...

def basic_auth_protocol_factory(realm: Optional[str] = ..., credentials: Optional[Union[Credentials, Iterable[Credentials]]] = ..., check_credentials: Optional[Callable[[str, str], Awaitable[bool]]] = ..., create_protocol: Optional[Callable[[Any], BasicAuthWebSocketServerProtocol]] = ...) -> Callable[[Any], BasicAuthWebSocketServerProtocol]: ...
