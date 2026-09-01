from collections.abc import Sequence

from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from pygal.graph.stackedline import StackedLine as StackedLine

class HorizontalStackedLine(HorizontalGraph[Sequence[float]], StackedLine): ...
