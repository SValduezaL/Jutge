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


def main() -> None:
    print(es_primer(17))
    print(es_primer(12))
    print(es_primer(101))
    print(es_primer(102))
    print(es_primer(10000000019))
    print(es_primer(1639649857))
    print(es_primer(736854654091))


if __name__ == "__main__":
    main()
