from typing import Any

def calc_text_pos(*args, **kwargs) -> Any: ...
def calc_width(*args, **kwargs) -> Any: ...
def decode_one(*args, **kwargs) -> Any: ...
def decode_one_right(*args, **kwargs) -> Any: ...
def get_byte_encoding() -> stringencoding: ...
def get_width(intord) -> intwidth: ...
def is_wide_char(*args, **kwargs) -> Any: ...
def move_next_char(*args, **kwargs) -> Any: ...
def move_prev_char(*args, **kwargs) -> Any: ...
def set_byte_encoding(stringencoding) -> None: ...
def within_double_byte(strinttext, intline_start, intpos) -> intwithindb: ...