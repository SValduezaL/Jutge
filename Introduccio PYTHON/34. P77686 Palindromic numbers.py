def is_palindromic(n: int) -> bool:
    """
    Returns True if the natural number is a palindromic number, or False otherwise.
    Prec: n is a positive natural number.
    
    """
    number = str(n)
    if len(number) % 2 != 0:
        for i, j in zip(range(len(number)//2), range(len(number)-1, len(number)//2, -1)):
            if number[i] != number[j]:
                return False
    else:
        for i, j in zip(range(len(number)//2), range(len(number)-1, (len(number)//2)-1, -1)):
            if number[i] != number[j]:
                return False
    return True


def main() -> None:
    print(is_palindromic(12321))
    print(is_palindromic(0))
    print(is_palindromic(4004))
    print(is_palindromic(12))
    print(is_palindromic(100201))


if __name__ == "__main__":
    main()
