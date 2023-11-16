from yogi import read

seconds = read(int)

s = seconds
m = 0
h = 0
if s > 59:
    m = s // 60
    s = s % 60
    if m > 59:
        h = m // 60
        m = m % 60

print (h, m , s)