from pygal import Config
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.style import Style
from pygal.util import alter as alter
from pygal.util import decorate as decorate

class SolidGauge(Graph[list[dict[str, float]] | float]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        inner_radius: float | None = None,
        **kwargs: object,
    ) -> None: ...
    def gaugify(
        self,
        serie: Serie,
        squares: object,
        sq_dimensions: tuple[float, float],
        current_square: tuple[int, int],
    ) -> None: ...  # squares is never accessed so it can be anything
