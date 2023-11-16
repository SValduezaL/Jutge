from yogi import scan


def main() -> None:
    
    n = scan(int)
    position = 1
    
    while n != None and n%2 != 0:
        position += 1
        n = scan(int)
    
    print(position)


if __name__ == "__main__":
    main()
