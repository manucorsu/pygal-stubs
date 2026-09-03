from collections.abc import Sequence
from typing import Generic, TypeVar

from pygal.graph.dual import Dual as Dual
from pygal.graph.line import Line as Line
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    compose as compose,
)
from pygal.util import (
    ident as ident,
)

_XYValueT = TypeVar("_XYValueT", default=Sequence[tuple[float | None, float | None]])
_XLabelT = TypeVar("_XLabelT", default=str)

class XY(
    Line[_XYValueT, _XLabelT],
    Dual[_XYValueT, _XLabelT],
    Generic[_XYValueT, _XLabelT],
):
    @cached_property
    def xvals(self) -> list[float]: ...
    @cached_property
    def yvals(self) -> list[float]: ...
