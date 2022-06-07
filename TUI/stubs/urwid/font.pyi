from typing import Any
from urwid.canvas import TextCanvas as TextCanvas
from urwid.compat import text_type as text_type
from urwid.escape import SAFE_ASCII_DEC_SPECIAL_RE as SAFE_ASCII_DEC_SPECIAL_RE
from urwid.util import apply_target_encoding as apply_target_encoding, str_util as str_util

def separate_glyphs(gdata, height): ...
def get_all_fonts(): ...
def add_font(name, cls) -> None: ...

class Font:
    char: Any
    canvas: Any
    utf8_required: bool
    def __init__(self) -> None: ...
    def add_glyphs(self, gdata) -> None: ...
    def characters(self): ...
    def char_width(self, c): ...
    def char_data(self, c): ...
    def render(self, c): ...

class Thin3x3Font(Font):
    height: int
    data: Any

class Thin4x3Font(Font):
    height: int
    data: Any

class HalfBlock5x4Font(Font):
    height: int
    data: Any

class HalfBlock6x5Font(Font):
    height: int
    data: Any

class HalfBlockHeavy6x5Font(Font):
    height: int
    data: Any

class Thin6x6Font(Font):
    height: int
    data: Any

class HalfBlock7x7Font(Font):
    height: int
    data: Any
