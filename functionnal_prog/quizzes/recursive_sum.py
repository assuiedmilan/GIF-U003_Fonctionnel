"""
Définissez une fonction nommée somme capable de récursivement faire la somme des éléments d'un objet itérable, y compris les éléments qui sont eux-mêmes itérables. Autrement dit, lorsque les éléments de l'itérable sont des nombres (types int ou float), la fonction n'a qu'à les sommer, mais lorsqu'un élément est itérable, la fonction doit faire un appel récursif sur celui-ci afin de récursivement sommer ses éléments. Plus précisément, votre fonction doit traiter les cas particuliers suivants :

    lorsqu'un élément est un nombre entier ou à virgule flottante, ajoutez simplement ce nombre à votre somme ;
    lorsqu'un élément est un tuple, une liste ou un ensemble, ajoutez à votre somme le résultat d'un appel récursif sur cet élément ;
    lorsqu'un élément est un dictionnaire, ajoutez à votre somme le résultat d'un appel récursif sur l'itérable des valeurs de cet élément (voir la méthode values) ;
    lorsqu'un élément est une chaîne de caractères, ignorez simplement cet élément ;
    lorsqu'un élément est un tableau numpy (numpy.ndarray), ajouter à votre somme la somme des éléments du tableau (voir la méthode sum) ;
    pour toute autre type d'élément, soulevez une exception de type TypeError.

"""
import numpy


def somme(iterable_object):

    count = 0
    for item in iterable_object:
        if isinstance(item, (int, float)):
            count += item
        elif isinstance(item, (list, tuple, set)):
            count += somme(item)
        elif isinstance(item, dict):
            count += somme(item.values())
        elif isinstance(item, str):
            count += 0
        elif isinstance(item, numpy.ndarray):
            count += numpy.sum(item)
        else:
            raise TypeError

    return count

v = [
  'cool',
  [1, {'a': {2, 3, 4, 5}, 'b':[{1: [6, 7], 2: 'nop'}]}, 3.14],
  numpy.array([1, 2, 3, 4]).reshape((2,2))
]

print(somme(v))