from yogi import read

x = read(int)
y = read(int)

if x <= y:
    for i in range(y, x-1, -1):
        print(i)
else:
    for i in range(x, y-1, -1):
        print(i)