from yogi import read


def main() -> None:
    Pica_Estats = 3143
    peak = False
    x, y, z = read(int), read(int), read(int)
    
    while z != 0:
        if x <= y >= z and y > Pica_Estats:
            peak = True
            break
        x, y, z = y, z, read(int)
    
    print('YES') if peak else print('NO')


if __name__ == "__main__":
    main()
