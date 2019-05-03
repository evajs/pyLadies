from scitani import secti
import pytest

def test_secti_tri_a_pet():
    # vysledek = secti(3,5)
    # if vysledek !=8:
    #     raise AssertionError('Nefunguje to.')
    assert secti(0, -1)== -1, 'Nefunguje to.'

def test_cislo_a_retezec():
    try:
        secti(10,'x')
    except TypeError:
        pass
    else:
        assert False, 'nedalo to TypeError'

def test_cislo_a_retezec_dva():
    with pytest.raises(TypeError):
        secti(10, 'x')

def test_dalsi():
    pass