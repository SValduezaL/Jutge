
def factorial(n: int) -> int:
    while n > 1:
        fact = n * factorial(n-1)
        return fact
    return 1


def main() -> None:
    print (factorial(23))


if __name__ == "__main__":
    main()
