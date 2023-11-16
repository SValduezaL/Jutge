import turtle
from yogi import read

def dibuixa_esfera_rellotge() -> None:
    
    ''' Dibuixa l'esfera d'un rellotge de radi 200.
        La tortuga acabará al centre del rellotje, amb la punta aixecada, y mirant cap a les 12.
        Args:
            None.
        Precondicions:
            None.
    '''
    
    # Es dibuixa l'esfera del rellotje de radi 200 amb el centre a 0,0.
    
    turtle.penup()
    turtle.forward(200)
    turtle.left(90)   # S'encara la tortuga mirant cap a les 12.
    turtle.pendown()
    turtle.circle(200)
    turtle.penup()
    turtle.goto(0, 0)   # Es retorna la tortuga al centre del rellotje, amb la punta aixecada.
    
    # Es dibuixen els marcadors de les hores.
    for _i in range(12):
        turtle.forward(150)
        turtle.pendown()
        turtle.forward(50)
        turtle.penup()
        turtle.backward(200)
        turtle.left(30)


def dibuixa_busques(hores: int, minuts: int) -> None:
    ''' Dibuixa les dues busques d'un relloge:
        - La de les hores, amb una llargada de 90.
        - La dels minuts, amb una llargada de 140.
        La tortuga acabará al centre del rellotje, amb la punta aixecada, y mirant cap a les 12.
        Args:
            hores (str): Posició de la busca de les hores.
            minuts (int): Posició de la busca dels minuts.
        Prec:
            1. 0 <= hores < 12
            2. 0 <= minuts < 60
            3. La tortuga ha de ser al centre del rellotje, amb la punta aixecada, y mirant cap a les 12.
    '''
    
    # Es dibuixa la busca de les hores.
    nova_hora = hores + minuts/60
    turtle.right(360*nova_hora/12)
    turtle.pendown()
    turtle.forward(90)
    
    # Es dibuixa la punta de la busca.
    turtle.left(150)
    for _i in range(3):
        turtle.forward(25)
        turtle.left(120)
    turtle.penup()
    turtle.right(150)
    
    # Es retorna la tortuga al centre del rellotje, amb la punta aixecada, y mirant un altre cop a les 12.
    turtle.goto(0, 0)
    turtle.left(360*nova_hora/12)
    
    
    # Es dibuixa la busca dels minuts.
    turtle.right(360*minuts/60)
    turtle.pendown()
    turtle.forward(140)
    
    # Es dibuixa la punta de la busca.
    turtle.left(150)
    for _i in range(3):
        turtle.forward(25)
        turtle.left(120)
    turtle.penup()
    turtle.right(150)
    
    # Es retorna la tortuga al centre del rellotje, amb la punta aixecada, y mirant un altre cop a les 12.
    turtle.goto(0, 0)
    turtle.left(360*minuts/60)


def dibuixa_rellotge(hores: int, minuts: int) -> None:
    ''' Dibuixa un rellotge esferic de radi 200
        amb les dues busques de les hores i els minuts
        segons l'hora donada.
        Args:
        hores (int): Posició de la busca de les hores.
        minuts (int): Posició de la busca dels minuts.
    '''
    
    dibuixa_esfera_rellotge()
    dibuixa_busques(hores, minuts)
    turtle.done()

def main() -> None:
    hores = read(int)
    minuts = read(int)
    
    dibuixa_rellotge(hores, minuts)


if __name__ == "__main__":
    main()
