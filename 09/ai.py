from random import randrange
import util

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
        print('case 1')
    elif  symbol_protihrace*2 +'-' in pole:
        cislo_policka = pole.index(symbol_protihrace*2 +'-') +2
        print('case 2')
    elif  symbol_protihrace +'-' + symbol_protihrace in pole:
        cislo_policka = pole.index(symbol_protihrace +'-' + symbol_protihrace) +1
        print('case 3')
    # ja mam dve
    elif '-' + symbol*2 in pole:
        cislo_policka = pole.index('-' + symbol*2)
        print('case 4')
    elif  symbol*2 + '-' in pole:
        cislo_policka = pole.index(symbol*2 + '-') +2
        print('case 5')
    elif symbol + '-' + symbol in pole:
        cislo_policka = pole.index(symbol + '-' + symbol) +1
        print('case 6')
    # protihrac ma jednu
    elif  symbol + '-' + symbol_protihrace + '--' in pole:
        cislo_policka = pole.index(symbol + '-' + symbol_protihrace + '--') + 3
        print('case 7')
    elif  symbol + '-' + symbol_protihrace + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index(symbol + '-' + symbol_protihrace + '-' + symbol_protihrace) + 1
        print('case 8')
    elif  '--' + symbol_protihrace + '-' + symbol in pole:
        cislo_policka = pole.index('--' + symbol_protihrace + '-' + symbol) + 1
        print('case 9')
    elif  '--' + symbol_protihrace + '--' in pole:
        cislo_policka = pole.index('--' + symbol_protihrace + '--') + 1
        print('case 10')
    elif '-' + symbol_protihrace + '--' in pole:
        cislo_policka = pole.index( '-' + symbol_protihrace + '--') + 2
        print('case 7a')
    elif '-' + symbol_protihrace + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index(7'-' + symbol_protihrace + '-' + symbol_protihrace)
        print('case 8a')
    elif  '--' + symbol_protihrace + '-' in pole:
        cislo_policka = pole.index('--' + symbol_protihrace + '-') + 1
        print('case 9b')
    # mam jednu
    elif symbol_protihrace + '-' + symbol + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index(symbol_protihrace + '-' + symbol + '-' + symbol_protihrace) + 1
        print('case 11')
    elif symbol_protihrace + '-' + symbol + '--' in pole:
        cislo_policka = pole.index(symbol_protihrace + '-' + symbol + '--') + 4
        print('case 12')
    elif '--' + symbol + '-' in pole:
        cislo_policka = pole.index('--' + symbol + '-')
        print('case 13')
    elif '-' + symbol + '--' in pole:
        cislo_policka = pole.index('-' + symbol + '--')+3
        print('case 13a')
    elif '-' + symbol + '-' + symbol_protihrace in pole:
        cislo_policka = pole.index('-' + symbol + '-' + symbol_protihrace)+2
        print('case 13b')
    else:
        volno = nejdelsi_volny_prostor(pole)
        cislo_policka = randrange(volno[0],volno[0]+ volno[1])
        while pole[cislo_policka]!='-':
            cislo_policka = randrange(volno[0],volno[0]+ volno[1])
        #print(volno)
        print('case 14')
    return  util.tah(pole,cislo_policka,symbol)

# print(tah_pocitace('xxxx','x'))

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
            #print(aktualni_zacina, aktualni_delka)
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
    return  (nejdelsi_zacina, nejdelsi_delka)

#print(nejdelsi_volny_prostor('-x----oxxo-xo-------'))