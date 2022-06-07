from typing import Optional, Tuple

class WebSocketURI:
    secure: bool
    host: str
    port: int
    path: str
    query: str
    username: Optional[str]
    password: Optional[str]
    @property
    def resource_name(self) -> str: ...
    @property
    def user_info(self) -> Optional[Tuple[str, str]]: ...
    def __init__(self, secure, host, port, path, query, username, password) -> None: ...

def parse_uri(uri: str) -> WebSocketURI: ...
