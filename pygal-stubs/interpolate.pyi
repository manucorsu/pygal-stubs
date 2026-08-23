from _typeshed import Incomplete
from collections.abc import Generator

def quadratic_interpolate(
    x, y, precision: int = 250, **kwargs
) -> Generator[Incomplete]: ...
def cubic_interpolate(
    x, y, precision: int = 250, **kwargs
) -> Generator[Incomplete]: ...
def hermite_interpolate(
    x, y, precision: int = 250, type: str = "cardinal", c=None, b=None, t=None
) -> Generator[Incomplete, None, Incomplete]: ...
def lagrange_interpolate(
    x, y, precision: int = 250, **kwargs
) -> Generator[Incomplete]: ...
def trigonometric_interpolate(
    x, y, precision: int = 250, **kwargs
) -> Generator[Incomplete]: ...

INTERPOLATIONS: Incomplete
