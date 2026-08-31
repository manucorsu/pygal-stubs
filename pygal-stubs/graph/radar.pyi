from pygal.adapters import none_to_zero as none_to_zero
from pygal.adapters import positive as positive
from pygal.graph.line import Line as Line
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    compute_scale as compute_scale,
)
from pygal.util import (
    cut as cut,
)
from pygal.util import (
    deg as deg,
)
from pygal.util import (
    truncate as truncate,
)
from pygal.view import PolarLogView as PolarLogView
from pygal.view import PolarView as PolarView

class Radar(Line):
    def __init__(self, *args: object, **kwargs: object) -> None: ...
