from typing import Optional

def es_primer(n: int) -> bool:
    """
    Ens diu si el nombre n es primer (True) o no (False).
    Prec: n >= 0.
    """
    if n == 0 or n == 1:
        return False
    
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def factor_mes_petit(n: int) -> Optional[int]:
    """
    Retorna el factor de n més petit, o None quan es un nombre primer.
    Prec: n >= 2.
    """
        
    d = 2
    while d*d <= n:
        if n % d == 0:
            if (es_primer(d)) and (d == n):
                return None
            return d
        d += 1
    return None


def main() -> None:
    print(factor_mes_petit(17))
    print(factor_mes_petit(12))
    print(factor_mes_petit(101))
    print(factor_mes_petit(102))
    print(factor_mes_petit(10000000019))
    print(factor_mes_petit(1639649857))
    print(factor_mes_petit(736854654091))


if __name__ == "__main__":
    main()
