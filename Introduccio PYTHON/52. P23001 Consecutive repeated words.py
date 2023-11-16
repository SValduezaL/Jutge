from yogi import read, scan


def main() -> None:
    
    first_word = read(str)
    count = 1
    max_count = count
    
    word = scan(str)
    while word != None:
        if word == first_word:
            count += 1
            max_count = count if count > max_count else max_count
        else:
            count = 0
        word = scan(str)
    
    print(max_count)


if __name__ == "__main__":
    main()
