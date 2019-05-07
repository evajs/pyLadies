# hra.py
import piskvorky
import ai
import util

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
                hlaska, novy_vstup = piskvorky.(vstup)
                if novy_vstup:
                    print(hlaska)
            pole = util.tah(pole,vstup,'x')
            print(pole)
            hraje =2
        else:
            pole = ai.tah_pocitace(pole)
            print(pole)
            hraje =1
        stav_hry = piskvorky.vyhodnot(pole)
    if stav_hry =='x':
        print('Vyhrál jsi. Gratulujeme.')
    elif stav_hry =='o':
        print('Vyhrál počítač.')
    elif stav_hry == '!':
        print('Remíza.')




piskvorky1d()