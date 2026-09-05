from collections.abc import Callable, Iterable, Sequence
from typing import Literal, TypedDict, TypeVar

from pygal import Config
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.style import Style
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    decorate as decorate,
)
from pygal.util import (
    ident as ident,
)
from pygal.util import (
    swap as swap,
)
from typing_extensions import NotRequired, Self, override

class _LinkDict(TypedDict):
    href: str
    target: NotRequired[Literal["_blank", "_self", "_parent", "_top"]]

class _ConfidenceIntervalDict(TypedDict):
    type: Literal["continuous", "dichotomous"]
    sample_size: int
    stddev: NotRequired[float]
    confidence: NotRequired[float]

class _ValueDict(TypedDict):
    value: float
    label: NotRequired[str]
    xlink: NotRequired[str | _LinkDict]
    ci: NotRequired[_ConfidenceIntervalDict]

_ValueT = TypeVar("_ValueT", default=float | None | Sequence[float | None | _ValueDict])
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float)

class Bar(Graph[_ValueT, _XLabelT, _YLabelT]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        pretty_print: bool | None = None,
        x_labels: Iterable[_XLabelT] | None = None,
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
        rounded_bars: int | None = None,
        value_formatter: Callable[[object], str] | None = None,
        **kwargs: object,
    ) -> None: ...
    def bar(self, serie: Serie, rescale: bool = False) -> None: ...
    @override
    def add(
        self,
        title: str,
        values: _ValueT,
        *,
        rounded_bars: int | None = None,
        formatter: Callable[[object], str] | None = None,
        **kwargs: object,
    ) -> Self: ...
    @override
    def render_table(
        self,
        *,
        style: bool | None = None,
        total: bool | None = None,
        transpose: bool | None = None,
        **kwargs: object,
    ) -> str: ...
