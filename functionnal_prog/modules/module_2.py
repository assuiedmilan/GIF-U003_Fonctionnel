"""Exercices sur module_2.donnees_immuables"""

def matrice(m, n):
    """
    Définissez une fonction matrice qui accepte deux arguments 𝑚 et 𝑛 correspondant aux nombres de lignes et de colonnes d'une matrice.
    Votre fonction doit retourner une liste de 𝑚 listes composées chacune de 𝑛 zéro. Notez que 𝑚≥1 et 𝑛≥1
    """

    return [[0] * n for x in range(m)]
