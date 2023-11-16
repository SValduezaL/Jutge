from yogi import read

h = read(int)
m = read(int)
s = read(int)

s += 1   # Añado un segundo a la hora

if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
            m = 0
            s = 0

print ('{:02d}:{:02d}:{:02d}'.format(h, m, s))