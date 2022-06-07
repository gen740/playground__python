from typing import Any
from urwid.compat import B as B, PYTHON3 as PYTHON3, bytes as bytes, xrange as xrange
from urwid.util import calc_text_pos as calc_text_pos, calc_trim_text as calc_trim_text, calc_width as calc_width, is_wide_char as is_wide_char, move_next_char as move_next_char, move_prev_char as move_prev_char

class TextLayout:
    def supports_align_mode(self, align): ...
    def supports_wrap_mode(self, wrap): ...
    def layout(self, text, width, align, wrap) -> None: ...

class CanNotDisplayText(Exception): ...

class StandardTextLayout(TextLayout):
    def __init__(self) -> None: ...
    def supports_align_mode(self, align): ...
    def supports_wrap_mode(self, wrap): ...
    def layout(self, text, width, align, wrap): ...
    def pack(self, maxcol, layout): ...
    def align_layout(self, text, width, segs, wrap, align): ...
    def calculate_text_segments(self, text, width, wrap): ...

default_layout: Any

class LayoutSegment:
    text: Any
    end: Any
    def __init__(self, seg) -> None: ...
    def subseg(self, text, start, end): ...

def line_width(segs): ...
def shift_line(segs, amount): ...
def trim_line(segs, text, start, end): ...
def calc_line_pos(text, line_layout, pref_col): ...
def calc_pos(text, layout, pref_col, row): ...
def calc_coords(text, layout, pos, clamp: int = ...): ...