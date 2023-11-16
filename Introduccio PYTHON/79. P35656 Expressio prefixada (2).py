from yogi import read


def prefixed_expression(symbol: str) -> int:
    """
    Retorna el valor d'una expressió prefixada amb 3 possibles operands:
        '-': Canvi de signe
        '+': Suma de dos valors o expressions
        'm': El màxim de 3 valors o expressions.
        Args:
            symbol(str): L'operand que defineix el que es fa amb lo que segueix.
        Returns:
            El valor de tota l'expressió concatenada.
    """
    if symbol == "+":
        return prefixed_expression(read(str)) + prefixed_expression(read(str))
    elif symbol == "-":
        return prefixed_expression(read(str)) * (-1)
    elif symbol == "m":
        return max(prefixed_expression(read(str)), prefixed_expression(read(str)), prefixed_expression(read(str)))
    else:
        return int(symbol)


def main():
    symbol = read(str)
    print(prefixed_expression(symbol))

if __name__ == "__main__":
    main()
