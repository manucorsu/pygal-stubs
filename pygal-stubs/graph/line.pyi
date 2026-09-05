from collections.abc import Callable, Iterable, Sequence
from typing import Generic, TypeVar

from pygal import Config
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.style import Style
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    decorate as decorate,
)

_ValueT = TypeVar("_ValueT", default=Sequence[float | None])
_XLabelT = TypeVar("_XLabelT", default=str)

class Line(Graph[_ValueT, _XLabelT], Generic[_ValueT, _XLabelT]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        x_title: str | None = None,
        y_title: str | None = None,
        style: Style | type[Style] | None = None,
        x_labels: Iterable[str] | None = None,
        x_labels_major: Iterable[str] | None = None,
        x_label_rotation: float | None = None,
        range: tuple[float, float] | list[float] | None = None,
        fill: bool | None = None,
        x_value_formatter: Callable[..., str] | None = None,
        **kwargs: object,
    ) -> None: ...
    def line(self, serie: Serie, rescale: bool = False) -> None: ...
