from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import alter as alter
from pygal.util import decorate as decorate

class SolidGauge(Graph):
    def gaugify(
        self,
        serie: Serie,
        squares: object,
        sq_dimensions: tuple[float, float],
        current_square: tuple[int, int],
    ) -> None: ...  # squares is never accessed so it can be anything
