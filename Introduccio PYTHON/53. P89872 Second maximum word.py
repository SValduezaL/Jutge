from yogi import read, tokens


def main() -> None:
    
    first = read(str)
    second = str()
    
    for word in tokens(str):
        if word > first:
            first, second = word, first
        elif word < first and word > second:
            second = word
    
    print (second)

if __name__ == "__main__":
    main()