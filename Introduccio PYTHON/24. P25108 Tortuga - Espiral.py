import turtle
from yogi import read

n = read(int)
m = read(int)

for i in range(1, n+1):
    turtle.forward(m*i)
    turtle.left(90)
    turtle.forward(m*i)
    turtle.left(90)
turtle.done()