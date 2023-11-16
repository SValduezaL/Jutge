import turtle
from yogi import read


def quadrat(d: float, pos: list[float]) -> None:
    """
    Dibuixa un quadrat de mida d.
        Arguments:
            d(int): mida del quadrat.
            p(tuple): origen del quadrat.
        Retorna:
            Quadrat de mida d, dibuixat amb el mòdul Turtle.
    """
    turtle.penup()
    turtle.goto(pos[0], pos[1])
    turtle.pendown()
    
    for _i in range(4):
        turtle.forward(d)
        turtle.left(90)
    
    turtle.penup()


def amenaça_fractal(n: int, d: float, p: list[float] = [0, 0]) -> None:
    """
    Dibuixa l'amenaça fractal de nivell n.
        Arguments:
            n(int): nivell de l'amenaça fractal.
            d(int): mida del quadrat més gran del fractal.
        Retorna:
            L'amenaça fractal de nivell n, dibuixat amb el mòdul Turtle.
    """
    if n == 1:
        pos = [p[0] + (-d/2), p[1] + (-d/2)]
        quadrat(d, pos)
    else:
        pos = [p[0] + (-d/2), p[1] + (-d/2)]
        quadrat(d, pos)
        pos = [p[0] + (3*d/4), p[1] + (3*d/4)]
        amenaça_fractal(n-1, d/2, pos)
        pos = [p[0] + (-3*d/4), p[1] + (3*d/4)]
        amenaça_fractal(n-1, d/2, pos)
        pos = [p[0] + (-3*d/4), p[1]+ (-3*d/4)]
        amenaça_fractal(n-1, d/2, pos)


def main() -> None:
    n = read(int)
    d = read(float)
    amenaça_fractal(n, d)
    turtle.done()


if __name__ == "__main__":
    main()