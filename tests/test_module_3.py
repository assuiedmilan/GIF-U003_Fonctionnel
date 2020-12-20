from functionnal_prog.modules.module_3 import calculer_distances
from functionnal_prog.modules.module_3 import calculer_factures
from functionnal_prog.modules.module_3 import grouper_produits


def test_grouper_produits():
    produits = [
        ("outil", "râteaux"),
        ("fruit", "pommes"),
        ("fruit", "fraises"),
        ("légume", "courgettes"),
        ("fleur", "roses"),
        ("légume", "tomates"),
        ("outil", "pelles"),
        ("électroménager", "fours"),
        ("légume", "champignons"),
        ("fleur", "tullipes")
    ]

    assert grouper_produits(produits) == [
        ('fleur', ('roses', 'tullipes')),
        ('fruit', ('fraises', 'pommes')),
        ('légume', ('champignons', 'courgettes', 'tomates')),
        ('outil', ('pelles', 'râteaux')),
        ('électroménager', ('fours',)),
    ]


def test_calculer_distances():
    villes = [
        ("Uneville", 4, 10),
        ("Villeautre", 10, 15),
        ("Idéedeville", 20, 2),
        ("Encoreuneville", 14, 14)
    ]

    assert calculer_distances(villes) == [
        ('Uneville', 'Villeautre', 7.810249675906654),
        ('Uneville', 'Idéedeville', 17.88854381999832),
        ('Uneville', 'Encoreuneville', 10.770329614269007),
        ('Villeautre', 'Idéedeville', 16.401219466856727),
        ('Villeautre', 'Encoreuneville', 4.123105625617661),
        ('Idéedeville', 'Encoreuneville', 13.416407864998739)
    ]

def test_calculer_factures():
    zoe = [35, 49, 10, 43, 1, 46, 15, 23, 22, 50, 1, 28, 39, 5, 7, 42, 41, 7, 12]
    leo = [15, 4, 49, 7, 24, 8, 23, 17, 20, 27, 3, 37, 39, 11, 3, 3, 11]
    bob = [21, 13, 42, 29, 40, 23, 3, 41, 18, 12, 37, 11, 7, 18, 12, 49, 49, 9]

    assert calculer_factures(zoe, leo, bob) == 78
