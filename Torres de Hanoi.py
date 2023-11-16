from yogi import read

def torre_Hanoi(n: int, ori: list[int], aux: list[int], dst: list[int], movimientos: int = 0) -> int:
    ''' Realiza todos los movimientos necesarios para resolver las Torres de Hanoi de nivel n,
        donde la posición inicial de Origen son n discos apilados de mayor a menor en una aguja Origen,
        y se tienen que llevar todos esos discos a otra aguja Destino, apilados en la misma posición,
        utilizando para ello una aguja Auxiliar intermedia.
        Sólo se puede mover un disco por movimiento, y nunca se puede apilar un disco encima de otro menor.
            Args:
                n(int): el nivel de la torre de Hanoi.
                ori(list[int]): la lista de posiciones de los discos en la aguja Origen.
                aux(list[int]): la lista de posiciones de los discos en la aguja Auxiliar.
                dst(list[int]): la lista de posiciones de los discos en la aguja Destino.
                movimientos(int): el número de movimientos que se debe realizar para resolver el problema. Por defecto 0.
            Precondiciones:
                n < 25. Para n mayores es fácil que el programa pete por tiempo de ejecución.
    '''
    if n > 0:
        movimientos = torre_Hanoi(n-1, ori, dst, aux, movimientos)
        dst.insert(0, min(ori))
        ori.remove(min(ori))
        movimientos += 1
        movimientos = torre_Hanoi(n-1, aux, ori, dst, movimientos)
    
    return movimientos


def main():
    
    ori = list(range(1, read(int)+1))
    aux = []
    dst = []
    
    print (f'Lista origen inicial = {ori}')
    print (f'Lista auxiliar inicial = {aux}')
    print (f'Lista destino inicial = {dst}', '\n')
    
    movimientos = torre_Hanoi(len(ori), ori, aux, dst)
    
    print (f'Lista origen final = {ori}')
    print (f'Lista auxiliar final = {aux}')
    print (f'Lista destino final = {dst}', '\n')
    
    print (f"Se han hecho {movimientos:,} movimientos para conseguirlo.")

if __name__ == "__main__":
    main()
