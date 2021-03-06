import ai_eva_blazkova
import util

# def tah_hrace(pole):
#     cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
#     while cislo_policka<0 or cislo_policka>=20 or pole[cislo_policka]!='-':
#         if cislo_policka<0 or cislo_policka>=20:
#             print('{} není v rozsahu hracího pole. Zadej číslo od 0 do 19.'.format(cislo_policka))
#         elif pole[cislo_policka]!='-':
#             print('Pole {} je obsazené'.format(cislo_policka))
#         cislo_policka = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
#     return util.tah(pole,cislo_policka,'x')

def over_vstup(pole, vstup):
    novy_vstup = False
    if vstup<0 or vstup>=20:
        novy_vstup = True
        return '{} není v rozsahu hracího pole. Zadej číslo od 0 do 19.'.format(vstup), novy_vstup
    elif pole[vstup]!='-':
        novy_vstup = True
        return 'Pole {} je obsazené.'.format(vstup), novy_vstup
    else:
        return '{} je dostupný tah.'.format(vstup), novy_vstup

# def vyhodnot(pole):
#     konec = True
#     kolecka = 0
#     krizky = 0
#     for znak in pole:
#         if znak=='-':
#             konec = False
#             kolecka = 0
#             krizky = 0
#         elif znak == 'x':
#             krizky = krizky+1
#             if krizky>=3:
#                 return 'x'
#             kolecka = 0
#         elif znak =='o':
#             kolecka = kolecka+1
#             if kolecka >= 3:
#                 return 'o'
#             krizky = 0
#     if konec:
#         return '!'
#     else:
#         return '-'

def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' in pole:
        return '-'
    else:
        return '!'

# print(vyhodnot('xxooxxooxxoxxooxxoo-'))

def jak_to_dopadlo(stav_hry):
    if stav_hry =='x':
        hlaska='Vyhrál jsi. Gratulujeme.'
    elif stav_hry =='o':
        hlaska='Vyhrál počítač.'
    elif stav_hry == '!':
        hlaska='Remíza.'
    return hlaska