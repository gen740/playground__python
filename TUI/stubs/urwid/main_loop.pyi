from ._async_kw_event_loop import TrioEventLoop as TrioEventLoop
from twisted.internet.abstract import FileDescriptor
from typing import Any
from urwid import signals as signals
from urwid.command_map import REDRAW_SCREEN as REDRAW_SCREEN, command_map as command_map
from urwid.compat import PYTHON3 as PYTHON3, reraise as reraise
from urwid.display_common import INPUT_DESCRIPTORS_CHANGED as INPUT_DESCRIPTORS_CHANGED
from urwid.util import StoppingContext as StoppingContext, is_mouse_event as is_mouse_event
from urwid.wimp import PopUpTarget as PopUpTarget

PIPE_BUFFER_READ_SIZE: int

class ExitMainLoop(Exception): ...
class CantUseExternalLoop(Exception): ...

class MainLoop:
    handle_mouse: Any
    pop_ups: Any
    screen: Any
    screen_size: Any
    event_loop: Any
    def __init__(self, widget, palette=..., screen: Any | None = ..., handle_mouse: bool = ..., input_filter: Any | None = ..., unhandled_input: Any | None = ..., event_loop: Any | None = ..., pop_ups: bool = ...) -> None: ...
    widget: Any
    def set_alarm_in(self, sec, callback, user_data: Any | None = ...): ...
    def set_alarm_at(self, tm, callback, user_data: Any | None = ...): ...
    def remove_alarm(self, handle): ...
    def watch_pipe(self, callback): ...
    def remove_watch_pipe(self, write_fd): ...
    def watch_file(self, fd, callback): ...
    def remove_watch_file(self, handle): ...
    def run(self) -> None: ...
    idle_handle: Any
    def start(self): ...
    def stop(self) -> None: ...
    def process_input(self, keys): ...
    def input_filter(self, keys, raw): ...
    def unhandled_input(self, input): ...
    def entering_idle(self) -> None: ...
    def draw_screen(self) -> None: ...

class EventLoop:
    def alarm(self, seconds, callback) -> None: ...
    def enter_idle(self, callback) -> None: ...
    def remove_alarm(self, handle) -> None: ...
    def remove_enter_idle(self, handle) -> None: ...
    def remove_watch_file(self, handle) -> None: ...
    def run(self) -> None: ...
    def watch_file(self, fd, callback) -> None: ...
    def set_signal_handler(self, signum, handler): ...

class SelectEventLoop(EventLoop):
    def __init__(self) -> None: ...
    def alarm(self, seconds, callback): ...
    def remove_alarm(self, handle): ...
    def watch_file(self, fd, callback): ...
    def remove_watch_file(self, handle): ...
    def enter_idle(self, callback): ...
    def remove_enter_idle(self, handle): ...
    def run(self) -> None: ...

class GLibEventLoop(EventLoop):
    GLib: Any
    def __init__(self) -> None: ...
    def alarm(self, seconds, callback): ...
    def set_signal_handler(self, signum, handler): ...
    def remove_alarm(self, handle): ...
    def watch_file(self, fd, callback): ...
    def remove_watch_file(self, handle): ...
    def enter_idle(self, callback): ...
    def remove_enter_idle(self, handle): ...
    def run(self) -> None: ...
    def handle_exit(self, f): ...

class TornadoEventLoop(EventLoop):
    class PollProxy:
        def __init__(self, poll_obj, idle_map) -> None: ...
        def __getattr__(self, name): ...
        def poll(self, timeout): ...
    def __init__(self, ioloop: Any | None = ...) -> None: ...
    def alarm(self, secs, callback): ...
    def remove_alarm(self, handle): ...
    def watch_file(self, fd, callback): ...
    def remove_watch_file(self, handle): ...
    def enter_idle(self, callback): ...
    def remove_enter_idle(self, handle): ...
    def handle_exit(self, func): ...
    def run(self) -> None: ...
FileDescriptor = object

class TwistedInputDescriptor(FileDescriptor):
    cb: Any
    def __init__(self, reactor, fd, cb) -> None: ...
    def fileno(self): ...
    def doRead(self): ...

class TwistedEventLoop(EventLoop):
    reactor: Any
    manage_reactor: Any
    def __init__(self, reactor: Any | None = ..., manage_reactor: bool = ...) -> None: ...
    def alarm(self, seconds, callback): ...
    def remove_alarm(self, handle): ...
    def watch_file(self, fd, callback): ...
    def remove_watch_file(self, handle): ...
    def enter_idle(self, callback): ...
    def remove_enter_idle(self, handle): ...
    def run(self) -> None: ...
    def handle_exit(self, f, enable_idle: bool = ...): ...

class AsyncioEventLoop(EventLoop):
    def __init__(self, **kwargs) -> None: ...
    def alarm(self, seconds, callback): ...
    def remove_alarm(self, handle): ...
    def watch_file(self, fd, callback): ...
    def remove_watch_file(self, handle): ...
    def enter_idle(self, callback): ...
    def remove_enter_idle(self, handle): ...
    def run(self) -> None: ...
