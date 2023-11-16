def escriure_factors_primers(n: int) -> None:
    """ Imprimeix per pantalla en una línea els factors primers d'un nombre natural, ordenats de petit a gran.
    Args:
        n (int): Nombre enter >= 1 
    """
    
    d = 2
    ini = 0
    while d*d <= n:
        if n%d == 0:
            if ini == 0:
                print (d, sep='', end='')
            else:
                print (',', d, sep='', end='')
            ini += 1
            while n%d == 0:
                n = n//d
        d += 1
    
    if n != 1 and ini == 0:
        print (n)
    elif n != 1 and ini != 0:
        print(',', n, sep='')
    else:
        print ()


def main() -> None:
    escriure_factors_primers(392)
    escriure_factors_primers(17)
    escriure_factors_primers(1)
    escriure_factors_primers(4312)


if __name__ == "__main__":
    main()
