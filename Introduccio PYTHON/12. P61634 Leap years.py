from yogi import read

year = read(int)

if (year%4 == 0 and year%100 != 0) or (year%100 == 0 and (year/100)%4 == 0):
    print ('YES')
else:
    print ('NO')    