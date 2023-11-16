from yogi import scan

def trick_uncle_Ernie(n: int) -> int:
    """
    Return the number of the trick of the uncle Ernie the Magician.
        Args:
            n(int): The number of the guy says after all the calculations.
        Preconditions:
            0 < n < (2**31)-1
        Returns:
            The number the guy was thinking at the beginning of the trick.
    """
    number = str(n)
    trick = int(number[:len(number)-2]) - 1
    
    return trick

def main():
    n = scan(int)
    while n != None:
        print(trick_uncle_Ernie(n))
        n = scan(int)

if __name__ == '__main__':
    main()