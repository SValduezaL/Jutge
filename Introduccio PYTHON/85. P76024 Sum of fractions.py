from yogi import scan


def sum_of_fractions(a: int, b: int, k: int) -> float:
    """
    Returns the sum of the serie of fractions that begins with 1/a and
    continue with 1/(a+k) until a+k > b.
        Args:
            a (int): The denominator of the first fraction.
            b (int): The denominator of the maximum fraction.
            k (int): The step to add to the denominator.
        Preconditions:
            1 <= a <= b
            k >= 1
    """
    sum = float()
    while a <=b:
        sum += 1/a
        a += k
    return sum


def main():
    a, b, k = scan(int), scan(int), scan(int)
    
    while a != None and b != None and k != None:
        print('{:.4f}'.format(sum_of_fractions(a, b, k)))
        a, b, k = scan(int), scan(int), scan(int)


if __name__ == "__main__":
    main()
