from random import randrange

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

# print(vyhodnot('xxoxoxoxxooxxooxxooxooo'))
# print(vyhodnot('-------xxx----------'))
# print(vyhodnot('-------xxox----------'))
# print(vyhodnot('xxoxxoxxooxxoo'))

def zamen(retezec, pozice, znak):
    """Zamění znak na dané pozici

    Vrátí řetězec, který má na dané pozici daný znak;
    jinak je stejný jako vstupní retezec
    """
    return retezec[:pozice] + znak + retezec[pozice + 1:]


def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    pole = zamen(pole,cislo_policka, symbol)
    return pole

# print(tah('x------x------------', 1, 'o'))

def tah_hrace(pole):
    cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
    while cislo_policka<0 or cislo_policka>=20:
        print('{} není v rozsahu hracího pole. Zadej číslo od 0 do 19.'.format(cislo_policka))
        cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
    while pole[cislo_policka]!='-':
        print('Pole {} je obsazené'.format(cislo_policka))
        cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
    return tah(pole,cislo_policka,'x')

# print(tah_hrace('x------x------------'))

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    cislo_policka= randrange(0,20)
    while pole[cislo_policka]!='-':
        cislo_policka= randrange(0,20)
    return  tah(pole,cislo_policka,'o')

# print(tah_pocitace('xxxxxxxxxxxxxxxxxxx-'))

def piskvorky1d():
    pole='--------------------'
    stav_hry = '-'
    hraje = 1
    while stav_hry == '-':
        if hraje==1:
            pole = tah_hrace(pole)
            print(pole)
            hraje =2
        else:
            pole = tah_pocitace(pole)
            print(pole)
            hraje =1
        stav_hry = vyhodnot(pole)
    if stav_hry =='x':
        print('Vyhrál jsi. Gratulujeme.')
    elif stav_hry =='o':
        print('Vyhrál počítač.')
    elif stav_hry == '!':
        print('Remíza.')

piskvorky1d()

