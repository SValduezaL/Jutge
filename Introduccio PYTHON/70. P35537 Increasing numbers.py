def is_increasing(n: int) -> bool:
    """ It says if the digits of the number are always equal or increasing.
            Args:
                n (int): Number to be checked.
            Returns:
                True if the number is increasing, False otherwise.
    """
    n_str = str(n)
    
    for i in range(len(n_str)-1):
        if n_str[i+1] < n_str[i]:
            return False
    return True


def main() -> None:
    print(is_increasing(123378))
    print(is_increasing(125433))
    print(is_increasing(7))


if __name__ == "__main__":
    main()
