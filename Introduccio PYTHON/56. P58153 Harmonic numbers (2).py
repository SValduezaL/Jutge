from yogi import read, scan


def difference_harmonic_numbers(n: int, m: int) -> float:
    """ Returns the difference between two harmonic numbers of n an m.
            Args:
                n (int): The number n to calculate the harmonic number for.
                m (int): The number m to calculate the harmonic number for.
            Returns:
                diff_Hns (float): The difference between Hn and Hm.
            Precondition:
                n and m consist of two natural numbers.
                n >= m
    """
    diff_Hns = 0
    
    for i in range(m+1, n+1):
        diff_Hns += 1 / i
    
    return diff_Hns


def main() -> None:
    
    n = scan(int)
    
    while n != None:
        m = read(int)
        print ('{:.10f}'.format(difference_harmonic_numbers(n, m)))
        n = scan(int)


if __name__ == "__main__":
    main()
