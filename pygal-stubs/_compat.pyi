import datetime
from typing import Any, Iterable

from typing_extensions import TypeGuard

def is_list_like(
    value: object,
) -> TypeGuard[Iterable[Any]]: ...  # pyright: ignore[reportExplicitAny]
def timestamp(x: datetime.datetime) -> float: ...
