from yogi import read, scan


def maximum_sums(list: list[int]) -> tuple[int, int]:
    
    sum_beginning = 0
    max_sum_beginning = 0
    for i in range(len(list)):
        sum_beginning += list[i]
        if sum_beginning > max_sum_beginning:
            max_sum_beginning = sum_beginning
    
    sum_end = 0
    max_sum_end = 0
    for i in range(len(list)-1, -1, -1):
        sum_end += list[i]
        if sum_end > max_sum_end:
            max_sum_end = sum_end
    
    return max_sum_beginning, max_sum_end


def main():
    n = scan(int)
    
    while n != None:
        list = []
        for _i in range(n):
            list.append(read(int))   # type: ignore
        print('{} {}'.format(maximum_sums(list)[0], maximum_sums(list)[1]))
        n = scan(int)


if __name__ == "__main__":
    main()
