from collections.abc import Sequence
from typing import Generic, TypeVar

from pygal.adapters import none_to_zero as none_to_zero
from pygal.graph.bar import Bar as Bar

_ValueT = TypeVar(
    "_ValueT",
    default=Sequence[float | None | Sequence[float | None]],
)

class StackedBar(Bar[_ValueT], Generic[_ValueT]): ...
