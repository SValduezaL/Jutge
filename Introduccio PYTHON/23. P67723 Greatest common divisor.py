from yogi import read

a = read(int)
b = read(int)

a_ini = a
b_ini = b

while a != b:
    if b > a:
        b -= a
    else:
        a -= b

print ('The gcd of {} and {} is {}.'.format(a_ini, b_ini, a))    