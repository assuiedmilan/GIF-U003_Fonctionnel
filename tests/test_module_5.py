import pytest

from functionnal_prog.modules.module_5 import FiltreAntiMarques


@pytest.mark.parametrize("x, y, z", [
    pytest.param("coke", "toto", "tata"),
    pytest.param("titi", "faNta", "tata"),
    pytest.param('titi', "toto", "OranGina")
])
def test_filtre_anti_marques(x, y, z):

    @FiltreAntiMarques
    def fct(a, b, c):
        print(a, b, c)

    with pytest.raises(ValueError):
        fct(x, y, z)

    with pytest.raises(ValueError):
        fct(x, y, c=z)

    with pytest.raises(ValueError):
        fct(x, b=y, c=z)

    with pytest.raises(ValueError):
        fct(a=x, b=y, c=z)

    fct("toto", "titi", "tata")
