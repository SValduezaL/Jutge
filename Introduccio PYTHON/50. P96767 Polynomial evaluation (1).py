from yogi import read, scan

def polynomial_evaluation(x: float, c_s: list[float]) -> None:
    ''' Prints the result of the polynomial evaluation:
            p(x) = c0 * x**0 + c1 * x**1 + c2 * x**2 + ... + cn * x**n
        where c0, c1, c2,..., cn are the coefficients of the polynomial.
            Args:
                x (float): The value of x.
                c_s (list[float]): The list of coefficients of the polynomial.
    '''
    res = 0
    for i in range(len(c_s)):
        res += c_s[i] * x ** i
    print ('{:.4f}'.format(res))

def main() -> None:
    x = read(float)
    c_s = list[float]()
    c = scan(float)
    while c!= None:
        c_s.append(c)
        c = scan(float)
        
    polynomial_evaluation(x, c_s)

if __name__ == "__main__":
    main()
