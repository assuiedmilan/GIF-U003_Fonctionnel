import pytest

from functionnal_prog.modules.module_4 import my_generic_map
from functionnal_prog.modules.module_4 import mymap
from functionnal_prog.modules.module_4 import palindrome
from functionnal_prog.modules.module_4 import rectangle_englobant


def test_rectangle_englobant():
    liste = [(1, 5), (3, 2), (0, 0), (1, 3), (2, 3), (2, 2), (4, 2), (1, 0), (4, 1), (1, 1)]
    assert rectangle_englobant(liste) == (0, 0, 4, 3)

@pytest.mark.parametrize("callable_object, iterable_object, expected_value", [
    (lambda x: x**2, range(5), [0, 1, 4, 9, 16]),
    (len, ['a', 'ab', 'abc', 'abcd'], [1, 2, 3, 4])
])
def test_mymap(callable_object, iterable_object, expected_value):
    assert list(mymap(callable_object, iterable_object)) == expected_value

def test_my_generic_mac():
    assert list(my_generic_map(lambda x, y: x+y, range(1, 6), range(3, 8))) == [4, 6, 8, 10, 12]

@pytest.mark.parametrize("value, expected_result", [
    ('aa', True),
    ('anana', True),
    ('dapodas', False)
])
def test_palindrome(value, expected_result):
    assert palindrome(value) == expected_result
