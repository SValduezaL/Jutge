from yogi import read, scan


def main():
    i = scan(int)
    
    while i != None:
        x = read(int)
        list_x = []
        while x != -1:
            list_x.append(x)   # type: ignore
            x = read(int)
        if i < 1 or i > len(list_x):
            print("Incorrect position.")            
        else:
            print("At the position {} there is a(n) {}.".format(i, list_x[i-1]))   # type: ignore
        
        i = scan(int)


if __name__ == "__main__":
    main()