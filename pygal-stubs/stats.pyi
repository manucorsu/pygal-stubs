def erfinv(x: float, a: float = 0.147) -> float: ...
def norm_ppf(x: float) -> float: ...
def ppf(x: float, n: int) -> float: ...
def confidence_interval_continuous(
    point_estimate: float,
    stddev: float,
    sample_size: int,
    confidence: float = 0.95,
    **kwargs: object,
) -> tuple[float, float]: ...
def confidence_interval_dichotomous(
    point_estimate: float,
    sample_size: int,
    confidence: float = 0.95,
    bias: bool = False,
    percentage: bool = True,
    **kwargs: object,
) -> tuple[float, float]: ...
def confidence_interval_manual(
    point_estimate: object, low: float, high: float
) -> tuple[float, float]: ...
