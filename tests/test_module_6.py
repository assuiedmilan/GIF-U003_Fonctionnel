import pytest

from functionnal_prog.modules.module_6 import factorielle


@pytest.mark.parametrize("n, expected_value", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (10, 3628800),
    pytest.param(-1, 0, marks=pytest.mark.xfail(raises=ValueError))
])
def test_facturielle(n, expected_value):
    assert factorielle(n) == expected_value