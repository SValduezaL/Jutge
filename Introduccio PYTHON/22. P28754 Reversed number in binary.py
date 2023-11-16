from yogi import read

n = read(int)

while n >= 2:
    print (f'{n % 2}', sep='', end='')
    n //= 2
print (f'{n}', sep='')