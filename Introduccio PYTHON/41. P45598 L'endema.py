
def any_de_traspas(a: int) -> bool:
    """ Comprova si un any determinat es de traspàs.

    Args:
        a (int): Any entre 1800 i 9999, ambdós inclosos.

    Returns:
        bool: True si és any de traspàs, False si no ho és.
    """
    if (a%4 == 0 and a%100 != 0) or (a%100 == 0 and (a/100)%4 == 0):
        return True
    return False


def dia_seguent(d: int, m: str, a: int) -> tuple[int, str, int]:
    """
    Donada una data vàlida del calendari, retorna el día següent.
    Tot amb el format següent: dia amb un nombre natural, mes amb text en minúscules y l'any amb un altre nombre natural.
    Prec: Data vàlida del calendari.
    """
    mesos_any = ('gener', 'febrer', 'març', 'abril', 'maig', 'juny', 'juliol', 'agost', 'setembre', 'octubre', 'novembre', 'desembre')
    mesos_amb_30_dies = ('abril', 'juny', 'setembre', 'novembre')
    mesos_amb_31_dies = ('gener', 'març', 'maig', 'juliol', 'agost', 'octubre', 'desembre')
    
    
    if m in mesos_amb_30_dies:
        if d == 30:
            d = 1
            m = mesos_any[mesos_any.index(m) + 1]
            return (d, m, a)
        d += 1
        return (d, m, a)
    elif m in mesos_amb_31_dies:
        if d == 31:
            d = 1
            if m == 'desembre':
                m = 'gener'
                a += 1
            else:
                m = mesos_any[mesos_any.index(m) + 1]
            return (d, m, a)
        d += 1
        return (d, m, a)
    else:
        if any_de_traspas(a):
            if d == 29:
                d = 1
                m = 'març'
                return (d, m, a)
            d += 1
            return (d, m, a)
        else:
            if d == 28:
                d = 1
                m = 'març'
                return (d, m, a)
            d += 1
            return (d, m, a)


def main() -> None:
    print(dia_seguent(14, 'abril', 2015))
    print(dia_seguent(17, 'novembre', 2006))
    print(dia_seguent(31, 'desembre', 2022))
    print(dia_seguent(27, 'febrer', 2020))
    print(dia_seguent(28, 'febrer', 2020))
    print(dia_seguent(28, 'febrer', 2021))
    print(dia_seguent(29, 'febrer', 2020))
    print(dia_seguent(28, 'febrer', 1900))


if __name__ == "__main__":
    main()
