import turtle
from yogi import read

def cercle_amb_diam(d:float, p: list[float] = [0, 0]) -> None:
    """
    Dibuixa un cercle de diàmetre d.
        Arguments:
            d(int): diàmetre del cercle.
        Retorna:
            Cercle de diàmetre d, dibuixat amb el mòdul Turtle.
    """
    turtle.penup()
    turtle.goto(p[0], p[1])
    turtle.pendown()
    turtle.circle(d/2)
    turtle.penup()


def cercles_Koch(n: int, d: float, p: list[float] = [0, 0]) -> None:
    """
    Dibuixa el fractal del Cercles de Koch de n nivell.
        Arguments:
            n(int): nivell del fractal del Cercles de Koch.
            d(int): diàmetre del cercle més gran del fractal.
        Retorna:
            Fractal del Cercles de Koch de nivell n, dibuixat amb el mòdul Turtle.
    """
    if n == 1:
        pos = [p[0], p[1] - (d/2)]
        cercle_amb_diam(d, pos)
    else:
        pos = [p[0], p[1] - (d/2)]
        cercle_amb_diam(d, pos)
        
        pos = [p[0] + (3*d/4), p[1]]
        cercles_Koch(n-1, d/2, pos)
        
        pos = [p[0], p[1] + (3*d/4)]
        cercles_Koch(n-1, d/2, pos)
        
        pos = [p[0] - (3*d/4), p[1]]
        cercles_Koch(n-1, d/2, pos)
        
        pos = [p[0], p[1] - (3*d/4)]
        cercles_Koch(n-1, d/2, pos)


def main() -> None:
    n = read(int)
    d = read(float)
    
    cercles_Koch(n, d)
    
    turtle.done()

if __name__ == "__main__":
    main()
