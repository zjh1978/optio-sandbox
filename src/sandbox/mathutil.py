def safe_divide(a: float, b: float) -> float:
    """Compute a / b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def lerp(a: float, b: float, t: float) -> float:
    """Linearly interpolate between a and b.

    Returns a + (b - a) * t.

    Raises:
        ValueError: if t is outside the closed interval [0, 1].
    """
    if t < 0 or t > 1:
        raise ValueError("t must be in [0, 1]")
    return a + (b - a) * t


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0
