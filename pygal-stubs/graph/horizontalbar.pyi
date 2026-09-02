from collections.abc import Sequence

from pygal.graph.bar import Bar as Bar
from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph

class HorizontalBar(HorizontalGraph[float | None | Sequence[float | None]], Bar): ...
