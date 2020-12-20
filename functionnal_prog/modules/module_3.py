"""Exercices sur module_3.donnes_iterables"""
import math
from itertools import chain
from itertools import combinations
from itertools import groupby
from itertools import islice
from itertools import product


def grouper_produits(object_to_group):
    """
    Soit une liste de couples (catégorie, produit) telle que celle définie dans le contexte de cet exercice.
    On vous demande d'écrire une fonction nommée grouper_produits qui à partir d'une telle liste produit en sortie
    une nouvelle liste de couples (catégorie, tuple de produits), où chaque catégorie n'apparaît qu'une seule fois.
    """

    def data_type(data_tupple):
        return data_tupple[0]

    return [(key, tuple(x[1] for x in group))
            for key, group in groupby(sorted(object_to_group), key=data_type)]



villes = [
    ("Uneville", 4, 10),
    ("Villeautre", 10, 15),
    ("Idéedeville", 20, 2),
    ("Encoreuneville", 14, 14)
]


def calculer_distances(liste_de_villes):
    """
    Soit une liste de villes telle que celle donnée en exemple dans le contexte de cet exercice. Chaque triplet de cette liste comporte le nom d'une ville ainsi que les coordonnées (𝑥,𝑦)
    de son emplacement sur la carte.

    On vous demande d'écrire une fonction nommée calculer_distances qui accepte en argument une telle liste de villes et qui retourne en sortie une nouvelle liste de triplets pour chaque combinaison de deux villes. Les triplets de sortie doivent comporter les information suivantes :

        le nom d'une première ville
        le nom d'une seconde ville
        la distance entre les deux villes en question.
    """

    def distance(x1, x2, y1, y2):
        """Calculer la distance entre les coordonnées (x1, y1) et (x2, y2)."""
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    def calculer_distance(tuple_de_villes):
        return (tuple_de_villes[0][0], tuple_de_villes[1][0],
                distance(tuple_de_villes[0][1],
                         tuple_de_villes[1][1],
                         tuple_de_villes[0][2],
                         tuple_de_villes[1][2]))

    return [calculer_distance(x) for x in list(combinations(liste_de_villes, 2))]


def calculer_factures(*args):
    """
    Un groupe d'amis part en vacances et décide de partager toutes leurs dépenses.
    Les dépenses de chacun sont conservées dans trois itérables de montants (voir cellule de contexte).

    L'un des membres du groupe n'ayant pas beaucoup d'argent, le groupe décide de lui faire une faveur:
    il ne payerera que les 15 factures les moins chères parmi toutes les factures réunies.

    Retournez le montant total des factures qu'il devra payer.
    """
    return sum(islice(sorted(chain(*args)), 15))


def damier(lignes, colonnes):
    """
    L'objectif de cet exercice est d'initialiser un damier tel que ci-contre.

    Dans le contexte de cet exercice, nous vous donnons des itérables pour les lignes et les colonnes du damier:

        les lignes sont représentées par des chiffres de 1 à 10 (du bas vers le haut)
    les colonnes par des lettres de 𝑎 à 𝑗(de gauche à droite).

    Définissez une fonction damier qui renvoie le plateau dans le contexte d'un début de partie, prenant en argument les listes lignes et colonnes correspondant aux indices donnés à ces dernières.
    Cette fonction renverra un dictionnaire qui accepte comme clé un tuple (ligne, colonne), par exemple : (1, "a")
    et associez à chacune de ces cases les valeurs 'blanc', 'noir' ou None selon la couleur du jeton de la case de la case.

    Pour résoudre cet exercice, faites une boucle sur le produit (voir product) des deux itérables lignes et colonne.
    """

    def couleur(case):
        """Retourner la couleur de la case; None si vide."""
        ligne, colonne = case

        def is_white():
            return (colonne in 'acegi' and ligne in (1, 3)) or (colonne not in 'acegi' and ligne in (2, 4))

        def is_black():
            return (colonne in 'acegi' and ligne in (7, 9)) or (colonne not in 'acegi' and ligne in (8, 10))

        return 'blanc' if is_white() else 'noir' if is_black() else None

    return {key: couleur(key) for key in product(lignes, colonnes)}
