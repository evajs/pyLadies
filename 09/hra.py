import piskvorky
import ai

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