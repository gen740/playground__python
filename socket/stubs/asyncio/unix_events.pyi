from . import base_subprocess, events, selector_events, transports
from _typeshed import Incomplete

class _UnixSelectorEventLoop(selector_events.BaseSelectorEventLoop):
    def __init__(self, selector: Incomplete | None = ...) -> None: ...
    def close(self) -> None: ...
    def add_signal_handler(self, sig, callback, *args) -> None: ...
    def remove_signal_handler(self, sig): ...
    async def create_unix_connection(self, protocol_factory, path: Incomplete | None = ..., *, ssl: Incomplete | None = ..., sock: Incomplete | None = ..., server_hostname: Incomplete | None = ..., ssl_handshake_timeout: Incomplete | None = ...): ...
    async def create_unix_server(self, protocol_factory, path: Incomplete | None = ..., *, sock: Incomplete | None = ..., backlog: int = ..., ssl: Incomplete | None = ..., ssl_handshake_timeout: Incomplete | None = ..., start_serving: bool = ...): ...

class _UnixReadPipeTransport(transports.ReadTransport):
    max_size: Incomplete
    def __init__(self, loop, pipe, protocol, waiter: Incomplete | None = ..., extra: Incomplete | None = ...) -> None: ...
    def pause_reading(self) -> None: ...
    def resume_reading(self) -> None: ...
    def set_protocol(self, protocol) -> None: ...
    def get_protocol(self): ...
    def is_closing(self): ...
    def close(self) -> None: ...
    def __del__(self, _warn=...) -> None: ...

class _UnixWritePipeTransport(transports._FlowControlMixin, transports.WriteTransport):
    def __init__(self, loop, pipe, protocol, waiter: Incomplete | None = ..., extra: Incomplete | None = ...) -> None: ...
    def get_write_buffer_size(self): ...
    def write(self, data) -> None: ...
    def can_write_eof(self): ...
    def write_eof(self) -> None: ...
    def set_protocol(self, protocol) -> None: ...
    def get_protocol(self): ...
    def is_closing(self): ...
    def close(self) -> None: ...
    def __del__(self, _warn=...) -> None: ...
    def abort(self) -> None: ...

class _UnixSubprocessTransport(base_subprocess.BaseSubprocessTransport): ...

class AbstractChildWatcher:
    def add_child_handler(self, pid, callback, *args) -> None: ...
    def remove_child_handler(self, pid) -> None: ...
    def attach_loop(self, loop) -> None: ...
    def close(self) -> None: ...
    def is_active(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, a, b, c) -> None: ...

class PidfdChildWatcher(AbstractChildWatcher):
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None: ...
    def is_active(self): ...
    def close(self) -> None: ...
    def attach_loop(self, loop) -> None: ...
    def add_child_handler(self, pid, callback, *args) -> None: ...
    def remove_child_handler(self, pid): ...

class BaseChildWatcher(AbstractChildWatcher):
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def is_active(self): ...
    def attach_loop(self, loop) -> None: ...

class SafeChildWatcher(BaseChildWatcher):
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, a, b, c) -> None: ...
    def add_child_handler(self, pid, callback, *args) -> None: ...
    def remove_child_handler(self, pid): ...

class FastChildWatcher(BaseChildWatcher):
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, a, b, c) -> None: ...
    def add_child_handler(self, pid, callback, *args) -> None: ...
    def remove_child_handler(self, pid): ...

class MultiLoopChildWatcher(AbstractChildWatcher):
    def __init__(self) -> None: ...
    def is_active(self): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def add_child_handler(self, pid, callback, *args) -> None: ...
    def remove_child_handler(self, pid): ...
    def attach_loop(self, loop) -> None: ...

class ThreadedChildWatcher(AbstractChildWatcher):
    def __init__(self) -> None: ...
    def is_active(self): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __del__(self, _warn=...) -> None: ...
    def add_child_handler(self, pid, callback, *args) -> None: ...
    def remove_child_handler(self, pid): ...
    def attach_loop(self, loop) -> None: ...

class _UnixDefaultEventLoopPolicy(events.BaseDefaultEventLoopPolicy):
    def __init__(self) -> None: ...
    def set_event_loop(self, loop) -> None: ...
    def get_child_watcher(self): ...
    def set_child_watcher(self, watcher) -> None: ...

SelectorEventLoop: Incomplete
DefaultEventLoopPolicy: Incomplete
