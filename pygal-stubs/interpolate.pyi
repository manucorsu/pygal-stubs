from collections.abc import Callable, Generator, Sequence
from typing import Literal

def quadratic_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float]]: ...
def cubic_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float]]: ...
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
) -> Generator[tuple[float, float]]: ...
def lagrange_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float]]: ...
def trigonometric_interpolate(
    x: Sequence[float], y: Sequence[float], precision: int = 250, **kwargs: object
) -> Generator[tuple[float, float]]: ...

INTERPOLATIONS: dict[str, Callable[..., Generator[tuple[float, float]]]]
