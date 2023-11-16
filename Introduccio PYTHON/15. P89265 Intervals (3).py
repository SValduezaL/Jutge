from yogi import read

a1 = read(int)
b1 = read(int)
a2 = read(int)
b2 = read(int)

if a1 == a2 and b1 == b2:
    print(f'= , [{a1},{b1}]')
elif a1 >= a2 and b1 <= b2:
    print(f'1 , [{a1},{b1}]')
elif a1 <= a2 and b1 >= b2:
    print(f'2 , [{a2},{b2}]')
else:
    if a1 > b2:
        print (f"? , []")
    elif a1 == b2:
        print (f'? , [{b2},{a1}]')
    elif a1 > a2:
        print (f'? , [{a1},{b2}]')
    else:
        if b1 > a2:
            print (f'? , [{a2},{b1}]')
        elif b1 == a2:
            print (f'? , [{b1},{a2}]')
        else:
            print (f'? , []')
