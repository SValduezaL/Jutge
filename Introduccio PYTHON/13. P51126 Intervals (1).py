from yogi import read

a1 = read(int)
a2 = read(int)
b1 = read(int)
b2 = read(int)

if b1 > a2:
    print ('[]')
    pass
elif b1 >= a1:
    x = b1
    if b2 >= a2:
        y = a2
    else:
        y = b2
    print (f'[{x},{y}]')
else:
    if b2 < a1:
        print ('[]')
        pass
    else:
        x = a1
        if b2 >= a2:
            y = a2
        else:
            y = b2
        print (f'[{x},{y}]')