import turtle
from yogi import read

n = read(int)
m = read(int)

for i in range(4):
    turtle.forward(m*n)
    turtle.left(90)

turtle.penup()
for i in range(n-1):
    turtle.forward(m)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(m*n)
    turtle.penup()
    turtle.backward(m*n)
    turtle.right(90)

turtle.forward(m)
turtle.left(90)
for i in range(n-1):    
    turtle.forward(m)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(m*n)
    turtle.penup()
    turtle.backward(m*n)
    turtle.right(90)

turtle.done()