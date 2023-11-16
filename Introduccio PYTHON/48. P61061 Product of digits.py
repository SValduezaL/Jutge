from yogi import scan

def product_of_digits(n: int) -> None:
    ''' Prints the product of the digits of the number n,
        and then the product of the digits of that number product,
        and so on until the product of the digits it's just a number of one digit.
        It prints also a line with 10 dashes at the end of all the printings.
            Args:
                n (int): The number n.
    '''
    product = 1
    str_number = str(n)
    
    for i in range(len(str_number)):
        product *= int(str_number[i])
    print ('The product of the digits of {} is {}.'.format(n, product))
    if len(str(product)) == 1:
        return print ('----------')
    else:
        return product_of_digits(product)


def main() -> None:
    number = scan(int)
    while number != None:
        product_of_digits(number)
        number = scan(int)


if __name__ == "__main__":
    main()
