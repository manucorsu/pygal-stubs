from collections.abc import Iterable, Sequence
from datetime import date, datetime, time, timedelta
from typing import TypeVar, overload

from pygal._compat import timestamp as timestamp
from pygal.adapters import positive as positive
from pygal.config import Config
from pygal.graph.xy import XY as XY

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

_DatetimeValueT = TypeVar("_DatetimeValueT", default=Sequence[tuple[datetime, float]])
_XLabelT = TypeVar("_XLabelT", default=str)

class DateTimeLine(XY[_DatetimeValueT, _XLabelT]): ...

class DateLine(DateTimeLine[Sequence[tuple[date, float]], str | date]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        x_labels: Iterable[str | date] | None = None,
        **kwargs: object,
    ) -> None: ...

class TimeLine(DateTimeLine[Sequence[tuple[time, float]]]): ...
class TimeDeltaLine(XY[Sequence[tuple[timedelta, float]]]): ...
