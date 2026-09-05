from collections.abc import Iterable, Sequence
from typing import TypeVar

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

_ValueT = TypeVar("_ValueT", default=float | None | Sequence[float | None])
_XLabelT = TypeVar("_XLabelT", default=str)

class Bar(Graph[_ValueT, _XLabelT]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        x_labels: Iterable[_XLabelT] | None = None,
        **kwargs: object,
    ) -> None: ...
    def bar(self, serie: Serie, rescale: bool = False) -> None: ...
