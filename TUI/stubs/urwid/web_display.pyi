from typing import Any
from urwid import util as util

ALARM_DELAY: int
POLL_CONNECT: int
MAX_COLS: int
MAX_ROWS: int
MAX_READ: int
BUF_SZ: int

class Screen:
    palette: Any
    has_color: bool
    def __init__(self) -> None: ...
    started: Any
    def register_palette(self, l) -> None: ...
    def register_palette_entry(self, name, foreground, background, mono: Any | None = ...) -> None: ...
    def set_mouse_tracking(self, enable: bool = ...) -> None: ...
    def tty_signal_keys(self, *args, **vargs) -> None: ...
    last_screen: Any
    last_screen_width: int
    update_method: Any
    pipe_name: Any
    input_fd: Any
    input_tail: str
    content_head: Any
    def start(self): ...
    def stop(self) -> None: ...
    def set_input_timeouts(self, *args) -> None: ...
    def run_wrapper(self, fn): ...
    def draw_screen(self, size, r) -> None: ...
    def clear(self) -> None: ...
    def get_cols_rows(self): ...
    def get_input(self, raw_keys: bool = ...): ...

def code_span(s, fg, bg, cursor: int = ...): ...
def html_escape(text): ...
def is_web_request(): ...
def handle_short_request(): ...

class _Preferences:
    app_name: str
    pipe_dir: str
    allow_polling: bool
    max_clients: int

def set_preferences(app_name, pipe_dir: str = ..., allow_polling: bool = ..., max_clients: int = ...) -> None: ...

class ErrorLog:
    errfile: Any
    def __init__(self, errfile) -> None: ...
    def write(self, err) -> None: ...

def daemonize(errfile) -> None: ...
