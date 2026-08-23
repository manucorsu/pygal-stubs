from pygal.graph.graph import Graph as Graph
from pygal.util import alter as alter, decorate as decorate

class SolidGauge(Graph):
    def gaugify(self, serie, squares, sq_dimensions, current_square) -> None: ...
