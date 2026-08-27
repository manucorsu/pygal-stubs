import datetime
from collections.abc import Iterable
from typing import Any, TypeGuard

def is_list_like(
    value: object,
) -> TypeGuard[Iterable[Any]]: ...  # pyright: ignore[reportExplicitAny]
def timestamp(x: datetime.datetime) -> float: ...
