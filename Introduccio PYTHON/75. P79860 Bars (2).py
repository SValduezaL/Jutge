from yogi import scan


def print_bars(n: int) -> None:
    """
    Prints a pattern of asterisks with (2^n - 1) lines.
        Args:
            n (int): The size of the pattern.
        Precondition:
            n > 0
    """
    if n != 0:
        print("*" * n)
        print_bars(n - 1)
        print_bars(n - 1)


def main() -> None:
    n = scan(int)
    while n != None:
        print_bars(n)
        n = scan(int)


if __name__ == "__main__":
    main()
