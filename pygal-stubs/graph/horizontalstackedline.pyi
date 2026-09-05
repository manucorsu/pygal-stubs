from collections.abc import Sequence
from typing import TypedDict

from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from pygal.graph.stackedline import StackedLine as StackedLine

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

class HorizontalStackedLine(
    HorizontalGraph[Sequence[float | None], str, str | float | _AxisLabelsDict],
    StackedLine[Sequence[float | None], str, str | float | _AxisLabelsDict],
): ...
