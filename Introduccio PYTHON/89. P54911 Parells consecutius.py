from yogi import read


def main():
    
    n = read(int)
    
    for _i in range(n):
        count = 0
        x = read(int)
        while x != -1:
            y = read(int)
            while y != -1:
                z = read(int)
                while z != -1:
                    if y + z < x + y:
                        count += 1
                    x, y = y, z
                    z = read(int)
                y = -1
            x = -1
        print(count)


if __name__ == "__main__":
    main()
