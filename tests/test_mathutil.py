import pytest

from sandbox.mathutil import lerp, safe_divide


def test_safe_divide():
    assert safe_divide(6, 3) == 2


def test_safe_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="division by zero"):
        safe_divide(1, 0)


def test_safe_divide_by_float_zero_raises_value_error():
    with pytest.raises(ValueError, match="division by zero"):
        safe_divide(1.5, 0.0)


def test_safe_divide_zero_numerator():
    assert safe_divide(0, 5) == 0


def test_lerp_endpoints():
    assert lerp(0, 10, 0) == 0
    assert lerp(0, 10, 1) == 10


def test_lerp_midpoint():
    assert lerp(0, 10, 0.5) == 5


def test_lerp_negative_values():
    assert lerp(-10, -2, 0) == -10
    assert lerp(-10, -2, 1) == -2
    assert lerp(-10, 10, 0.5) == 0


def test_lerp_t_below_zero_raises_value_error():
    with pytest.raises(ValueError, match="t must be in \\[0, 1\\]"):
        lerp(0, 1, -0.01)


def test_lerp_t_above_one_raises_value_error():
    with pytest.raises(ValueError, match="t must be in \\[0, 1\\]"):
        lerp(0, 1, 1.01)


def test_g1():
    assert safe_divide(4, 2) == 2
