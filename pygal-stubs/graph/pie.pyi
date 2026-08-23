from pygal.adapters import none_to_zero as none_to_zero, positive as positive
from pygal.graph.graph import Graph as Graph
from pygal.util import alter as alter, decorate as decorate

class Pie(Graph):
    def slice(self, serie, start_angle, total): ...
