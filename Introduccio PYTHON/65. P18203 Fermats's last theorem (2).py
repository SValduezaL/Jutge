from yogi import read, scan


def main() -> None:
    a = scan(int)
    solution = False
    
    while a != None:
        _b, c, _d = read(int), read(int), read(int)
        if a == 0:
            print(f'0^3 + {c}^3 = {c}^3')
            solution = True
            break
        elif c == 0:
            print(f'{a}^3 + 0^3 = {a}^3')
            solution = True
            break
        else:
            a = scan(int)
    
    if not solution:
        print('No solution!')


if __name__ == "__main__":
    main()
