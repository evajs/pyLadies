################ ukol 0 ################
# seznam cisle od 0 do n-1

################ ukol 1 ################
# from turtle import forward, left, exitonclick, penup, pendown
#
# for n in range(5,9):
#     for cisloStrany in range(n):
#         delkaStrany= 200.0/n
#         uhel = 360.0/n
#         forward(delkaStrany)
#         left(uhel)
#     penup()
#     forward(90)
#     pendown()
#
# exitonclick()

################ ukol 2 ################
# from turtle import forward, left, exitonclick, penup, pendown
#
# pocet = int(input('Zadej počet stran n-úhelníku:'))
# delkaStrany = 200.0/pocet
# uhel = 360.0/pocet
#
# for cisloStrany in range(pocet):
#     forward(delkaStrany)
#     left(uhel)
#
# exitonclick()

################ ukol 3 ################
# cislo1 = input('První číslo:')
# cislo2 = input('Druhé číslo:')
# operace =input('Operace:')
#
# if operace =='+':
#     print(cislo1+operace+cislo2, '=', float(cislo1)+float(cislo2))
# elif operace =='-':
#     print(cislo1 + operace + cislo2, '=', float(cislo1) - float(cislo2))
# elif operace =='*':
#     print(cislo1 + operace + cislo2, '=', float(cislo1) * float(cislo2))
# elif operace =='/':
#     print(cislo1 + operace + cislo2, '=', float(cislo1) / float(cislo2))
# else:
#     print('Neznámá operace')

################ ukol 4 ################
# range(m, n) vraci seznam hodnot od m do n-1

################ ukol 5 ################
# range(m, n, k) vraci seznam hodnot od m s krokem k do posledni hodnoty mensi nez n

################ ukol 6 ################
# from turtle import forward, left, exitonclick, penup, pendown
#
# pocet = 3
# delkaStrany = 200.0/pocet
# uhel = 360.0/pocet
#
# for cisloStrany in range(pocet):
#     forward(delkaStrany)
#     left(uhel)
#
# exitonclick()

################ ukol 7 ################
# from turtle import forward, left, right, exitonclick, penup, pendown
# from math import sqrt
#
# uhlopricka = 50 * sqrt(2)
#
# for cisloStrany in range(4):
#     forward(50)
#     left(90)
#
# left(45)
# forward(uhlopricka)
# left(90)
# forward(uhlopricka/2)
# left(90)
# forward(uhlopricka/2)
# left(90)
# forward(uhlopricka)
# left(45)
#
# exitonclick()


################ ukol 8 ################
# from turtle import forward, left, right, exitonclick, penup, pendown
# from math import sqrt
#
# uhlopricka = 50 * sqrt(2)
#
# for cisloDomu in range(10):
#     for cisloStrany in range(4):
#         forward(50)
#         left(90)
#     left(45)
#     forward(uhlopricka)
#     left(90)
#     forward(uhlopricka/2)
#     left(90)
#     forward(uhlopricka/2)
#     left(90)
#     forward(uhlopricka)
#     left(45)
#     penup()
#     forward(10)
#     pendown()
#
# exitonclick()

################ ukol 9 ################
# from turtle import forward, left, exitonclick, penup, pendown
#
# pocet = 200
# delkaStrany = 200.0/pocet
# uhel = 360.0/pocet
#
# for cisloStrany in range(pocet):
#     forward(delkaStrany)
#     left(uhel)
#
# exitonclick()

# ################ ukol 10 ################
# from turtle import forward, left, exitonclick, penup, pendown
#
# pocet = 95
# delkaStrany = 200.0/pocet
# uhel = 360.0/pocet
#
# for cisloStrany in range(pocet):
#     forward(delkaStrany)
#     left(uhel)
#
# exitonclick()

################ ukol 11 ################
# from turtle import forward, left, right, exitonclick, penup, pendown
#
# delkaStrany = 90
# left(90)
# for cisloStrany in range(19):
#     forward(delkaStrany)
#     right(90)
#     delkaStrany = delkaStrany - 5
#
# exitonclick()

################ ukol 12 ################
# from turtle import forward, left, right, exitonclick, penup, pendown
#
# delkaStrany = 118
# uhel=360.0/8
# right(uhel)
# for cisloStrany in range(58):
#     forward(delkaStrany)
#     right(uhel)
#     delkaStrany = delkaStrany - 2
#
# exitonclick()

################ ukol 13 ################
# TODO
# from turtle import forward, left, right, exitonclick, penup, pendown
#
# pocetStranUhelniku =100
# pocetStranSpiraly =int(16.5*pocetStranUhelniku)
# delkaStrany = 5
# uhel=360.0/pocetStranUhelniku
# left(45)
# for cisloStranySpiraly in range(pocetStranSpiraly):
#     forward(delkaStrany)
#     right(uhel)
#     delkaStrany = delkaStrany - delkaStrany/pocetStranSpiraly
#
# exitonclick()

################ ukol 17 ################
# vysledek = input('Zadej číslo:')
#
# for opakovani in range(4):
#     cislo=input('Zadej číslo:')
#     vysledek = min(vysledek, cislo)
#
# print('Nejmenší číslo bylo:', vysledek, end='.\n')