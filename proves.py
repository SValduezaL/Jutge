import turtle

def corba_Koch(m: float, n:int) -> None:
    ''' Dibuixa la corba de Koch per una determinada mida m i n nombre de nivells. '''
    
    if  n == 0:
        turtle.forward(m)
    else:
        corba_Koch(m/3, n-1)
        turtle.left(60)
        corba_Koch(m/3, n-1)
        turtle.right(120)
        corba_Koch(m/3, n-1)
        turtle.left(60)
        corba_Koch(m/3, n-1)

def main():
    corba_Koch(200, 2)

if __name__ == '__main__':
    main()