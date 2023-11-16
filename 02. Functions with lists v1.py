def myLength(L):
    return len(L)

def myMaximum(L):
    return max(L)

def average(L):
    return sum(L) / len(L)

def buildPalindrome(L):
    L_aux = L.copy()
    L.reverse()
    return L + L_aux

def remove(L1, L2):
    for i in L2:
        while i in L1:
            L1.remove(i)
    return L1

def flatten(L):
    sol = []
    for i in L:
        if isinstance(i,list):
            sol.extend(flatten(i))
        else:
            sol.append(i)
    return sol

def oddsNevens(L):
    odds = []
    evens = []
    for i in L:
        if i % 2 == 0:
            odds.append(i)
        else:
            evens.append(i)
    return evens, odds

def primeDivisors(h):
    sol = []
    for i in range(2, h):
        if h % i == 0:
            if sol == []:
                sol.append(i)
            else:
                isprime = True
                for prime in sol:
                    if i % prime == 0:
                        isprime = False
                        break
                if isprime == True:
                    sol.append(i)
    return sol

print (myLength([1, 3, 6, 1]))
print (myMaximum([4, 3, 1, 5, 4, 5, 2]))
print (myMaximum(['Josep', 'Jordi', 'Alba']))
print (average([1, 2, 3]))
print (buildPalindrome(['pa', 'amb', 'oli']))
print (remove([1, 4, 5, 3, 4, 5, 1, 2, 7, 4, 2], [2, 4]))
print (flatten([[2, 6], [[8, 1, 4], [3, 'uau']], [[], [1]],[[]]]))
print (oddsNevens([1, 4, 5, 3, 4, 5, 1, 2, 7, 4, 2]))
print (primeDivisors(255))