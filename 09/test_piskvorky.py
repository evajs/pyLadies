from piskvorky import vyhodnot
import pytest

def test_vyhnoceni_krizky():
    assert vyhodnot('xxx----oo--x-oo-----')=='x'