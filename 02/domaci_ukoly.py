################### ukol 1 #####################
#
# hrana=2852
# print('Povrch krychle o hraně', hrana, 'je', 6*hrana**2, 'centimetrů čtverečných.')
# print('Objem krychle o hraně', hrana, 'je', hrana**3, 'centimetrů krychlových.')

################### ukol 2 #####################
#
# hrana= float(input('Zadej hranu krychle v centimetrech'))
# print('Povrch krychle o hraně ', hrana, ' je ', 6*hrana**2, '.')
# print('Objem krychle o hraně', hrana, ' je ', hrana**3, '.')

################### ukol 3 #####################
# from random import randrange
# cislo = randrange(3)
# print(cislo)

# Vrací náhodně nulu, jedničku nebo dvojku.

################### ukol 4 #####################
# heslo = 'zmrzlina'
# zadano = input('Zadej heslo:')
# if zadano == heslo:
#     print('Pšššt. Všechny děti spí.')
# else:
#     print('Nesprávné heslo. Žádné tajemnství se nedozvíš.')

################### ukol 4 #####################
# verzi 3.7
# PyCharm > Preferences > Project:PyLadies > Project Interpreter

################### ukol 5 #####################
# Dáš uvozovky jen na jednu stranu řetězce? — SyntaxError
# Zkusíš odečíst číslo od řetězce? — TypeError
# Dělíš nulou? — ZeroDivisionError
# Použiješ proměnnou, která neexistuje? — NameError
# Stiskneš Ctrl+C, když se program ptá na vstup (pomocí input)? — InputError
# Odsadíš příkaz bez předchozího if:? — IndentationError
# Po if: odsadíš jeden příkaz o čtyři mezery a druhý jen o dvě? — IndentationError
# Neuzavřeš závorku? – SyntaxError
# Zkusíš použít vykřičník (!) jako operátor? — SyntaxError
# Napíšeš v příkazu print(1, 2, 3) čárku navíc? — SyntaxError

################### ukol 6 #####################
# NameError

################### ukol 7 #####################
# TypeError

################### ukol 8 #####################
# když operátor nelze použít pro daný typ (lomítko), vrací TypeError
# když operátor vůbec neexistuje, vrací SyntaxError

################### ukol 9 #####################
# x  OK
# tlacitko4 OK
# 34 - je číslo, má už nejaký význam
# 3e4 - nemůže začínat ani číslem
# krůta - OK
# $i - nemůže začínat $
# druha-odmocnina - "-" bere jako odcitani - neleze pouzita jako nazev
# readme.txt - bere jako volani metody txt v tride readme?
# kratsiStrana OK
# POCET_BODU OK
# _ (podtržítko) OK
# π (pí) OK
# True - má jiný význam
# _cache - OK
# __name__ - OK
# while  - nelze, má jiný význam

################### ukol 10 #####################
# from random import randrange
# cislo = randrange(3)
# if cislo == 0:
#     tah_pocitace = 'kámen'
# elif cislo ==2:
#     tah_pocitace = 'papír'
# elif cislo ==1:
#     tah_pocitace = 'nůžky'
#
# tah_cloveka = input('kámen, nůžky, nebo papír? ')
# print(tah_pocitace);
#
# if tah_cloveka == 'kámen':
#     if tah_pocitace == 'kámen':
#         print('Plichta.')
#     elif tah_pocitace == 'nůžky':
#         print('Vyhrála jsi!')
#     elif tah_pocitace == 'papír':
#         print('Počítač vyhrál.')
# elif tah_cloveka == 'nůžky':
#     if tah_pocitace == 'kámen':
#         print('Počítač vyhrál.')
#     elif tah_pocitace == 'nůžky':
#         print('Plichta.')
#     elif tah_pocitace == 'papír':
#         print('Vyhrála jsi!')
# elif tah_cloveka == 'papír':
#     if tah_pocitace == 'kámen':
#         print('Vyhrála jsi!')
#     elif tah_pocitace == 'nůžky':
#         print('Počítač vyhrál.')
#     elif tah_pocitace == 'papír':
#         print('Plichta.')
# else:
#     print('Nerozumím.')

################### ukol 11 #####################
# +, -, /, *, **, <, >, <=, >=, ==, //,

################### ukol 12 #####################
# a	        b
# 2	    >	1
# 1	    <	2
# 'abc'	==	'abc'
# 'aaa'	<	'abc'
# 'abc'	>	'Abc'
# 'abC'   <	'abc'
# 'abc'	<	'abcde'
# 'abc'	<	'ábč'
# 'abc'   !=   10

################### ukol 13 #####################
# promenna = 1 < 2 ? True
# promenna = 2 < 2 ? False
# promenna = 1 < 2 < 3 ? True
# promenna = 1 < 3 < 2 ? False
# promenna = 1 < 3 < 3 ? False
# promenna = 'abc' < 'ABC' < 'def' < 'zajíc' ? False

################### ukol 14 #####################
# cas = float(input('Kolik je hodin?'))
# if cas < 0:
#     print('Zadávej v dnešním datu.')
# elif cas < 7.5:
#     print('Klídek, ještě spi.')
# elif cas == 7.5:
#     print('Vstávat!!!')
# elif cas < 23:
#     print('To je ale krásný den.')
# elif cas == 23:
#     print('Spát!!!')
# elif cas <= 24:
#     print('Klídek, ještě spi.')
# elif cas > 24:
#     print('Zadávej v dnešním datu.')


################### ukol 16 #####################
# a	    b	    a and b	    a or b	    not a
# True	True	True        True        False
# False	True	False       True        True
# True	False	False		True        False
# False	False	False		False       True

################### ukol 17 #####################
# from random import randrange
# cislo = randrange(3)
# if cislo == 0:
#     tah_pocitace = 'kámen'
# elif cislo ==2:
#     tah_pocitace = 'papír'
# elif cislo ==1:
#     tah_pocitace = 'nůžky'
#
# tah_cloveka = input('kámen, nůžky, nebo papír? ')
# print(tah_pocitace);
#
# if tah_pocitace == tah_cloveka:
#     print('Plichta.')
# elif (tah_pocitace == 'kámen' and tah_cloveka == 'nůžky') or (tah_pocitace == 'nůžky' and tah_cloveka == 'papír') or (tah_pocitace == 'papír' and tah_cloveka == 'kámen'):
#     print('Počítač vyhrál.')
# elif (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky') or (tah_cloveka == 'nůžky' and tah_pocitace == 'papír') or (tah_cloveka == 'papír' and tah_pocitace == 'kámen'):
#     print('Vyhrála jsi.')

################### ukol 18 #####################
# print('Odpovídej "ano" nebo "ne".')
# stastna_retezec = input('Jsi šťastná? ')
# if stastna_retezec == 'ano':
#     stastna = True
# elif stastna_retezec == 'ne':
#     stastna = False
# else:
#     print('Nerozumím!')
#
# bohata_retezec = input('Jsi bohatá? ')
# if bohata_retezec == 'ano':
#     bohata = True
# elif bohata_retezec == 'ne':
#     bohata = False
# else:
#     print('Nerozumím!')
#
# if bohata:
#     if stastna:
#         # Je bohatá a zároveň štǎstná, ta se má.
#         print('Gratuluji!')
#     else:
#         # Je bohatá, ale není „bohatá a zároveň šťastná“,
#         # takže musí být jen bohatá.
#         print('Zkus se víc usmívat.')
# else:
#     if stastna:
#         # Tady musí být jen šťastná.
#         print('Zkus míň utrácet.')
#     else:
#         # A tady víme, že není ani šťastná, ani bohatá.
#         print('To je mi líto.')
