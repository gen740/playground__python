import typing
from . import events

async def staggered_race(coro_fns: typing.Iterable[typing.Callable[[], typing.Awaitable]], delay: typing.Optional[float], *, loop: events.AbstractEventLoop = ...) -> typing.Tuple[typing.Any, typing.Optional[int], typing.List[typing.Optional[Exception]]]: ...
