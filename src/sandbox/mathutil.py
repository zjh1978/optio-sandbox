def safe_divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: The dividend. Must be an int or float (bool is rejected).
        b: The divisor. Must be an int or float (bool is rejected).

    Returns:
        The result of ``a / b``.

    Raises:
        TypeError: If either operand is not an int or float, or is a bool.
        ZeroDivisionError: If ``b`` is zero.
    """
    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("operands must be numbers")
    return a / b
