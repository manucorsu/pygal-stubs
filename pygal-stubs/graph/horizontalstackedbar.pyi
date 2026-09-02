from collections.abc import Sequence

from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from pygal.graph.stackedbar import StackedBar as StackedBar

class HorizontalStackedBar(
    HorizontalGraph[Sequence[float | None | Sequence[float | None]]], StackedBar
): ...
