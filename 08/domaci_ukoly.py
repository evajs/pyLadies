############ ukol 0 ##################
# def mocniny(n):
#     seznam = [];
#     for i in range(n):
#         seznam.append((i+1,(i+1)**2))
#     return dict(seznam)

def mocniny(n):
    seznam = {};
    for i in range(n):
        seznam[i+1] = (i+1)**2
    return seznam


# print(mocniny(4))

############ ukol 1 ##################
def vypis_slovnik(slovnik):
    for klic,hodnota in slovnik.items():
        print('Klíč {}, hodnota {}'.format(klic,hodnota))

# vypis_slovnik(mocniny(4))

############ ukol 2 ##################
def soucet_klicu_a_hodnot(slovnik):
    soucet_hodnot=0
    soucet_klicu=0
    for klic,hodnota in slovnik.items():
        soucet_hodnot = soucet_hodnot+hodnota
        soucet_klicu = soucet_klicu+klic
    return soucet_klicu,soucet_hodnot

# print(soucet_klicu_a_hodnot(mocniny(4)))

############ ukol 3 ##################
# def pocet_znaku(retezec):
#     seznam_znaku = list(retezec)
#     pocty_znaku = {}
#     for znak in seznam_znaku:
#         pocty_znaku.setdefault(znak, seznam_znaku.count(znak))
#     return pocty_znaku

def pocet_znaku(retezec):
    pocty_znaku = {}
    for znak in retezec:
        if znak in pocty_znaku.keys():
            pocty_znaku[znak] = pocty_znaku[znak]+1
        else: pocty_znaku[znak] = 1
    return pocty_znaku

print(pocet_znaku('hello world'))

############ ukol 4 ##################
# import random
# otazky = ['Kdo? ', 'S kým? ', 'Co dělali? ', 'Kde? ', 'Kdy? ', 'Proč? ']
# pocet_otazek = len(otazky)
# vsechny_odpovedi = []
# for i in range(pocet_otazek):
#     jeste = 'ano'
#     odpovedi =[]
#     while jeste=='ano':
#         odpoved = str(input(otazky[i]))
#         odpovedi.append(odpoved)
#         while True:
#             jeste = str(input('Další odpověď? '))
#             if not (jeste=='ano' or jeste=='ne'):
#                 print('Odpovídej ano nebo ne.')
#             else: break
#     vsechny_odpovedi.append(odpovedi)
# for i in range(pocet_otazek):
#     print(random.choice(vsechny_odpovedi[i]), end=' ')

############ ukol 5 ##################
def mapa_tecek(velikost):
    mapa=[]
    for cislo_radku in range(velikost):
        radek = []
        for cislo_sloupce in range(velikost):
            radek.append('.')
        mapa.append(radek)
    return mapa

def nakresli_mapu(seznam_krizku):
    velikost_mapy = 10
    mapa=mapa_tecek(velikost_mapy)
    for krizek in seznam_krizku:
        mapa[krizek[1]][krizek[0]]='X'
    for cislo_radku in range(velikost_mapy):
        for cislo_sloupce in range(velikost_mapy):
            print(mapa[cislo_radku][cislo_sloupce], end=' ')
        print();

# print(nakresli_mapu([(2,3)]))

############ ukol 6 ##################
# def pohyb(souradnice, pohyb):
#     poloha = souradnice[-1]
#     if pohyb=='v':
#         nova_poloha = (poloha[0]+1, poloha[1]+0)
#     elif pohyb == 's':
#         nova_poloha = (poloha[0] + 0, poloha[1] - 1)
#     elif pohyb == 'j':
#         nova_poloha = (poloha[0] + 0, poloha[1] + 1)
#     elif pohyb == 'z':
#         nova_poloha = (poloha[0] -1, poloha[1] + 0)
#     souradnice.append(nova_poloha)

# souradnice = [(0, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]

############ ukol 7 ##################
# seznam=[(0, 0), (1, 0), (2, 0)]
# nakresli_mapu(seznam)
# while True:
#     while True:
#         kam = str(input('Kam půjdeš? (zadej světovou stranu) '))
#         if not (kam=='s' or kam=='j' or kam=='v' or kam=='z'):
#             print('Neplatná volba. Zadej světovou stranu malými písmeny: s, j, z nebo v.')
#         else: break
#     pohyb(seznam, kam)
#     nakresli_mapu(seznam)

############ ukol 8 ##################
# def pohyb(souradnice, pohyb):
#     poloha = souradnice[-1]
#     if pohyb=='v':
#         nova_poloha = (poloha[0] + 1, poloha[1] + 0)
#     elif pohyb == 's':
#         nova_poloha = (poloha[0] + 0, poloha[1] - 1)
#     elif pohyb == 'j':
#         nova_poloha = (poloha[0] + 0, poloha[1] + 1)
#     elif pohyb == 'z':
#         nova_poloha = (poloha[0] -1, poloha[1] + 0)
#     souradnice.append(nova_poloha)
#     del souradnice[0]
#
# souradnice=[(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(1, 0), (2, 0), (3, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(2, 0), (3, 0), (4, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(3, 0), (4, 0), (4, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(4, 0), (4, 1), (4, 0)]
