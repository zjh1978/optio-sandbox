def safe_divide(a: float, b: float) -> float:
    """Compute a / b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def clamp(x: float, lo: float, hi: float) -> float:
    """Return x limited to the closed interval [lo, hi].

    Raises:
        ValueError: if lo > hi.
    """
    if lo > hi:
        raise ValueError("lo must be <= hi")
    return min(max(x, lo), hi)
