from piskvorky import vyhodnot
from ai import tah_pocitace
from util import tah
import pytest

def test_vyhnoceni_krizky():
    assert vyhodnot('xxx----oo--x-oo-----')=='x'

def test_vyhnoceni_kolecka():
    assert vyhodnot('xx-----ooo-x-oo-----') == 'o'

def test_vyhnoceni_remiza():
    assert vyhodnot('xxooxxooxxoxxooxxoox') == '!'

def test_vyhnoceni_nekonec():
    assert vyhodnot('xx------oo-x-oo-----') == '-'

def test_tah_pocitace_kolecko():
    assert tah_pocitace('xx------o--x-oo-----').count('o') == 4;

def test_tah_pocitace_ubylo_pradnych():
    assert tah_pocitace('xx------o--x-oo-----').count('-') == 13;

def test_tah_pocitace_najde_prazdne():
    assert tah_pocitace('xxooxxooxxoxxooxxo-x') == 'xxooxxooxxoxxooxxoox'

def test_tah_krizek():
    assert tah('xx------o--x-oo-----', 2, 'x') == 'xxx-----o--x-oo-----'

def test_tah_kolecko():
    assert tah('xx------o--x-oo-----', 2, 'o') == 'xxo-----o--x-oo-----'

