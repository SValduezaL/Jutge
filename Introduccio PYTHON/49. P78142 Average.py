from yogi import scan

def main() -> None:
    number = scan(float)
    sum = 0
    count = 0
    while number!= None:
        sum += number
        count += 1
        number = scan(float)
    print ('{:.2f}'.format(sum / count))

if __name__ == "__main__":
    main()
