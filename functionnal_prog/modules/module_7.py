"""Exercices sur module_7.recursion"""

def fibo_recursive(n):
    """
    Implantez la suite de Fibonacci définie par la formule de récurrence suivante:

    𝐹(𝑛)=01𝐹(𝑛−1)+𝐹(𝑛−2)si 𝑛=0si 𝑛=1si 𝑛>1

    Exprimez votre solution sous la forme d'une fonction récursive nommée fibo qui accepte en argument un nombre entier 𝑛 et qui retourne la valeur de 𝐹(𝑛)

    Notez que le contexte de cet exercice définit une classe nommée RecursiveCheck. Vous n'avez pas à vous soucier de cette classe ni à l'utiliser. Elle sert à l'interne pour le correcteur automatique.

    """

    return fibo_recursive(n-1) + fibo_recursive(n-2) if n > 1 else n


def fibo_non_recursive(n):
    """
    Implantez la suite de Fibonacci définie par la formule de récurrence suivante:

    𝐹(𝑛)=01𝐹(𝑛−1)+𝐹(𝑛−2)si 𝑛=0si 𝑛=1si 𝑛>1

    Exprimez votre solution sous la forme d'une fonction non récursive nommée fibo qui accepte en argument un nombre entier 𝑛
    et qui retourne la valeur de 𝐹(𝑛).
    """

    if n in (0, 1):
        return n

    liste = [0, 1]

    for _ in range(1, n):
        liste.append(liste[-1] + liste[-2])

    return liste[-1]


def fibo_generatrice(n):
    """
    Implantez la suite de Fibonacci définie par la formule de récurrence suivante:

    𝐹(𝑛)=01𝐹(𝑛−1)+𝐹(𝑛−2)si 𝑛=0si 𝑛=1si 𝑛>1

    Exprimez votre solution sous la forme d'une fonction génératrice nommée fibo qui retourne la séquence des 𝐹(𝑖), ∀𝑖≤𝑛.
    """

    def fibo():
        a, b = 0, 1

        for i in range(0, n + 1):
            if i in (0, 1):
                res = i
            else:
                res = a + b
                a, b = b, res

            yield res

    return list(fibo())[-1]
