from yogi import read


def main() -> None:
    n = read(int)
    x = read(int)
    
    for _i in range(1, n):
        x = read(int)
    
    print('At the position {} there is a(n) {}.'.format(n, x))


if __name__ == "__main__":
    main()
