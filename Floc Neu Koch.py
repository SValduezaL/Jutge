import turtle, yogi

def corba_Koch(m: float, n: int) -> None:
    """Dibuixa la corba de Koch per una determinada mida m i n nombre de nivells."""

    if n == 0:
        turtle.forward(m)
    else:
        corba_Koch(m / 3, n - 1)
        turtle.left(60)
        corba_Koch(m / 3, n - 1)
        turtle.right(120)
        corba_Koch(m / 3, n - 1)
        turtle.left(60)
        corba_Koch(m / 3, n - 1)

def floc_neu_Koch(m: float, n: int) -> None:
    for _i in range(3):
        corba_Koch(m, n)
        turtle.right(120)

def main():
    turtle.speed(0) # accelerem la tortuga
    
    m = yogi.read(float)
    n = yogi.read(int)
    
    floc_neu_Koch(m, n)
    turtle.done()
    
if __name__ == "__main__":
    main()
