"""Exercices sur module_6.fonctions_superieures"""
from functools import partial
from functools import reduce


def factorielle(n):
    """
    Écrivez une fonction nommée factorielle qui accepte un entier 𝑛≥1 en argument, et qui retourne la valeur de la factorielle 𝑛!

    Pour rappel, la factorielle se définit par: 𝑛!=1∗2∗3∗…∗(𝑛−2)∗(𝑛−1)∗𝑛

    Pour produire la solution de cet exercice, faites appel à fonction reduce du module functools.
    """

    if n < 0:
        raise ValueError

    if n == 0:
        return 1

    return reduce(lambda x, y: x*y, range(1, n+1))


def polynôme(a, b, c, x):
    """
    Écrivez une fonction nommée polynôme qui accepte en argument a, b, c et x (dans cet ordre) et qui retourne la valeur du polynôme du second degré ax2+bx+c.
    """

    return a*x**2 + b*x + c

def polyor(x):
    """
    En utilisant la fonction partial du module functools, créez une fonction nommée polyor prenant en entrée x et renvoyant le polynôme x2−x−1.

    Notez que l'équation x2−x−1=0 a pour particularité d'avoir le nombre d'or comme racine, d'où le nom de polyor pour la fonction.
    """

    return partial(polynôme, 1, -1, -1)(x)
