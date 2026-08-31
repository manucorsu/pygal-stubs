from pygal.adapters import none_to_zero as none_to_zero
from pygal.adapters import positive as positive
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import alter as alter
from pygal.util import decorate as decorate

class Pie(Graph):
    def slice(self, serie: Serie, start_angle: float, total: float) -> float: ...
