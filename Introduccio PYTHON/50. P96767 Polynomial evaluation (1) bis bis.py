from yogi import read, tokens


def main() -> None:
    x = read(float)
    polynomial_evaluation = 0
    power = 0
    for c in tokens(float):
        polynomial_evaluation += c * x**power
        power += 1
    print("{:.4f}".format(polynomial_evaluation))


if __name__ == "__main__":
    main()
