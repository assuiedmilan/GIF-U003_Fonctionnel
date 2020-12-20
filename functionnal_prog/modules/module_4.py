"""Exercices sur module_4.map_filter_zip"""

def rectangle_englobant(liste):
    """
    Codez une fonction nommée rectangle_englobant qui accepte en argument un itérable de couples (𝑥,𝑦) et qui retourne le quadrulet (𝑥𝑚𝑖𝑛,𝑦𝑚𝑖𝑛,𝑥𝑚𝑎𝑥,𝑦𝑚𝑎𝑥).
    """

    coordonnes = list(zip(*liste))
    return min(coordonnes[0]), min(coordonnes[1]), max(coordonnes[0]), max(coordonnes[1])


def mymap(callable_object, iterable_object):
    """
    Définissez une fonction génératrice nommée map qui reproduit le comportement du map de la librairie standard, mais dans le cas particulier où celui-ci n'accepte qu'un seul objet itérable.
    Notez bien que dans ce cas, la fonction sur laquelle on applique le map doit aussi être restreinte à un seul argument positionnel.
    """

    for x in iterable_object:
        yield callable_object(x)


def my_generic_map(callable_object, *args):
    """
    Définissez une fonction génératrice nommée map qui reproduit le comportement du map de la librairie standard, y compris dans le cas général où celui-ci accepte en argument un nombre arbitraire d'objets itérables.
    Notez bien que la fonction sur laquelle on applique le map doit accepter un nombre d'arguments positionnels égal au nombre d'objets itérables reçus par le map.
    """

    for tuple_of_args in zip(*args):
        yield callable_object(*tuple_of_args)

def palindrome(sequence):
    """
    Définissez une fonction nommée palindrome qui accepte en argument une séquence itérable et qui retourne si oui ou non celle-ci forme un palindrome,
    c'est-à-dire une séquence qui peut être parcourue indifféremment du début vers la fin ou de la fin vers le début.
    Par exemple, la chaîne de caractères 'anana' est un palindrome.
    """

    return all(x[0] == x[1] for x in zip(sequence, reversed(sequence)))
