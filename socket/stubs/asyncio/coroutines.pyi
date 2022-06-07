from _typeshed import Incomplete

class CoroWrapper:
    gen: Incomplete
    func: Incomplete
    __name__: Incomplete
    __qualname__: Incomplete
    def __init__(self, gen, func: Incomplete | None = ...) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    def send(self, value): ...
    def throw(self, type, value: Incomplete | None = ..., traceback: Incomplete | None = ...): ...
    def close(self): ...
    @property
    def gi_frame(self): ...
    @property
    def gi_running(self): ...
    @property
    def gi_code(self): ...
    def __await__(self): ...
    @property
    def gi_yieldfrom(self): ...
    def __del__(self) -> None: ...

def coroutine(func): ...
def iscoroutinefunction(func): ...
def iscoroutine(obj): ...