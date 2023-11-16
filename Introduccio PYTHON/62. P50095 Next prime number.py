from yogi import scan


def primality(n: int) -> bool:
    """ Tells if a number is prime or not.
            Args:
                n (int): number to be checked.
            Precondition:
                n must be a natural number
            Returns:
                bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True


def next_prime_number(x: int) -> int:
    """ Returns the next prime number greater than x.
            Args:
                x (int): number to be checked.
            Prec:
                x must be a prime number
            Returns:
                int: the next prime number greater than x.
    """
    y = x + 1
    while not primality(y):
        y += 1
    return y


def main() -> None:
    x = scan(int)
    
    while x!= None:
        if primality(x):
            print(next_prime_number(x))
        x = scan(int)


if __name__ == "__main__":
    main()
