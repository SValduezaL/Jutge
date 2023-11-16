def absValue(x):
    sol = x
    if x < 0:
        sol = sol * -1
    return sol

def power(x,p):
    return x ** p

def isPrime(x):
    if x < 2:
        return False
    for i in range (2, x):
        if x % i == 0:
            return False
    return True

def slowFib(n):
    if n == 0:
        sol = 0
    elif n==1:
        sol = 1
    else:
        sol_aux1 = 0
        sol_aux2 = 1
        for i in range(1, n):
            sol = sol_aux1 + sol_aux2
            sol_aux1 = sol_aux2
            sol_aux2 = sol
    return sol

def quickFib(n):
    if n == 0:
        sol = 0
    elif n==1:
        sol = 1
    else:
        lFib = [0, 1]
        for i in range(1, n):
            lFib = [lFib[1], lFib[1] + lFib[0]]
        sol = lFib[1]
    return sol