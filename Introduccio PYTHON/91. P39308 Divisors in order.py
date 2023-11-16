from yogi import scan


def divisors_in_order(n: int) -> None:
    
    print('divisors of {}:'.format(n), end='')
    d = 1
    list_d = []
    while d * d <= n:
        if n % d == 0:
            print(' {}'.format(d), end='')
            if d * d != n:
                list_d.append(n//d)   # type: ignore
        d += 1
    
    for item in reversed(list_d):   # type: ignore
        print(' {}'.format(item), end='')   # type: ignore
    
    return print()


def main():
    n = scan(int)
    
    while n != None:
        divisors_in_order(n)
        n = scan(int)


if __name__ == "__main__":
    main()
