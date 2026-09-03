from collections.abc import Sequence

from pygal import Config
from pygal.adapters import none_to_zero as none_to_zero
from pygal.adapters import positive as positive
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import alter as alter
from pygal.util import decorate as decorate

class Pie(Graph[float | Sequence[float]]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        inner_radius: float | None = None,
        half_pie: bool | None = None,
        **kwargs: object,
    ) -> None: ...
    def slice(self, serie: Serie, start_angle: float, total: float) -> float: ...
