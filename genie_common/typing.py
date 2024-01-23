from typing import Union, Tuple, Callable, Any, Awaitable

Json = Union[dict, list]
Image = Tuple[int, int, int, int]
AF = Callable[[Any, Any], Awaitable[Any]]
F = Callable[[Any], Any]
