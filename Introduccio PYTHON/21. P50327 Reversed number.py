from yogi import read

n = read(int)

number = str(n)

for i in range(len(number)-1, -1, -1):
    print(f"{number[i]}", sep='', end='')
print ()