from collections.abc import Sequence
from typing import Generic, TypeVar

from pygal.adapters import positive as positive
from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from pygal.graph.stackedbar import StackedBar as StackedBar

_ValueT = TypeVar(
    "_ValueT",
    default=Sequence[float | None],
)

class VerticalPyramid(StackedBar[_ValueT], Generic[_ValueT]): ...
class Pyramid(HorizontalGraph[Sequence[float | None]], VerticalPyramid): ...
