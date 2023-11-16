def sum_divisors(x: int) -> int:
    """
    Returns the sum of the divisors of a natural number.
    Prec: 1 <= n <= 1e8.

    """
    sum_divisors = 0
    d = 1
    while d*d < x:
        if x % d == 0:
            sum_divisors += d + x // d
        d += 1
    if d*d == x:
        sum_divisors += d
    
    return sum_divisors

def main() -> None:
    print(sum_divisors(28))
    print(sum_divisors(1))
    print(sum_divisors(100))

if __name__ == "__main__":
    main()
