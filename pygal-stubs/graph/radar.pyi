from pygal.adapters import none_to_zero as none_to_zero, positive as positive
from pygal.graph.line import Line as Line
from pygal.util import (
    cached_property as cached_property,
    compute_scale as compute_scale,
    cut as cut,
    deg as deg,
    truncate as truncate,
)
from pygal.view import PolarLogView as PolarLogView, PolarView as PolarView

class Radar(Line):
    def __init__(self, *args, **kwargs) -> None: ...
