# soubor = open('basnicka.txt', encoding='utf-8')
# obsah = soubor.read()
# soubor.close()
#
# print(obsah)

# with open('basnicka.txt', encoding='utf-8') as soubor:
#     obsah = soubor.read()
#
# print(obsah)

# print('Slyšela jsem tuto básničku:')
# print()
#
# with open('basnicka.txt', encoding='utf-8') as soubor:
#     for radek in soubor:
#         print('    ' + radek, end='')
#
# print()
# print()
# print('Jak se ti líbí?')
#
# print('Slyšela jsem tuto básničku:')
# print()

# with open('basnicka.txt', encoding='utf-8') as soubor:
#     for radek in soubor:
#         radek = radek.rstrip()
#         print('    ' + radek)
#
# print()
# print('Jak se ti líbí?')

with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
    print('Naše staré hodiny', file=soubor)
    print('Bijí', 2+2, 'hodiny', file=soubor)
