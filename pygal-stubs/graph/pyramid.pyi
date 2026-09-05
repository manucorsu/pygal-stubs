from collections.abc import Iterable, Sequence
from typing import Generic, Literal, TypeVar

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
        pretty_print: bool | None = None,
        x_labels: Iterable[str] | None = None,
        width: int | None = None,
        height: int | None = None,
        explicit_size: bool | None = None,
        spacing: int | None = None,
        margin: int | None = None,
        margin_top: int | None = None,
        margin_right: int | None = None,
        margin_bottom: int | None = None,
        margin_left: int | None = None,
        print_values: bool | None = None,
        dynamic_print_values: bool | None = None,
        print_values_position: Literal["top", "bottom"] | str | None = None,
        print_zeroes: bool | None = None,
        print_labels: bool | None = None,
        human_readable: bool | None = None,
        no_data_text: str | None = None,
        legend_at_bottom: bool | None = None,
        rounded_bars: int | None = None,
        **kwargs: object,
    ) -> None: ...
