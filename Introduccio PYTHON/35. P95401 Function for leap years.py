def is_leap_year(year: int) -> bool:
    """
    Returns True if the year defined is a Leap year, False otherwise.
    Prec: The parameter year is between 1800 and 9999, both included.

    """
    if ((year % 4 == 0) and (year % 100 != 0 or (year//100) % 4 == 0)):
        return True
    else:
        return False


def main() -> None:
    print(is_leap_year(1967))
    print(is_leap_year(1968))
    print(is_leap_year(2100))
    print(is_leap_year(2400))


if __name__ == "__main__":
    main()
