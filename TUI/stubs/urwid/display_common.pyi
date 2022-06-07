from typing import Any
from urwid import signals as signals
from urwid.compat import B as B, bytes3 as bytes3, with_metaclass as with_metaclass, xrange as xrange
from urwid.util import StoppingContext as StoppingContext, int_scale as int_scale

UNPRINTABLE_TRANS_TABLE: Any
UPDATE_PALETTE_ENTRY: str
INPUT_DESCRIPTORS_CHANGED: str
DEFAULT: str
BLACK: str
DARK_RED: str
DARK_GREEN: str
BROWN: str
DARK_BLUE: str
DARK_MAGENTA: str
DARK_CYAN: str
LIGHT_GRAY: str
DARK_GRAY: str
LIGHT_RED: str
LIGHT_GREEN: str
YELLOW: str
LIGHT_BLUE: str
LIGHT_MAGENTA: str
LIGHT_CYAN: str
WHITE: str

class AttrSpecError(Exception): ...

class AttrSpec:
    foreground: Any
    background: Any
    def __init__(self, fg, bg, colors: int = ...) -> None: ...
    foreground_basic: Any
    foreground_high: Any
    foreground_true: Any
    foreground_number: Any
    background_basic: Any
    background_high: Any
    background_true: Any
    background_number: Any
    italics: Any
    bold: Any
    underline: Any
    blink: Any
    standout: Any
    strikethrough: Any
    colors: Any
    def get_rgb_values(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__: Any

class RealTerminal:
    def __init__(self) -> None: ...
    def tty_signal_keys(self, intr: Any | None = ..., quit: Any | None = ..., start: Any | None = ..., stop: Any | None = ..., susp: Any | None = ..., fileno: Any | None = ...): ...

class ScreenError(Exception): ...

class BaseScreen:
    signals: Any
    def __init__(self) -> None: ...
    started: Any
    def start(self, *args, **kwargs): ...
    def stop(self) -> None: ...
    def run_wrapper(self, fn, *args, **kwargs): ...
    def register_palette(self, palette) -> None: ...
    def register_palette_entry(self, name, foreground, background, mono: Any | None = ..., foreground_high: Any | None = ..., background_high: Any | None = ...): ...
