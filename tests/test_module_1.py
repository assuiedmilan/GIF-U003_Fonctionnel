import datetime

import pytest

from functionnal_prog.modules.module_1 import compute_serie
from functionnal_prog.modules.module_1 import conversion_binaire
from functionnal_prog.modules.module_1 import echo
from functionnal_prog.modules.module_1 import est_occupee
from functionnal_prog.modules.module_1 import signature
from functionnal_prog.modules.module_1 import valeur_portefeuille


def test_echo():
    with pytest.raises(TypeError):
        echo(1, 2, 3)  # pylint: disable=too-many-function-args

    assert echo(1, 2) == (1, 2, 1, 2, 3)
    assert echo(1, 2, karg1=4, karg2=6, karg3=9) == (1, 2, 4, 6, 9)

def test_compute_serie():
    assert compute_serie(3, 5) == 0.3330078125


def test_valeur_portefeuille():
    valeurs = {'a': 5, 'b': 10, 'c': 1}
    list_of_titles = [
        (datetime.date(2018, 1, 1), 10, 'a'),
        (datetime.date(2018, 1, 1), 1, 'b'),
        (datetime.date(2018, 1, 1), 100, 'c'),
        (datetime.date(2020, 1, 1), 100, 'c')
    ]


    assert valeur_portefeuille(list_of_titles, valeurs) == 260
    assert valeur_portefeuille(list_of_titles, valeurs, datetime.date(2019, 1, 1)) == 160


def test_conversion_binaire():
    assert conversion_binaire('1101100101') == 869


def test_signature():
    assert signature(a=1, b=2, c=3) == 'a=1, b=2, c=3'


@pytest.mark.parametrize("case, occupancies, expected_value", [
    ((1, 1), [{'jeton': 'A', 'ligne': 0, 'colonne': 2}, {'jeton': 'B', 'ligne': 1, 'colonne': 1}, {'jeton': 'C', 'ligne': 2, 'colonne': 0}], True),
    ((3, 1), [{'jeton': 'A', 'ligne': 0, 'colonne': 2}, {'jeton': 'B', 'ligne': 1, 'colonne': 1}, {'jeton': 'C', 'ligne': 2, 'colonne': 0}], False),
])
def test_occupation(case, occupancies, expected_value):
    assert est_occupee(case, occupancies) == expected_value
