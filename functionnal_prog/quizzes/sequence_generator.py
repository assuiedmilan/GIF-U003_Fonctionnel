from math import factorial

import pytest


def generateur(z, n):
    """Définissez une fonction génératrice nommée generateur qui accepte en argument deux paramètres 𝑧 et 𝑛
    (dans cet ordre) et qui produit la séquence des valeurs:

    (−1)𝑘⋅𝑧2𝑘+1(2𝑘+1)!,pour tous les𝑘pris dans1,2,…,𝑛,

    où désigne la multiplication et 𝑥! représente la factorielle de 𝑥. Pour calculer la factorielle, vous pouvez faire appel à la fonction factorial du module standard math."""

    for k in range(1, n+1):
        yield (-1)**k * z**(2*k+1) / factorial(2*k + 1)

@pytest.mark.parametrize("z, n, expected_value", [
    (2, 3, [-1.3333333333333333, 0.26666666666666666, -0.025396825396825397])
])
def test_generator(z, n, expected_value):
    assert list(generateur(z, n)) == expected_value
