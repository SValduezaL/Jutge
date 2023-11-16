from yogi import read


def prefixed_expression(symbol: str) -> int:
    """
    Returns the value of an expression prefixed with '+', '-', '*'.
        Args:
            symbol(str): The symbol to be evaluated at the beginning of the expression.
        Returns:
            The value of the concatenated expression.
    """
    if symbol == '+':
        return prefixed_expression(read(str)) + prefixed_expression(read(str))
    elif symbol == '-':
        return prefixed_expression(read(str)) - prefixed_expression(read(str))
    elif symbol == '*':
        return prefixed_expression(read(str)) * prefixed_expression(read(str))
    else:
        return int(symbol)


def main():
    symbol = read(str)
    print (prefixed_expression(symbol))

if __name__ == "__main__":
    main()
