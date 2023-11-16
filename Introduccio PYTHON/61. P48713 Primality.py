from yogi import read


def primality(n: int) -> bool:
    ''' Tells if a number is prime or not.
            Args:
                n (int): number to be checked.
            Precondition:
                n must be a natural number
            Returns:
                bool: True if n is prime, False otherwise.
    '''
    if n <= 1:
        return False
    elif n==2 or n==3:
        return True
    else:
        d = 2
        while d*d <= n:
            if n % d == 0:
                return False
            d += 1
        return True


def main() -> None:
    n = read(int)
    
    for _i in range(n):
        x = read(int)
        print('{} is prime'.format(x)) if primality(x) else print('{} is not prime'.format(x))


if __name__ == "__main__":
    main()
