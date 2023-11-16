from yogi import read, tokens


def polynomial_evaluation(x: float, c_s: list[float]) -> float:
    polynomial_evaluation = 0
    power = 0
    for c in c_s:
        polynomial_evaluation += c * x**power
        power += 1
    return polynomial_evaluation


def main() -> None:
    x = read(float)
    c_s = list[float]()
    for token in tokens(float):
        c_s.append(token)
        
    print ('{:.4f}'.format(polynomial_evaluation(x, c_s)))


if __name__ == "__main__":
    main()