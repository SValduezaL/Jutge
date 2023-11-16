import turtle
from yogi import read

figura = read(str)

if figura == 'cercle':
    radi = read(int)
    turtle.circle(radi)
    turtle.done()
elif figura == 'quadrat':
    costat = read(int)
    for i in range(4):
        turtle.forward(costat)
        turtle.left(90)
    turtle.done()
elif figura == 'rectangle':
    amplada = read(int)
    alçada = read(int)
    for i in range(2):
        turtle.forward(amplada)
        turtle.left(90)
        turtle.forward(alçada)
        turtle.left(90)
    turtle.done()