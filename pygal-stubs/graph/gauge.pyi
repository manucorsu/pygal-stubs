from pygal import Config
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
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

class Gauge(Graph[float]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        human_readable: bool | None = None,
        reverse_direction: bool | None = None,
        **kwargs: object,
    ) -> None: ...
    needle_width: float
    def needle(self, serie: Serie) -> None: ...
