from .. import frames
from ..typing import ExtensionName, ExtensionParameter
from typing import List, Optional, Sequence, Tuple

class Extension:
    name: ExtensionName
    def decode(self, frame: frames.Frame, *, max_size: Optional[int] = ...) -> frames.Frame: ...
    def encode(self, frame: frames.Frame) -> frames.Frame: ...

class ClientExtensionFactory:
    name: ExtensionName
    def get_request_params(self) -> List[ExtensionParameter]: ...
    def process_response_params(self, params: Sequence[ExtensionParameter], accepted_extensions: Sequence[Extension]) -> Extension: ...

class ServerExtensionFactory:
    name: ExtensionName
    def process_request_params(self, params: Sequence[ExtensionParameter], accepted_extensions: Sequence[Extension]) -> Tuple[List[ExtensionParameter], Extension]: ...
