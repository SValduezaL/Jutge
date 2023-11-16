from yogi import read

temp_Celsius = read(int)

if temp_Celsius > 30:
    print ("it's hot")
    if temp_Celsius >= 100:
        print ('water would boil')
elif temp_Celsius >= 10:
    print ("it's ok")
else:
    print ("it's cold")
    if temp_Celsius <= 0:
        print ('water would freeze')
