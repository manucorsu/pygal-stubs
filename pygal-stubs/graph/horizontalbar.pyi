from collections.abc import Sequence
from typing import Literal, TypedDict

from pygal.graph.bar import Bar as Bar
from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from typing_extensions import NotRequired

class _LinkDict(TypedDict):
    href: str
    target: NotRequired[Literal["_blank", "_self", "_parent", "_top"]]

class _ConfidenceIntervalDict(TypedDict):
    type: Literal["continuous", "dichotomous"]
    sample_size: int
    stddev: NotRequired[float]
    confidence: NotRequired[float]

class _ValueDict(TypedDict):
    value: float
    label: NotRequired[str]
    style: NotRequired[str]
    xlink: NotRequired[str | _LinkDict]
    ci: NotRequired[_ConfidenceIntervalDict]

class HorizontalBar(
    HorizontalGraph[float | None | Sequence[float | None | _ValueDict], Bar]
): ...
