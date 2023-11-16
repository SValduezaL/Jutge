def missatge(qui: str, verb: str, cops: int, fem: bool) -> None:
    """Escriu un missatge del tipus "Na Marta ha saltat 3 cops", tenint em compte:
            - El nom de la persona (Marta en aquest cas).
            - El verb (saltat en aquest cas).
            - El nombre de cops que ha realitzat el verb (3 en aquest cas).
            - El seu gènere (femení en aquest cas).
    Args:
        qui (str): Nom de la persona (Marta en aquest cas).
        verb (str): Verb (saltat en aquest cas).
        cops (int): Nombre de cops que ha realitzat el verb (3 en aquest cas).
        fem (bool): True si la persona es femení (femení en aquest cas).
    Returns:
        Res, només imprimeix la frase en pantalla.
    """
    
    if fem:
        qui = 'Na ' + qui
    else:
        qui = 'En ' + qui
    
    if cops == 0:
        return print (f'{qui} no ha {verb}.')
    elif cops == 1:
        str_cops = str(cops) + " cop"
    else:
        str_cops = str(cops) + " cops"
    
    return print (f'{qui} ha {verb} {str_cops}.')


def main() -> None:
    missatge('Marta', 'saltat', 3, True)
    missatge('Pere', 'jugat', 1, False)
    missatge('Sandra', 'mirat', 0, True)


if __name__ == "__main__":
    main()
