from collections.abc import Sequence

from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from pygal.graph.line import Line as Line

class HorizontalLine(HorizontalGraph[Sequence[float | None]], Line):
    range: tuple[float, float] | list[float]
