def es_xupiguai(n: int, b:int) -> bool:
    
    if n//b < b:
        return n%b >= b/2 and n//b < b/2
    else:
        return (n%b >= b/2 or not es_xupiguai(n//b, b)) if n%b >= b/2 else (n%b < b/2 and es_xupiguai(n//b, b))


def main():
    print(bool(es_xupiguai(50, 4)))   # True
    print(bool(es_xupiguai(49, 4)))   # False
    print()
    print(bool(es_xupiguai(22, 10)))   # False
    print(bool(es_xupiguai(29, 10)))   # True
    print(bool(es_xupiguai(69, 10)))   # False
    print(bool(es_xupiguai(92, 10)))   # False
    print()
    print(bool(es_xupiguai(119, 4)))   # True
    print(bool(es_xupiguai(47, 4)))   # False
    print()
    # print(True and True)
    print(False and False)
    print(True and False)
    # print(True or True)
    # print(True or False)
    # print(False or False)

if __name__ == "__main__":
    main()
