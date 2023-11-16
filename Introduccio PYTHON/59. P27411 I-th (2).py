from yogi import read


def main() -> None:
    n = read(int)
    x = read(int)
    position = 1
    
    while x != -1 and position < n:
        position += 1
        x = read(int)
    
    if n <= 0 or n > position or x == -1:
        print ('Incorrect position.')
    else:
        print ("At the position {} there is a(n) {}.".format(n, x))


if __name__ == "__main__":
    main()