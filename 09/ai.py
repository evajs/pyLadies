from random import randrange
import util

def tah_pocitace(pole, symbol):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    if not '-' in pole:
        raise Exception('Počítač nemá kam hrát!')
    cislo_policka= randrange(0,20)
    while pole[cislo_policka]!='-':
        cislo_policka= randrange(0,20)
    return  util.tah(pole,cislo_policka,symbol)

# print(tah_pocitace('xxxx','x'))