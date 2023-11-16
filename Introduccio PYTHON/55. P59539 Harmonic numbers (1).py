from yogi import scan


def harmonic_number(n: int) -> float:
    ''' Returns the harmonic number of n.
            Args:
                n (int): The number to calculate the harmonic number for.
            Returns:
                Hn (float): The harmonic number of n.
            Precondition:
                n consists of a natural number.
    '''
    Hn = 0
    for i in range(1, n+1):
        Hn += 1/i
    
    return Hn


def main() -> None:
    n = scan(int)
    
    while n != None:
        print('{:.4f}'.format(harmonic_number(n)))
        n = scan(int)

if __name__ == "__main__":
    main()
