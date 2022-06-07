from .. import frames
from ..typing import ExtensionParameter
from .base import ClientExtensionFactory, Extension, ServerExtensionFactory
from _typeshed import Incomplete
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

class PerMessageDeflate(Extension):
    name: Incomplete
    remote_no_context_takeover: Incomplete
    local_no_context_takeover: Incomplete
    remote_max_window_bits: Incomplete
    local_max_window_bits: Incomplete
    compress_settings: Incomplete
    decoder: Incomplete
    encoder: Incomplete
    decode_cont_data: bool
    def __init__(self, remote_no_context_takeover: bool, local_no_context_takeover: bool, remote_max_window_bits: int, local_max_window_bits: int, compress_settings: Optional[Dict[Any, Any]] = ...) -> None: ...
    def decode(self, frame: frames.Frame, *, max_size: Optional[int] = ...) -> frames.Frame: ...
    def encode(self, frame: frames.Frame) -> frames.Frame: ...

class ClientPerMessageDeflateFactory(ClientExtensionFactory):
    name: Incomplete
    server_no_context_takeover: Incomplete
    client_no_context_takeover: Incomplete
    server_max_window_bits: Incomplete
    client_max_window_bits: Incomplete
    compress_settings: Incomplete
    def __init__(self, server_no_context_takeover: bool = ..., client_no_context_takeover: bool = ..., server_max_window_bits: Optional[int] = ..., client_max_window_bits: Optional[Union[int, bool]] = ..., compress_settings: Optional[Dict[str, Any]] = ...) -> None: ...
    def get_request_params(self) -> List[ExtensionParameter]: ...
    def process_response_params(self, params: Sequence[ExtensionParameter], accepted_extensions: Sequence[Extension]) -> PerMessageDeflate: ...

def enable_client_permessage_deflate(extensions: Optional[Sequence[ClientExtensionFactory]]) -> Sequence[ClientExtensionFactory]: ...

class ServerPerMessageDeflateFactory(ServerExtensionFactory):
    name: Incomplete
    server_no_context_takeover: Incomplete
    client_no_context_takeover: Incomplete
    server_max_window_bits: Incomplete
    client_max_window_bits: Incomplete
    compress_settings: Incomplete
    require_client_max_window_bits: Incomplete
    def __init__(self, server_no_context_takeover: bool = ..., client_no_context_takeover: bool = ..., server_max_window_bits: Optional[int] = ..., client_max_window_bits: Optional[int] = ..., compress_settings: Optional[Dict[str, Any]] = ..., require_client_max_window_bits: bool = ...) -> None: ...
    def process_request_params(self, params: Sequence[ExtensionParameter], accepted_extensions: Sequence[Extension]) -> Tuple[List[ExtensionParameter], PerMessageDeflate]: ...

def enable_server_permessage_deflate(extensions: Optional[Sequence[ServerExtensionFactory]]) -> Sequence[ServerExtensionFactory]: ...
