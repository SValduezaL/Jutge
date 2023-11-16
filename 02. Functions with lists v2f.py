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
    return [item for item in L1 if item not in L2]

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
    for i in range(2, h+1):
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