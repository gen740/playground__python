from typing import Any
from urwid import escape as escape
from urwid.compat import bytes as bytes, text_type as text_type, text_types as text_types

str_util: Any
calc_text_pos: Any
calc_width: Any
is_wide_char: Any
move_next_char: Any
move_prev_char: Any
within_double_byte: Any

def detect_encoding(): ...

detected_encoding: Any

def set_encoding(encoding) -> None: ...
def get_encoding_mode(): ...
def apply_target_encoding(s): ...
def supports_unicode(): ...
def calc_trim_text(text, start_offs, end_offs, start_col, end_col): ...
def trim_text_attr_cs(text, attr, cs, start_col, end_col): ...
def rle_get_at(rle, pos): ...
def rle_subseg(rle, start, end): ...
def rle_len(rle): ...
def rle_prepend_modify(rle, a_r) -> None: ...
def rle_append_modify(rle, a_r) -> None: ...
def rle_join_modify(rle, rle2) -> None: ...
def rle_product(rle1, rle2): ...
def rle_factor(rle): ...

class TagMarkupException(Exception): ...

def decompose_tagmarkup(tm): ...
def is_mouse_event(ev): ...
def is_mouse_press(ev): ...

class MetaSuper(type):
    def __init__(cls, name, bases, d) -> None: ...

def int_scale(val, val_range, out_range): ...

class StoppingContext:
    def __init__(self, wrapped) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...