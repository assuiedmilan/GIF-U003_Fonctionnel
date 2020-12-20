"""Exercices sur module_1.prog_fonctionnelle"""

import datetime

from typing import List, Dict


def echo(first_positional: int, second_positional: int, *, karg1=1, karg2=2, karg3=3) -> tuple:
    """
    Définissez une fonction nommée écho qui accepte en entrée deux arguments positionnels et trois arguments obligatoirement nommés.
    Les noms de vos arguments obligatoirement nommés doivent être karg1, karg2, et karg3.
    Donnez respectivement à ces trois arguments les valeurs par défaut 1, 2 et 3.

    Par ailleurs, votre fonction doit retourner un tuple contenant dans l'ordre les valeurs des cinq arguments reçues.

    """

    return first_positional, second_positional, karg1, karg2, karg3


def compute_serie(r: int, n: int) -> float:
    """
    Soit la série 𝑆

    définie par la formule suivante:

    𝑆(𝑟,𝑛)==∑𝑖=1𝑛1(1+𝑟)𝑖1(1+𝑟)1+1(1+𝑟)2+⋯+1(1+𝑟)𝑛−1+1(1+𝑟)𝑛

    où 𝑟≠−1 est une valeur réelle et 𝑛≥1 est une valeur entière.

    Définissez une fonction Python qui calcule cette série. Nommez votre fonction S et faites en sorte qu'elle accepte en argument des valeurs pour 𝑟
    et 𝑛 (dans cet ordre). Assurez-vous aussi de toujours retourner une valeur en virgule flottante. Par exemple, l'expression S(3, 5) doit retourner la valeur 0.3330078125.
    """

    if r == -1 or n < 1:
        raise ValueError

    values = (1 / ((1 + r) ** i) for i in range(1, n + 1))
    return sum(values)


def valeur_portefeuille(list_of_titles: List[tuple], valeurs: Dict[str, int], current_date: datetime = None) -> float:
    """
    Définissez une fonction nommée valeur_portefeuille qui accepte trois arguments:

        une liste de titres achetés à différentes dates, les éléments de cette liste étant des tuples (date, quantité, titre),
            où date (instance de datetime.date) correspond à la date d'achat d'une quantité quantité de titre titre;
        un dictionnaire contenant les valeurs des titres (on suppose ici des valeurs constantes dans le temps);
        la date (instance de datetime.date) pour laquelle on veut établir la valeur du portefeuille.

    En absence de date (3e argument), votre fonction doit retourner la valeur totale de tous les achats contenus dans le portefeuille.
    Donnez la valeur par défaut None à cet argument.
    Si une date est spécifiée, votre fonction ne doit pas tenir compte des achats postérieurs à cette date dans le calcul de la valeur du portefeuille.
    """

    limit_date = current_date if current_date else datetime.date.today()
    considered_list_of_titles = [x for x in list_of_titles if x[0] <= limit_date]
    return sum(x[1] * valeurs[x[2]] for x in considered_list_of_titles if x[2] in valeurs)


def conversion_binaire(binary_value: str) -> int:
    """
    Définissez une fonction nommé bin2int qui accepte en argument une chaîne de caractères ne contenant que des zéros et des uns, autrement dit une chaîne qui représente un nombre exprimé en base 2, c'est-à-dire un nombre composé exclusivement de chiffres 0 et 1, et qui retourne le nombre entier (int) équivalent. Par exemple, 1101 en base 2 correspond à 13 en base 10.

    Plus formellement, la représentation binaire d'un nombre constitué des chiffres 𝑏𝑛⋯𝑏𝑖⋯𝑏1𝑏0, avec 𝑏𝑖∈{0,1}∀𝑖, peut être convertie en nombre décimal grâce au calcul suivant:

    𝑏𝑛×2𝑛+⋯+𝑏𝑖×2𝑖+𝑏1×21+𝑏0×20=∑𝑖=0𝑛𝑏𝑖×2𝑖

    Votre fonction doit calculer cette somme pour une chaîne binaire de longueur arbitraire. Dans le cas particulier d'une chaîne vide, votre fonction doit retourner zéro.
    """

    size_of_value = len(binary_value)

    return sum(2**(size_of_value -1 - x) * int(binary_value[x]) for x in range(size_of_value))\
        if binary_value else 0


def signature(**kwargs):
    """
    Définissez une fonction nommée signature qui accepte un nombre arbitraire d'arguments nommés, et qui retourne la signature de ces arguments,
    c'est-à-dire la chaîne de caractères qui énumère les noms et les valeurs de ces arguments, séparés par des virgules.

    Par exemple, si vous faites l'appel signature(a=1, b=2, c=3), la fonction doit retourner la chaîne 'a=1, b=2, c=3'.

    Indices: utilisez l'argument doublement étoilé pour les arguments nommés; utilisez la méthode str.join pour joindre des chaînes de caractères.

    Notez bien que votre fonction doit retourner une chaîne et non afficher sa valeur.
    """

    signatures = ["{}={}".format(x, y) for x, y in kwargs.items()]
    return ', '.join(signatures)


def est_occupee(case, occupations):
    """
    Définissez une fonction nommée est_occupée qui accepte en entrée deux arguments:

        un couple (𝑖,𝑗)

    spécifiant respectivement les indices de ligne et de colonne d'une case d'un damier;
    une liste de dictionnaires décrivant l'ensemble des jetons actuellement présents sur le damier;

    où chaque dictionnaire de la liste contient exactement les trois clés suivantes:

        'jeton' associé au symbole du jeton;
        'ligne' associé à l'indice de ligne du jeton;
        'colonne' associé à l'indice de colonne du jeton.

    Votre fonction doit retourner un booléen indiquant si oui ou non la case (𝑖,𝑗)
    du damier est actuellement occupée par un jeton.
    """

    for element in occupations:
        if case == (element['ligne'], element['colonne']):
            return True

    return False
