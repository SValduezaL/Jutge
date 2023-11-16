from yogi import tokens

def X_rhombus(n: int) -> None:
    ''' Prints on screen a rhombus with 'X's,
        starting in a row with n 'X's,
        increasing 2 'X's in the following rows,
        writing n rows of [n + 2 * (n-1)] 'X's in the middle of the rhombus,
        and decreasing de 'X's in the following rows
        until the rhombus is finished in a row with n 'X's again.
        Args:
            n (int): The number of 'X's to start the rhombus. It determines the size of the rhombus.
        Preconditions:
            n > 0
    '''
    for i, j in zip(range(n-1, 0, -1), range(n-1)):
        print (' ' * (i), sep='', end='')
        print ('X' * n, sep='', end='')
        print ('X' * (j * 2), sep='', end='')
        print ()
    
    for _i in range(n):
        print ('X' * n, sep='', end='')
        print ('X' * 2 * (n-1), sep='', end='')
        print ()
    
    for i, j in zip(range(1, n), range(n-2, -1, -1)):
        print (' ' * (i), sep='', end='')
        print ('X' * n, sep='', end='')
        print ('X' * 2 * j, sep='', end='')
        print ()


def main():
    for number in tokens(int):
        X_rhombus(number)
        print ()


if __name__ == "__main__":
    main()