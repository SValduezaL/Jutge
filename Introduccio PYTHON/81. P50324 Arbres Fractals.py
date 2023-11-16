import turtle


def arbre_fractal(n: int, d: float, alfa: int) -> None:
    """Dibuixa un arbre fractal de nivell n, amb un tronc de mida d, la seva branca esquerra i la seva branca dreta,
    ambdues com a arbres de n-1 nivells i mida 3/4 de d, simètriques respecte del tronc amb un angle de 2 * alfa graus entre elles.
    Un arbre de nivell zero és buit.
    Args:
        n (int): el nivell de l'arbre fractal.
        d (float): la mida d del tronc de l'arbre.
        alfa (int): la meitat de l'angle que separa les dues branques superiors.
    Precondition:
        n >= 1
        0 <= alfa <= 90
    """

    if n == 1:
        turtle.forward(d)
    else:
        turtle.forward(d)
        pos, head = turtle.position(), turtle.heading()
        turtle.left(alfa)
        arbre_fractal(n - 1, (3 / 4) * d, alfa)
        turtle.penup()
        turtle.goto(pos)
        turtle.setheading(head)
        turtle.pendown()
        turtle.right(alfa)
        arbre_fractal(n - 1, (3 / 4) * d, alfa)


def main():
    turtle.speed(0)  # accelerem la tortuga
    turtle.setheading(90)
    arbre_fractal(5, 200, 90)
    turtle.done()


if __name__ == "__main__":
    main()
