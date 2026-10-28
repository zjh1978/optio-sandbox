import pytest

from sandbox.mathutil import clamp, safe_divide


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


def test_clamp_normal():
    assert clamp(5, 0, 10) == 5


def test_clamp_below():
    assert clamp(-1, 0, 10) == 0


def test_clamp_above():
    assert clamp(15, 0, 10) == 10


def test_clamp_lo_greater_than_hi():
    with pytest.raises(ValueError, match=r"^lo must be <= hi$"):
        clamp(1, 10, 0)
