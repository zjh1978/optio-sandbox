def safe_divide(a: float, b: float) -> float:
    """Return the quotient of a and b; a zero divisor is rejected.

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


def sign(x: float) -> int:
    """Return the sign of x: -1 if negative, 1 if positive, 0 otherwise."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def halve(x: float) -> float:
    """Return half of x."""
    return x / 2


def quarter(x: float) -> float:
    """Return a quarter of x."""
    return x / 4
