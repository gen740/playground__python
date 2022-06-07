from . import constants as constants, protocols as protocols, transports as transports
from .log import logger as logger
from _typeshed import Incomplete

class _SSLPipe:
    max_size: Incomplete
    def __init__(self, context, server_side, server_hostname: Incomplete | None = ...) -> None: ...
    @property
    def context(self): ...
    @property
    def ssl_object(self): ...
    @property
    def need_ssldata(self): ...
    @property
    def wrapped(self): ...
    def do_handshake(self, callback: Incomplete | None = ...): ...
    def shutdown(self, callback: Incomplete | None = ...): ...
    def feed_eof(self) -> None: ...
    def feed_ssldata(self, data, only_handshake: bool = ...): ...
    def feed_appdata(self, data, offset: int = ...): ...

class _SSLProtocolTransport(transports._FlowControlMixin, transports.Transport):
    def __init__(self, loop, ssl_protocol) -> None: ...
    def get_extra_info(self, name, default: Incomplete | None = ...): ...
    def set_protocol(self, protocol) -> None: ...
    def get_protocol(self): ...
    def is_closing(self): ...
    def close(self) -> None: ...
    def __del__(self, _warn=...) -> None: ...
    def is_reading(self): ...
    def pause_reading(self) -> None: ...
    def resume_reading(self) -> None: ...
    def set_write_buffer_limits(self, high: Incomplete | None = ..., low: Incomplete | None = ...) -> None: ...
    def get_write_buffer_size(self): ...
    def get_write_buffer_limits(self): ...
    def write(self, data) -> None: ...
    def can_write_eof(self): ...
    def abort(self) -> None: ...

class SSLProtocol(protocols.Protocol):
    def __init__(self, loop, app_protocol, sslcontext, waiter, server_side: bool = ..., server_hostname: Incomplete | None = ..., call_connection_made: bool = ..., ssl_handshake_timeout: Incomplete | None = ...) -> None: ...
    def connection_made(self, transport) -> None: ...
    def connection_lost(self, exc) -> None: ...
    def pause_writing(self) -> None: ...
    def resume_writing(self) -> None: ...
    def data_received(self, data) -> None: ...
    def eof_received(self) -> None: ...
