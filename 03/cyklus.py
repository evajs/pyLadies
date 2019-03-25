# for cislo in range(5):
#     print(cislo)
#
# for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei', 'SYN':
#     print(pozdrav + '!')

from turtle import forward, left, right, exitonclick, penup, pendown

# for cisloStrany in range(4):
#     forward(50)
#     left(90)

# for i in range(10):
#     forward(i)
#     penup()
#     forward(5)
#     pendown()

# for cisloCtverce in range(3):
#     for cisloStrany in range(4):
#         forward(50)
#         left(90)
#     left(20)

# for cisloSchodu in range(6):
#     forward(50)
#     left(90)
#     forward(50)
#     right(90)

for cisloHexu in range(6):
    for cisloStrany in range(6):
        forward(50)
        left(60)
    forward(50)
    right(60)

exitonclick()