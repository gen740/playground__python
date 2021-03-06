import http
from . import datastructures, frames, http11
from _typeshed import Incomplete
from typing import Optional

class WebSocketException(Exception): ...

class ConnectionClosed(WebSocketException):
    rcvd: Incomplete
    sent: Incomplete
    rcvd_then_sent: Incomplete
    def __init__(self, rcvd: Optional[frames.Close], sent: Optional[frames.Close], rcvd_then_sent: Optional[bool] = ...) -> None: ...
    @property
    def code(self) -> int: ...
    @property
    def reason(self) -> str: ...

class ConnectionClosedError(ConnectionClosed): ...
class ConnectionClosedOK(ConnectionClosed): ...
class InvalidHandshake(WebSocketException): ...
class SecurityError(InvalidHandshake): ...
class InvalidMessage(InvalidHandshake): ...

class InvalidHeader(InvalidHandshake):
    name: Incomplete
    value: Incomplete
    def __init__(self, name: str, value: Optional[str] = ...) -> None: ...

class InvalidHeaderFormat(InvalidHeader):
    def __init__(self, name: str, error: str, header: str, pos: int) -> None: ...

class InvalidHeaderValue(InvalidHeader): ...

class InvalidOrigin(InvalidHeader):
    def __init__(self, origin: Optional[str]) -> None: ...

class InvalidUpgrade(InvalidHeader): ...

class InvalidStatus(InvalidHandshake):
    response: Incomplete
    def __init__(self, response: http11.Response) -> None: ...

class InvalidStatusCode(InvalidHandshake):
    status_code: Incomplete
    headers: Incomplete
    def __init__(self, status_code: int, headers: datastructures.Headers) -> None: ...

class NegotiationError(InvalidHandshake): ...

class DuplicateParameter(NegotiationError):
    name: Incomplete
    def __init__(self, name: str) -> None: ...

class InvalidParameterName(NegotiationError):
    name: Incomplete
    def __init__(self, name: str) -> None: ...

class InvalidParameterValue(NegotiationError):
    name: Incomplete
    value: Incomplete
    def __init__(self, name: str, value: Optional[str]) -> None: ...

class AbortHandshake(InvalidHandshake):
    status: Incomplete
    headers: Incomplete
    body: Incomplete
    def __init__(self, status: http.HTTPStatus, headers: datastructures.HeadersLike, body: bytes = ...) -> None: ...

class RedirectHandshake(InvalidHandshake):
    uri: Incomplete
    def __init__(self, uri: str) -> None: ...

class InvalidState(WebSocketException, AssertionError): ...

class InvalidURI(WebSocketException):
    uri: Incomplete
    msg: Incomplete
    def __init__(self, uri: str, msg: str) -> None: ...

class PayloadTooBig(WebSocketException): ...
class ProtocolError(WebSocketException): ...
WebSocketProtocolError = ProtocolError
