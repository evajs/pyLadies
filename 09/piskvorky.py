import util

def tah_hrace(pole):
    cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
    while cislo_policka<0 or cislo_policka>=20:
        print('{} není v rozsahu hracího pole. Zadej číslo od 0 do 19.'.format(cislo_policka))
        cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
    while pole[cislo_policka]!='-':
        print('Pole {} je obsazené'.format(cislo_policka))
        cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
    return util.tah(pole,cislo_policka,'x')

def vyhodnot(pole):
    konec = True
    kolecka = 0
    krizky = 0
    for znak in pole:
        if znak=='-':
            konec = False
            kolecka = 0
            krizky = 0
        elif znak == 'x':
            krizky = krizky+1
            if krizky>=3:
                return 'x'
            kolecka = 0
        elif znak =='o':
            kolecka = kolecka+1
            if kolecka >= 3:
                return 'o'
            krizky = 0
    if konec:
        return '!'
    else:
        return '-'