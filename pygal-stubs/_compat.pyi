from collections.abc import Iterable
from typing import TypeVar, Protocol
from typing_extensions import TypeIs

_T_co = TypeVar("_T_co", covariant=True, default=object)

class _ListLikeIterable(Iterable[_T_co], Protocol):
    pass

def is_list_like(value: object) -> TypeIs[_ListLikeIterable[object]]: ...
