from typing import Any
from urwid import escape as escape
from urwid.compat import PYTHON3 as PYTHON3, bytes as bytes, ord2 as ord2, text_type as text_type, xrange as xrange
from urwid.display_common import AttrSpec as AttrSpec, BaseScreen as BaseScreen, RealTerminal as RealTerminal, UNPRINTABLE_TRANS_TABLE as UNPRINTABLE_TRANS_TABLE

KEY_RESIZE: int
KEY_MOUSE: int

class Screen(BaseScreen, RealTerminal):
    curses_pairs: Any
    palette: Any
    has_color: bool
    s: Any
    cursor_state: Any
    prev_input_resize: int
    last_bstate: int
    def __init__(self) -> None: ...
    def set_mouse_tracking(self, enable: bool = ...) -> None: ...
    max_tenths: Any
    complete_tenths: Any
    resize_tenths: Any
    def set_input_timeouts(self, max_wait: Any | None = ..., complete_wait: float = ..., resize_wait: float = ...): ...
    def get_input(self, raw_keys: bool = ...): ...
    def get_cols_rows(self): ...
    keep_cache_alive_link: Any
    def draw_screen(self, size, r) -> None: ...
    def clear(self) -> None: ...

class _test:
    ui: Any
    l: Any
    def __init__(self) -> None: ...
    def run(self) -> None: ...
