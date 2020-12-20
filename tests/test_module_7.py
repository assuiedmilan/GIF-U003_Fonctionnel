import pytest

from functionnal_prog.modules.module_7 import fibo_generatrice
from functionnal_prog.modules.module_7 import fibo_non_recursive
from functionnal_prog.modules.module_7 import fibo_recursive


@pytest.mark.parametrize("callable_object", [fibo_recursive, fibo_non_recursive, fibo_generatrice])
@pytest.mark.parametrize("n, expected_value", [
    (0, 0),
    (1, 1),
    (2, 1),
    (5, 5),
    (10, 55)
])
def test_fibonacci(n, expected_value, callable_object):
    assert callable_object(n) == expected_value
