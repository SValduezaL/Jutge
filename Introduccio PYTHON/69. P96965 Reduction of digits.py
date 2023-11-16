def reduction_of_digits(n: int) -> int:
    """ Keeps calculating the sum of the digits in a given number until
        the result of this calculation is a number of only one digit,
        then returns this number.
            Args:
                n (int): Number to be reduced.
    """
    n_str = str(n)
    new_n = 0
    for i in range(len(n_str)):
        new_n += int(n_str[i])
    if new_n < 10:
        return new_n
    else:
        return reduction_of_digits(new_n)


def main() -> None:
    print(reduction_of_digits(33))
    print(reduction_of_digits(5699))
    print(reduction_of_digits(0))


if __name__ == "__main__":
    main()
