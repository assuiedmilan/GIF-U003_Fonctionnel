"""
Définissez un décorateur nommé horodateur qui, à chaque appel de la fonction décorée, affiche la date de l'appel ainsi que la valeur de ses arguments.
Implantez votre décorateur sous la forme d'une fonction qui accepte en argument une autre fonction.

Sur une même ligne, le format d'affichage doit comprendre les éléments suivants:

    la date du jour sous le format jj/mm/aaaa;
    un espace;
    le nom de la fonction décorée;
    une parenthèse ouvrante;
    les arguments positionnels utilisés lors de l'appel, séparés par des virgules
    les arguments nommés utilisés lors de l'appel, séparés par des virgules
    une parenthèse fermante.
"""

from datetime import date

def horodateur(callable_object):

    def f(*args, **kwargs):

        today = date.today().strftime('%d/%m/%Y')
        l_args = [str(x) for x in args]
        l_args += ['{}={}'.format(k, v) for k, v in sorted(zip(kwargs.keys(), kwargs.values()))]
        l_args = ', '.join(l_args)

        print('{} {}({})'.format(today, callable_object.__name__, l_args))
        return callable_object(*args, **kwargs)

    return f
