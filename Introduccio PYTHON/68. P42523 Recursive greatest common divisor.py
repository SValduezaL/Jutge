def gcd(a: int, b: int) -> int:
    ''' Returns the greatest common divisor of a and b.
            Args:
                a (int): The first natural number.
                b (int): The second natural number.
            Preconditions:
                At least one of a or b is non-zero.
    '''
    if b == 0:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


def main() -> None:
    print(gcd(66, 12))
    print(gcd(100, 21))
    print(gcd(0, 10))
    print(gcd(10, 0))


if __name__ == "__main__":
    main()
