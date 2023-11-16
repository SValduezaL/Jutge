from yogi import read

n = read(int)

number = str(n)

count = 0
for i in number:
    count += 1
print(f'The number of digits of {n} is {count}.')