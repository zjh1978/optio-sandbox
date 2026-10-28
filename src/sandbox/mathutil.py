def safe_divide(a: float, b: float) -> float:
    """Compute a / b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b
