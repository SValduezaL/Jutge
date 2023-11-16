from yogi import read

a = read(int)
b = read(int)

if b >= a:
    print (a, sep='', end='')
    for i in range(a+1, b+1):
        print (',',i, sep='', end='')
print ()