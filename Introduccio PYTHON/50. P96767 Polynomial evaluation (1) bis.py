from yogi import read, scan


def main() -> None:
    x = read(float)
    c = scan(float)
    polynomial_evaluation = 0
    power = 0
    while c != None:
        polynomial_evaluation += c * x ** power
        c = scan(float)
        power += 1
    print("{:.4f}".format(polynomial_evaluation))


if __name__ == "__main__":
    main()
