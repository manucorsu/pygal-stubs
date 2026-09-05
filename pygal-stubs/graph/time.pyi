from collections.abc import Callable, Iterable, Sequence
from datetime import date, datetime, time, timedelta
from typing import Generic, TypedDict, TypeVar, overload

from pygal._compat import timestamp as timestamp
from pygal.adapters import positive as positive
from pygal.config import Config
from pygal.graph.xy import XY as XY
from pygal.style import Style

_T = TypeVar("_T")

@overload
def datetime_to_timestamp(x: datetime) -> float: ...
@overload
def datetime_to_timestamp(
    x: _T,
) -> _T: ...  # if x isn't a datetime it gets returned without modification
@overload
def datetime_to_time(x: datetime) -> time: ...
@overload
def datetime_to_time(x: _T) -> _T: ...
@overload
def date_to_datetime(x: date) -> datetime: ...
@overload
def date_to_datetime(x: _T) -> _T: ...
@overload
def time_to_datetime(x: time) -> datetime: ...
@overload
def time_to_datetime(x: _T) -> _T: ...
@overload
def timedelta_to_seconds(x: timedelta) -> float: ...
@overload
def timedelta_to_seconds(x: _T) -> _T: ...
@overload
def time_to_seconds(x: time) -> float: ...
@overload
def time_to_seconds(x: str) -> str: ...
@overload
def time_to_seconds(x: float) -> float: ...
def seconds_to_time(x: float) -> time: ...

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

_DatetimeValueT = TypeVar("_DatetimeValueT", default=Sequence[tuple[datetime, float]])
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float | _AxisLabelsDict)

class DateTimeLine(XY[_DatetimeValueT, _XLabelT, _YLabelT]): ...

class DateLine(
    DateTimeLine[Sequence[tuple[date, float]], str | date, _YLabelT],
    Generic[_YLabelT],
):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        x_title: str | None = None,
        y_title: str | None = None,
        style: Style | type[Style] | None = None,
        x_labels: Iterable[str | date] | None = None,
        x_labels_major: Iterable[str] | None = None,
        x_labels_major_every: int | None = None,
        x_labels_major_count: int | None = None,
        show_minor_x_labels: bool | None = None,
        x_label_rotation: float | None = None,
        show_x_labels: bool | None = None,
        y_labels: Iterable[_YLabelT] | None = None,
        y_labels_major: Iterable[str] | None = None,
        y_labels_major_every: int | None = None,
        y_labels_major_count: int | None = None,
        show_y_labels: bool | None = None,
        show_minor_y_labels: bool | None = None,
        y_label_rotation: float | None = None,
        truncate_label: int | None = None,
        range: tuple[float, float] | list[float] | None = None,
        fill: bool | None = None,
        x_value_formatter: Callable[..., str] | None = None,
        show_legend: bool | None = None,
        legend_at_bottom: bool | None = None,
        legend_at_bottom_columns: int | None = None,
        legend_box_size: int | None = None,
        truncate_legend: int | None = None,
        **kwargs: object,
    ) -> None: ...

class TimeLine(
    DateTimeLine[Sequence[tuple[time, float]], str, _YLabelT], Generic[_YLabelT]
): ...
class TimeDeltaLine(
    XY[Sequence[tuple[timedelta, float]], str, _YLabelT], Generic[_YLabelT]
): ...
