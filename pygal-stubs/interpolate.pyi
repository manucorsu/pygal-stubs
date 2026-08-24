from collections.abc import Generator, Sequence
from typing import Callable, Literal

def quadratic_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float], None, None]: ...
def cubic_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float], None, None]: ...
def hermite_interpolate(
    x: Sequence[float],
    y: Sequence[float],
    precision: int = 250,
    type: Literal[
        "cardinal", "catmull_rom", "finite_difference", "kochanek_bartels"
    ] = "cardinal",
    c: float | None = None,
    b: float | None = None,
    t: float | None = None,
) -> Generator[tuple[float, float], None, None]: ...
def lagrange_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float], None, None]: ...
def trigonometric_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float], None, None]: ...

INTERPOLATIONS: dict[str, Callable[..., Generator[tuple[float, float], None, None]]]
