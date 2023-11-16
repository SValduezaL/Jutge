from yogi import scan


def is_strobogrammatic_and_odd_number(n: int) -> tuple[bool, bool]:
    
    num = str(n)
    
    for i in range(len(num)):
        if num[i] == '2' or num[i] == '3' or num[i] == '4' or num[i] == '5' or num[i] == '7':
            print('{} is not strobogrammatic'.format(n))
            return False, False
        elif (num[i] == '0' and num[-(i+1)] != '0') or\
            (num[i] == '1' and num[-(i+1)] != '1') or\
                (num[i] == '6' and num[-(i+1)] != '9') or\
                    (num[i] == '8' and num[-(i+1)] != '8') or\
                        (num[i] == '9' and num[-(i+1)] != '6'):
                            print('{} is not strobogrammatic'.format(n))
                            return False, False
    
    print('{} is strobogrammatic'.format(n))
    
    if n%2 != 0:
        return True, True
    else:
        return True, False


def main():
    n = scan(int)
    odds = 0
    while n != None:
        odd = is_strobogrammatic_and_odd_number(n)[1]
        if odd:
            odds += 1
        n = scan(int)
    
    print()
    print('odd strobogrammatic: {}'.format(odds))


if __name__ == "__main__":
    main()