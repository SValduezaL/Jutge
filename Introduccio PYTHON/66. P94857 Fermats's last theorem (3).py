from yogi import read, scan
# from time import time


def count_solutions_Fermat_last_theorem(a: int, b: int, c: int, d: int) -> int:
    ''' Returns the number of solutions of the Fermat last theorem that accomplish:
            x^2 + y^2 = z^2, for a <=x <= b and c <= y <= d
            being x, y and z natural numbers.
        Args:
            a (int): lower bound of x
            b (int): upper bound of x
            c (int): lower bound of y
            d (int): upper bound of y
    '''
    count = 0
    if a == 0 and c == 0:
        count += ((d - c) + 1) + (b - a)
        a += 1
        c += 1
    elif a == 0:
        count += ((d - c) + 1)
        a += 1
    elif c == 0:
        count += ((b - a) + 1)
        c += 1
    
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            z = ((x**2) + (y**2))**0.5
            if z % 1 == 0:
                count += 1
    
    return count


def main() -> None:
    # start_time = time()
    # print(count_solutions_Fermat_last_theorem(3, 3, 0, 1000000))
    # end_time = time()
    # print(f'{((end_time - start_time) * 1000):.2f} milliseconds')
    
    a = scan(int)
    while a != None:
        b, c, d = read(int), read(int), read(int)
        print(count_solutions_Fermat_last_theorem(a, b, c, d))
        a = scan(int)


if __name__ == "__main__":
    main()
