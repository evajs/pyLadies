from piskvorky import vyhodnot
from ai import tah_pocitace
from util import tah
from piskvorky import over_vstup
from piskvorky import jak_to_dopadlo
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
    assert tah_pocitace('xx------o--x-oo-----', 'o').count('o') == 4;

def test_tah_pocitace_krizek():
    assert tah_pocitace('xx------o--x-oo-----', 'x').count('x') == 4;

def test_tah_pocitace_ubylo_pradnych():
    assert tah_pocitace('xx------o--x-oo-----', 'o').count('-') == 13;

def test_tah_pocitace_najde_prazdne():
    assert tah_pocitace('xxooxxooxxoxxooxxo-x', 'o') == 'xxooxxooxxoxxooxxoox'

def test_tah_krizek():
    assert tah('xx------o--x-oo-----', 2, 'x') == 'xxx-----o--x-oo-----'

def test_tah_kolecko():
    assert tah('xx------o--x-oo-----', 2, 'o') == 'xxo-----o--x-oo-----'

def test_over_vstup_obsazeno():
    assert over_vstup('xx------o--x-oo-----', 1) == ('Pole 1 je obsazené.', True)

def test_over_vstup_mimo():
    assert over_vstup('xx------o--x-oo-----', -1) == ('-1 není v rozsahu hracího pole. Zadej číslo od 0 do 19.', True)

def test_over_vstup_ok():
    assert over_vstup('xx------o--x-oo-----', 2) == ('2 je dostupný tah.', False)

def test_jak_to_dopadlo_krizky():
    assert jak_to_dopadlo('x') == 'Vyhrál jsi. Gratulujeme.'

def test_jak_to_dopadlo_remiza():
    assert jak_to_dopadlo('!') == 'Remíza.'

def test_jak_to_dopadlo_kolecka():
    assert jak_to_dopadlo('o') == 'Vyhrál počítač.'

def test_tah_pocitace_jina_delka():
    assert tah_pocitace('xx-------oo-----x-x-o-o----xx', 'o').count('o') == 5

def test_tah_pocitace_prazdne_pole():
    try:
        tah_pocitace('','x')
    except Exception:
        pass
    else:
        assert False

def test_tah_pocitace_plne_pole():
    try:
        tah_pocitace('xoxoooxoxo','x')
    except Exception:
        pass
    else:
        assert False