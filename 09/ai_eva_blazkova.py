from random import randrange
from util import tah


def nejdelsi_volny_prostor(pole):
    "Vrací pozici začátku a délku nejdelšího úseku -"

    nejdelsi_zacina = 0
    nejdelsi_delka = 0
    aktualni_zacina = 0
    aktualni_delka = 0
    for i in range(len(pole)):
        if pole[i] == '-':
            if i - aktualni_delka != aktualni_zacina:
                aktualni_zacina = i
            aktualni_delka += 1
        else:
            if aktualni_delka > nejdelsi_delka:
                nejdelsi_delka = aktualni_delka
                nejdelsi_zacina = aktualni_zacina
                aktualni_delka = 0
            else:
                aktualni_delka = 0
    if aktualni_delka > nejdelsi_delka:
        nejdelsi_delka = aktualni_delka
        nejdelsi_zacina = aktualni_zacina
    return (nejdelsi_zacina, nejdelsi_delka)


def tah_pocitace(pole, symbol):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    # zkontroluje, zda je kam hrat
    if not '-' in pole:
        raise Exception('Počítač nemá kam hrát!')

    # zjisti, za co hraje protihrac
    if symbol == 'o':
        symbol_protihrace = 'x'
    else:
        symbol_protihrace = 'o'

    #protihrac ma dve
    if '-' + symbol_protihrace*2 in pole:
        cislo_policka = pole.index('-' + symbol_protihrace*2)
    elif  symbol_protihrace*2 +'-' in pole:
        cislo_policka = pole.index(symbol_protihrace*2 +'-') +2
    elif  symbol_protihrace +'-' + symbol_protihrace in pole:
        cislo_policka = pole.index(symbol_protihrace +'-' + symbol_protihrace) +1
    # ja mam dve
    elif '-' + symbol*2 in pole:
        cislo_policka = pole.index('-' + symbol*2)
    elif  symbol*2 + '-' in pole:
        cislo_policka = pole.index(symbol*2 + '-') +2
    elif symbol + '-' + symbol in pole:
        cislo_policka = pole.index(symbol + '-' + symbol) +1
    # protihrac ma jednu
    elif  symbol + '-' + symbol_protihrace + '--' in pole:
        cislo_policka = pole.index(symbol + '-' + symbol_protihrace + '--') + 3
    elif  symbol + '-' + symbol_protihrace + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index(symbol + '-' + symbol_protihrace + '-' + symbol_protihrace) + 1
    elif  '--' + symbol_protihrace + '-' + symbol in pole:
        cislo_policka = pole.index('--' + symbol_protihrace + '-' + symbol) + 1
    elif  '--' + symbol_protihrace + '--' in pole:
        cislo_policka = pole.index('--' + symbol_protihrace + '--') + 1
    #okrajove varianty pole
    elif '-' + symbol_protihrace + '--' in pole:
        cislo_policka = pole.index( '-' + symbol_protihrace + '--') + 2
    elif '-' + symbol_protihrace + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index('-' + symbol_protihrace + '-' + symbol_protihrace)
    elif '--' + symbol_protihrace + '-' in pole:
        cislo_policka = pole.index('--' + symbol_protihrace + '-') + 1
    # ja mam jednu
    elif symbol_protihrace + '-' + symbol + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index(symbol_protihrace + '-' + symbol + '-' + symbol_protihrace) + 1
    elif symbol_protihrace + '-' + symbol + '--' in pole:
        cislo_policka = pole.index(symbol_protihrace + '-' + symbol + '--') + 4
    elif '--' + symbol + '-' in pole:
        cislo_policka = pole.index('--' + symbol + '-')
    # okrajove varianty pole
    elif '-' + symbol + '--' in pole:
        cislo_policka = pole.index('-' + symbol + '--')+3
    elif '-' + symbol + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index('-' + symbol + '-' + symbol_protihrace)+2
    else:
        volno = nejdelsi_volny_prostor(pole)
        cislo_policka = randrange(volno[0],volno[0]+ volno[1])
    return  tah(pole,cislo_policka,symbol)


