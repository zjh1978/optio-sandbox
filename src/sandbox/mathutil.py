def safe_divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b
