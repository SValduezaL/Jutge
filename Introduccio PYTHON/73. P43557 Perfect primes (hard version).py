def is_prime(n: int) -> bool:
    """ It says if a given natural number is a Prime number.
            Args:
                n (int): Natural number to be checked.
            Returns:
                True if the number is a Prime number, False otherwise.
    """
    if n == 0 or n == 1:
        return False
    
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def one_reduction_of_digits(n: int) -> int:
    """ Returns the sum of the digits in a given natural number.
            Args:
                n (int): Number to be reduced.
            Returns:
                The reduced natural number.
    """
    new_n = int()
    for i in range(len(str(n))):
        new_n += int(str(n)[i])
    return new_n


def is_perfect_prime(n: int) -> bool:
    """ It says if a given number is a Perfect Prime,
        that mean the sum of its digits is another Perfect Prime,
        and so on until that sum of digits is a number of only one digit.
            Args:
                n (int): Natural number to be checked.
            Returns:
                True if the number is a Perfect Prime, False otherwise.
    """
    if n < 10:
        return True if is_prime(n) else False
    
    if not is_prime(n):
        return False
    else:
        return is_perfect_prime(one_reduction_of_digits(n))


def main() -> None:
    print(is_perfect_prime(977))
    print(is_perfect_prime(978))
    print(is_perfect_prime(0))
    print(is_perfect_prime(11))


if __name__ == "__main__":
    main()
