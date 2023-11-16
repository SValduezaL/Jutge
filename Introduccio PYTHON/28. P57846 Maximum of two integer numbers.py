def max2(a: int, b: int) -> int:
    '''Returns the larger of two numbers.'''
    
    return a if a > b else b

def main() -> None:
    print (max2(123, 666))
    print (max2(3, 4))
    print (max2(2, 2))
    print (max2(-1, 0))

if __name__ == '__main__':
    main ()