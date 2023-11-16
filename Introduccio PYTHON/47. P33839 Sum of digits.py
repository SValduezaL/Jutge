from yogi import scan

def sum_of_digits(n: int) -> int:
    """ Returns the sum of the digits of the number n.
        Args:
            n (int): The number n.
    """
    sum = 0
    str_number = str(n)
    
    for i in range(len(str_number)):
        sum += int(str_number[i])
    
    return sum


def main() -> None:
    number = scan(int)
    while number != None:
        print ('The sum of the digits of {} is {}.'.format(number, sum_of_digits(number)))
        number = scan(int)

if __name__ == "__main__":
    main()
