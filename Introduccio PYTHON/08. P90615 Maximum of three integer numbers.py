from yogi import read

a = read(int)
b = read(int)
c = read(int)

if a >= b:
    m = a
else:
    m = b

if m < c:
    m = c

print (m)