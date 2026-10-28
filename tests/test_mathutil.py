import pytest

from sandbox.mathutil import safe_divide


def test_safe_divide():
    assert safe_divide(6, 3) == 2


def test_safe_divide_floats():
    assert safe_divide(7.5, 2.5) == 3.0
    assert safe_divide(1, 4.0) == 0.25


@pytest.mark.parametrize(
    "a, b",
    [
        ("6", 3),
        (6, "3"),
        (None, 1),
        (1, None),
        ([1], 1),
        (True, 1),
        (1, False),
        (1 + 2j, 1),
    ],
)
def test_safe_divide_rejects_non_numbers(a, b):
    with pytest.raises(TypeError, match="^operands must be numbers$"):
        safe_divide(a, b)


def test_safe_divide_by_zero_still_raises_zero_division():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)
