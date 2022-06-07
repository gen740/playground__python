from typing import Any
from urwid import old_str_util as str_util
from urwid.compat import bytes as bytes, bytes3 as bytes3

within_double_byte: Any
SO: str
SI: str
IBMPC_ON: str
IBMPC_OFF: str
DEC_TAG: str
DEC_SPECIAL_CHARS: str
ALT_DEC_SPECIAL_CHARS: str
DEC_SPECIAL_CHARMAP: Any
SAFE_ASCII_DEC_SPECIAL_RE: Any
DEC_SPECIAL_RE: Any

class MoreInputRequired(Exception): ...

def escape_modifier(digit): ...

input_sequences: Any

class KeyqueueTrie:
    data: Any
    def __init__(self, sequences) -> None: ...
    def add(self, root, s, result): ...
    def get(self, keys, more_available): ...
    def get_recurse(self, root, keys, more_available): ...
    def read_mouse_info(self, keys, more_available): ...
    def read_cursor_position(self, keys, more_available): ...

MOUSE_RELEASE_FLAG: int
MOUSE_MULTIPLE_CLICK_MASK: int
MOUSE_MULTIPLE_CLICK_FLAG: int
MOUSE_DRAG_FLAG: int
input_trie: Any

def process_keyqueue(codes, more_available): ...

ESC: str
CURSOR_HOME: Any
CURSOR_HOME_COL: str
APP_KEYPAD_MODE: Any
NUM_KEYPAD_MODE: Any
SWITCH_TO_ALTERNATE_BUFFER: Any
RESTORE_NORMAL_BUFFER: Any
REPORT_STATUS: Any
REPORT_CURSOR_POSITION: Any
INSERT_ON: Any
INSERT_OFF: Any

def set_cursor_position(x, y): ...
def move_cursor_right(x): ...
def move_cursor_up(x): ...
def move_cursor_down(x): ...

HIDE_CURSOR: Any
SHOW_CURSOR: Any
MOUSE_TRACKING_ON: Any
MOUSE_TRACKING_OFF: Any
DESIGNATE_G1_SPECIAL: Any
ERASE_IN_LINE_RIGHT: Any
