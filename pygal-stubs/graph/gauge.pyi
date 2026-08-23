from _typeshed import Incomplete
from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
    compute_scale as compute_scale,
    cut as cut,
    decorate as decorate,
)
from pygal.view import (
    PolarThetaLogView as PolarThetaLogView,
    PolarThetaView as PolarThetaView,
)

class Gauge(Graph):
    needle_width: Incomplete
    def needle(self, serie): ...
