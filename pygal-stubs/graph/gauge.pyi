from _typeshed import Incomplete
from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    compute_scale as compute_scale,
)
from pygal.util import (
    cut as cut,
)
from pygal.util import (
    decorate as decorate,
)
from pygal.view import (
    PolarThetaLogView as PolarThetaLogView,
)
from pygal.view import (
    PolarThetaView as PolarThetaView,
)

class Gauge(Graph):
    needle_width: Incomplete
    def needle(self, serie): ...
