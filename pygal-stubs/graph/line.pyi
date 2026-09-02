from collections.abc import Iterable, Sequence

from pygal import Config
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

class Line(Graph[Sequence[float | None]]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        x_labels: Iterable[str] | None = None,
        x_labels_major: Iterable[str] | None = None,
        x_label_rotation: float | None = None,
        range: tuple[float, float] | list[float] | None = None,
        fill: bool | None = None,
        **kwargs: object,
    ) -> None: ...
    def line(self, serie: Serie, rescale: bool = False) -> None: ...
