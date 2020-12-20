"""Exercices sur module_5.decorateurs"""


def obsolète(callable_object):
    """
    Définissez un décorateur nommé obsolète qui affiche à la console le message suivant avant d'appeler la fonction décorée:

    "Cette fonction est obsolète, vous ne devriez plus l'appeler!"

    Faites en sorte que votre décorateur puisse décorer n'importe quelle fonction et implantez-le sous la forme d'une fonction et non d'une classe.
    """

    def f(*args, **kwargs):
        print("Cette fonction est obsolète, vous ne devriez plus l'appeler!")
        return callable_object(*args, **kwargs)

    return f


class FiltreAntiMarques:
    """
    Définissez une classe nommé FiltreAntiMarques permettant de décorer n'importe quelle fonction recevant un nombre arbitraire d'arguments positionnels ou nommés.
    Votre décorateur doit analyser tous les arguments reçus et s'assurer qu'aucun d'entre eux n'est une chaîne de caractères appartenant à l'ensemble:

    {'coke', 'fanta', 'orangina', 'pepsi', 'sprite'}

    Rendez votre filtre invariant à la casse (majuscule vs minuscule) des chaînes de caractères.
    Si un argument de la fonction décorée correspond à l'une ou l'autre des chaînes de l'ensemble, votre fonction doit soulever une exception de type ValueError avec le message suivant dans le cas d'un argument positionnel:

        ValueError: l'argument 'val' est interdit où val est la valeur de l'argument; et le message suivant dans le cas d'un argument nommé:
        ValueError: l'argument 'nom=val' est interdit où nom est le nom de l'argument et val sa valeur. Par exemple, le code suivant:

            @FiltreAntiMarques
            def fct(a, b, c):
                print(a, b, c)

            fct('Bonjour', 'le', c='Fanta')

            devrait soulever une exception avec le message: ValueError: l'argument 'c=Fanta' est interdit
    """

    __FILTRE = {'coke', 'fanta', 'orangina', 'pepsi', 'sprite'}

    def __init__(self, fct):
        self.fct = fct

    def __call__(self, *args, **kwargs):

        def find(x):
            return [i for i, j in enumerate(x) if j.lower() in self.__FILTRE]

        first = find(args)
        second = find(kwargs.values())

        if first:
            raise ValueError("ValueError: l'argument '{}' est interdit".format(args[first[0]]))
        if second:
            raise ValueError("ValueError: l'argument '{}={}' est interdit".format(
                list(kwargs.keys())[second[0]],
                list(kwargs.values())[second[0]])
            )

        return self.fct(*args, **kwargs)
