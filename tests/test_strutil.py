from sandbox.strutil import shout


def test_shout():
    assert shout("hello") == "HELLO!"


def test_shout_empty():
    assert shout("") == "!"


def test_shout_already_upper():
    assert shout("HI there") == "HI THERE!"
