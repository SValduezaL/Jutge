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


def mixing_in_base_2(a: int, b: int) -> str:
    a_in_base2 = binary(a)
    b_in_base2 = binary(b)
    
    solution = str()
    for i in range(len(a_in_base2)):
        solution += a_in_base2[i] + b_in_base2[i]
    
    return solution


def main():
    a, b = scan(int), scan(int)

    while a != None and b != None:
        print(mixing_in_base_2(a, b))
        a, b = scan(int), scan(int)


if __name__ == "__main__":
    main()
