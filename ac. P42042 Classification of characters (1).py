from yogi import read

letter = read(str)

if letter.isupper():
    print ("uppercase")
else:
    print ('lowercase')

if letter.lower() in ('aeiou'):
    print ('vowel')
else:
    print ('consonant')