from yogi import scan


def sequence_Collatz(n: int) -> tuple[list[int], int]:
    ''' Returns the sequence of Collatz numbers up to 1 and including n.
            Args:
                n (int): The number to start the sequence at.
            Returns:
                sequence_Collatz (list[int]): The sequence of Collatz numbers.
                count (int): The number of steps in the sequence.
            Precondition:
                n >= 0
    '''
    sequence_Collatz = [n]
    count = 0
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        sequence_Collatz.append(n)
        count += 1
    
    return sequence_Collatz, count


def main() -> None:
    
    n = scan(int)
    
    while n!= None:
        print (sequence_Collatz(n)[1])
        n = scan(int)

if __name__ == "__main__":
    main()