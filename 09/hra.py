# hra.py
import piskvorky

# def piskvorky1d():
#     pole='--------------------'
#     stav_hry = '-'
#     hraje = 1
#     while stav_hry == '-':
#         if hraje==1:
#             pole = piskvorky.tah_hrace(pole)
#             print(pole)
#             hraje =2
#         else:
#             pole = ai.tah_pocitace(pole)
#             print(pole)
#             hraje =1
#         stav_hry = piskvorky.vyhodnot(pole)
#     if stav_hry =='x':
#         print('Vyhrál jsi. Gratulujeme.')
#     elif stav_hry =='o':
#         print('Vyhrál počítač.')
#     elif stav_hry == '!':
#         print('Remíza.')

def piskvorky1d():
    pole='--------------------'
    stav_hry = '-'
    hraje = 1
    while stav_hry == '-':
        if hraje==1:
            novy_vstup = True
            while novy_vstup:
                vstup = int(input('Zadej číslo pole, kam chceš hrát (0-19): '))
                hlaska, novy_vstup = piskvorky.over_vstup(pole,vstup)
                if novy_vstup:
                    print(hlaska)
            pole = piskvorky.util.tah(pole,vstup,'x')
            print(pole)
            hraje =2
        else:
            pole = piskvorky.ai.tah_pocitace(pole)
            print(pole)
            hraje =1
        stav_hry = piskvorky.vyhodnot(pole)
    print(piskvorky.jak_to_dopadlo(stav_hry))

piskvorky1d()