from collections.abc import Iterable, Mapping
from typing import Generic

from pygal import stats as stats
from pygal._compat import is_list_like as is_list_like
from pygal.graph.public import PublicApi as PublicApi
from pygal.interpolate import INTERPOLATIONS as INTERPOLATIONS
from pygal.serie import Serie
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
    decorate as decorate,
)
from pygal.util import (
    filter_kwargs as filter_kwargs,
)
from pygal.util import (
    get_text_box as get_text_box,
)
from pygal.util import (
    get_texts_box as get_texts_box,
)
from pygal.util import (
    majorize as majorize,
)
from pygal.util import (
    rad as rad,
)
from pygal.util import (
    reverse_text_len as reverse_text_len,
)
from pygal.util import (
    split_title as split_title,
)
from pygal.util import (
    truncate as truncate,
)
from pygal.view import (
    LogView as LogView,
)
from pygal.view import (
    ReverseView as ReverseView,
)
from pygal.view import (
    View as View,
)
from pygal.view import (
    XYLogView as XYLogView,
)
from typing_extensions import TypeVar

_ValueT = TypeVar(
    "_ValueT",
    default=Iterable[object] | Mapping[object, object] | object,
)
_XLabelT = TypeVar("_XLabelT", default=str)

class Graph(PublicApi[_ValueT, _XLabelT], Generic[_ValueT, _XLabelT]):
    @property
    def all_series(self) -> list[Serie]: ...
    def add_squares(self, squares: tuple[int, int]) -> tuple[float, float]: ...
