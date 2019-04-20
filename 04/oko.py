# from random import randrange
#
# bodu = 0
# while bodu <= 21:
#     print('Máš', bodu, 'bodů.')
#     if input('Chceš kartu? ')== 'ano':
#         bodu = bodu + 2 + randrange(9)
#     else:
#         break
#
# if bodu < 21:
#     print('Získal(a) jsi s', bodu, 'bodů. Gratulujeme.')
# elif bodu == 21:
#     print('Máš oko! Gratulujeme!')
# else:
#     print('Prohrál(a) jsi. Získal(a) jsi s', bodu, 'bodů.')

from random import randrange

soucet = 0
while soucet < 21:
    print('Máš', soucet, 'bodů')
    odpoved = input('Otočit kartu? ')
    if odpoved == 'ano':
        karta = randrange(2, 11)
        print('Otočil/a jsi', karta)
        soucet = soucet + karta
    elif odpoved == 'ne':
        break
    else:
        print('Nerozumím! Odpovídej "ano", nebo "ne"')

if soucet == 21:
    print('Gratuluji! Vyhrál/a jsi!')
elif soucet > 21:
    print('Smůla!', soucet, 'bodů je moc!')
else:
    print('Chybělo jen', 21 - soucet, 'bodů!')
