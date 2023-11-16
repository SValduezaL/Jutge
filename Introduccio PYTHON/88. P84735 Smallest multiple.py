from math import ceil
from yogi import scan, read


def main():
    a = scan(int)
    i = 0
    
    while a != None:
        b = read(int)
        i += 1
        m = int(ceil(a/b))
        print("#{} : {}".format(i, m*b))
        a = scan(int)


if __name__ == "__main__":
    main()