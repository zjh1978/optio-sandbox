from sandbox.mathutil import safe_divide


def test_safe_divide():
    assert safe_divide(6, 3) == 2
