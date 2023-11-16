def is_prime(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def one_reduction_of_digits(n: int) -> int:
    new_n = int()
    for i in range(len(str(n))):
        new_n += int(str(n)[i])
    return new_n


def is_perfect_prime(n: int) -> bool:
    if n < 10:
        return True if is_prime(n) else False
    if not is_prime(n):
        return False
    else:
        return is_perfect_prime(one_reduction_of_digits(n))