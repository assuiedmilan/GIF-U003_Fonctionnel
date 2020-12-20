"""
Écrivez le code Python d'une fonction nommée puissance(x, n), qui élève un nombre 𝑥 à la puissance entière 𝑛

, en utilisant la formule de récurrence :

𝑥𝑛=1𝑥(𝑥⋅𝑥)𝑛/2𝑥⋅(𝑥⋅𝑥)(𝑛−1)/2si 𝑛=0si 𝑛=1si 𝑛 est pairsi 𝑛 est impair

Implantez votre fonction en utilisant la récursion (ne PAS utiliser l'opérateur **). Dans le cas d'un exposant négatif, votre fonction doit soulever une exception de type ValueError.
"""

def puissance(x, n):

    if n < 0:
        raise ValueError

    if n == 0:
        return 1

    if n == 1:
        return x

    if (n % 2) == 0:
        return puissance(x * x, n/2)
    else:
        return x * puissance(x * x, (n-1)/2)

print(puissance(2, 8))