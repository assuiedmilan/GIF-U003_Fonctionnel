"""
Écrivez le code source d'une fonction nommée compter qui accepte en argument un objet itérable dont les éléments sont potentiellement eux-mêmes itérables, récursivement, et qui retourne le nombre total d'objets. Votre fonction doit reconnaître quatre types particuliers d'objets :

    la liste:
    le tuple:
    l'ensemble:
    et le dictionnaire.

Votre fonction doit initialiser une variable pour accumuler le compte, puis itérer sur les éléments de l'itérable. Lorsqu'un élément correspond à l'un ou l'autre des types ci-dessus, votre fonction doit ajouter au compte le résultat d'un traitement particulier sur cet élément. Autrement, pour tout autre élément, elle ajoute simplement la valeur 1 au compte actuel.

Dans le cas d'une liste ou d'un tuple, le traitement consiste à faire un appel récursif directement sur l'objet. Dans le cas d'un ensemble, le traitement consiste à déterminer le nombre d'éléments de l'ensemble. Dans le cas d'un dictionnaire, le traitement consiste à faire un appel récursif sur les valeurs de l'objet.

À la fin de l'itération, la fonction retourne simplement la valeur du compte accumulé. Par exemple :

compter([1, [2, [3, 4, 5], {'a': 6, 'b': (7, 8, 9), 'c': {'x': 10}}], (11, 12)])

doit retourner 12.
"""

def compter(iterable_object):

    count = 0
    for item in iterable_object:
        if isinstance(item, (list, tuple, set)):
            count += compter(item)
        elif isinstance(item, dict):
            count += compter(item.values())
        else:
            count += 1

    return count

x = compter([1, [2, [3, 4, 5], {'a': 6, 'b': (7, 8, 9), 'c': {'x': 10}}], (11, 12)])
print(x)