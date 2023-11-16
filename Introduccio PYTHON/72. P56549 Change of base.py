from yogi import scan


def binary(n: int) -> str:
    '''
    Returns the binary representation of a given natural number.
        Args:
            n (int): Natural number to be converted to binary.
        Returns:
            (str): binary representation of the given natural number.
    '''
    if n < 2:
        return str(n)
    
    if n//2 < 2:
        return str(n//2) + str(n%2)
    else:
        return binary(n//2) + str(n%2)


def octal(n: int) -> str:
    ''' 
    Returns the octal representation of a given natural number.
        Args:
            n (int): Natural number to be converted to octal.
        Returns:
            (str): octal representation of the given natural number.
    '''
    if n < 8:
        return str(n)
    
    if n//8 < 8:
        return str(n//8) + str(n%8)
    else:
        return octal(n//8) + str(n%8)


def get_digit_hexadecimal(n: int) -> str:
    '''
    Returns the hexadecimal representation of a given natural number.
        Args:
            n (int): Natural number to be converted to hexadecimal.
        Precondition:
            0 >= n < 16
        Returns:
            (str): hexadecimal representation of the given natural number.
    '''
    if 0 <= n < 10:
        hex_digit = str(n)
    elif n == 10:
        hex_digit = 'A'
    elif n == 11:
        hex_digit = 'B'
    elif n == 12:
        hex_digit = 'C'
    elif n == 13:
        hex_digit = 'D'
    elif n == 14:
        hex_digit = 'E'
    else:
        hex_digit = 'F'
    return hex_digit


def hexadecimal(n: int) -> str:
    '''
    Returns the hexadecimal representation of a given natural number.
        Args:
            n (int): Natural number to be converted to hexadecimal.
        Returns:
            (str): hexadecimal representation of the given natural number.
    '''
    if n < 16:
        return get_digit_hexadecimal(n)
    
    if n//16 < 16:
        return get_digit_hexadecimal(n//16) + get_digit_hexadecimal(n%16)
    else:
        return hexadecimal(n//16) + get_digit_hexadecimal(n%16)


def main() -> None:
    x = scan(int)
    
    while x != None:
        print('{} = {}, {}, {}'.format(x, binary(x), octal(x), hexadecimal(x)))
        x = scan(int)


if __name__ == "__main__":
    main()
