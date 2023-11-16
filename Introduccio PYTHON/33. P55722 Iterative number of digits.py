def number_of_digits(n: int) -> int:
    """Returns the number of digits of a number n."""

    number = str(n)

    return len(number)


def main() -> None:
    print(number_of_digits(7))
    print(number_of_digits(4321))
    print(number_of_digits(0))


if __name__ == "__main__":
    main()
