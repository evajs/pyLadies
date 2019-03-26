################ ukol 1 ################
# seznam cisle od 0 do n-1

################ ukol 2 ################
# from turtle import forward, left, exitonclick, penup, pendown
#
# for n in range(5,9):
#     for cisloStrany in range(n):
#         delkaStrany= 200/n
#         uhel = 360/n
#         print(uhel)
#         forward(delkaStrany)
#         left(uhel)
#     penup()
#     forward(90)
#     pendown()
#
# exitonclick()

################ ukol 3 ################
from turtle import forward, left, exitonclick, penup, pendown

pocet = int(input('Zadej pocet stran n-uhelniku:'))
delkaStrany = 200/pocet
uhel = 360/pocet
print(delkaStrany, uhel)

for cisloStrany in range(pocet):
    forward(delkaStrany)
    left(uhel)

exitonclick()
