def gcd(a: int, b: int) -> int:
    """Returns the greatest common divisor of two natural numbers."""

    while b != 0:
        a, b = b , a % b
    
    return a


def main() -> None:
    print(gcd(66, 12))
    print(gcd(100, 21))
    print(gcd(0, 10))


if __name__ == "__main__":
    main()
