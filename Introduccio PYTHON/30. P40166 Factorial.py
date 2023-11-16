def factorial(n: int) -> int:
    """Returns the n!."""
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    
    return fact


def main() -> None:
    print(factorial(5))
    print(factorial(6))
    print(factorial(23))


if __name__ == "__main__":
    main()
