from collections.abc import Sequence
from typing import TypeAlias

from pygal.graph.bar import Bar as Bar
from pygal.graph.dual import Dual as Dual
from pygal.serie import Serie
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    decorate as decorate,
)
from typing_extensions import override

_HistValue: TypeAlias = tuple[float | None, float | None, float | None]

class Histogram(Dual[Sequence[_HistValue]], Bar[Sequence[_HistValue]]):
    @cached_property
    def xvals(self) -> list[float]: ...
    @cached_property
    def yvals(self) -> list[float]: ...
    @override
    def bar(self, serie: Serie, rescale: bool = False) -> None: ...
