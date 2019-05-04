from random import randrange
import util

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    cislo_policka= randrange(0,20)
    while pole[cislo_policka]!='-':
        cislo_policka= randrange(0,20)
    return  tah(pole,cislo_policka,'o')
