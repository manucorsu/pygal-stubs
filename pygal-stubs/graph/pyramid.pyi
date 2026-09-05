from collections.abc import Sequence
from typing import Generic, TypeVar

from pygal import Config
from pygal.adapters import positive as positive
from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from pygal.graph.stackedbar import StackedBar as StackedBar
from pygal.style import Style

_ValueT = TypeVar(
    "_ValueT",
    default=Sequence[float | None],
)

class VerticalPyramid(StackedBar[_ValueT], Generic[_ValueT]): ...

class Pyramid(HorizontalGraph[Sequence[float | None]], VerticalPyramid):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        human_readable: bool | None = None,
        legend_at_bottom: bool | None = None,
        **kwargs: object,
    ) -> None: ...
