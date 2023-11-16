def max2(a: int, b: int) -> int:
    """Returns the larger of two numbers."""
    return a if a > b else b

def max4(a: int, b: int, c: int, d: int) -> int:
    """Returns the larger of four numbers."""
    return max2(max2(a, b), max2(c, d))


def main() -> None:
    print(max4(10, 20, 5, 8))
    print(max4(0, -2, 15, 15))
    print(max4(-1, -2, -3, -4))


if __name__ == "__main__":
    main()
