def gcd(a: int, b: int) -> int:
    """Returns the greatest common divisor of two natural numbers."""

    while b != 0:
        a, b = b, a % b

    return a


def gcd4(a: int, b: int, c: int, d: int) -> int:
    """Returns the greatest common divisor of four natural numbers."""
    
    return gcd(gcd(a, b), gcd(c, d))

def main() -> None:
    print(gcd4(66, 12, 1200, 36))
    print(gcd4(10, 6, 21, 35))


if __name__ == "__main__":
    main()
