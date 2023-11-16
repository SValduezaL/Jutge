from typing import Optional

def es_primer(n: int) -> bool:
    """
    Ens diu si el nombre n es primer (True) o no (False).
    Prec: n >= 0.
    """
    if n == 0 or n == 1:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def semiprimalitat(n: int) -> Optional[tuple[int,int]]:
    """
    Retorna els 2 nombres primers d'un nombre semiprimer, o None si no es un nombre semiprimer.
    Prec: n >= 2.
    """

    d = 2
    while d * d <= n:
        if n % d == 0:
            if (es_primer(d)) and (d == n):
                return None
            if es_primer(n//d):
                return d, n//d
            else:
                return None
        d += 1
    return None


def main() -> None:
    print(semiprimalitat(33))
    print(semiprimalitat(17))
    print(semiprimalitat(4))
    print(semiprimalitat(6))
    print(semiprimalitat(30))
    print(semiprimalitat(107711))
    print(semiprimalitat(1000003))


if __name__ == "__main__":
    main()
