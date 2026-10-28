import pytest

from sandbox.mathutil import cube, lerp, safe_divide, sign


def test_safe_divide():
    assert safe_divide(6, 3) == 2


def test_safe_divide_float():
    assert safe_divide(1, 4) == 0.25


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


def test_sign_positive():
    assert sign(3.5) == 1


def test_sign_negative():
    assert sign(-2) == -1


def test_sign_zero():
    assert sign(0) == 0
    assert sign(-0.0) == 0


def test_cube():
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0
    assert cube(0.5) == 0.125
