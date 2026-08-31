from collections.abc import Iterable
from datetime import datetime
from typing import Protocol, TypeVar

from typing_extensions import TypeIs

_T_co = TypeVar("_T_co", covariant=True, default=object)

class _ListLikeIterable(Iterable[_T_co], Protocol): ...

def is_list_like(value: object) -> TypeIs[_ListLikeIterable[object]]: ...
def timestamp(x: datetime) -> float: ...
