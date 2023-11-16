from yogi import read, scan


def main() -> None:
    n = read(int)
    x = scan(int)
    position = 1
    
    while x != None and position < n:
        position += 1
        x = scan(int)
    
    if n <= 0 or x == None or n > position:
        print("Incorrect position.")
    else:
        print("At the position {} there is a(n) {}.".format(n, x))


if __name__ == "__main__":
    main()
