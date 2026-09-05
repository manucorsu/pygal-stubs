from collections.abc import Iterable, Sequence
from typing import TypeVar

from pygal.config import Config
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    decorate as decorate,
)
from pygal.util import (
    safe_enumerate as safe_enumerate,
)
from pygal.view import ReverseView as ReverseView
from pygal.view import View as View

_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float)

class Dot(Graph[Sequence[float], _XLabelT, _YLabelT]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        pretty_print: bool | None = None,
        x_labels: Iterable[_XLabelT] | None = None,
        x_label_rotation: float | None = None,
        **kwargs: object,
    ) -> None: ...
    def dot(self, serie: Serie, r_max: float) -> None: ...
