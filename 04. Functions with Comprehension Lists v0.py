def my_map(f, L):
    sol = list(map(f, L))
    return print (sol)

def my_filter(f, L):
    sol = list(filter(f, L))
    return print (sol)

def factors(n):
    L = []
    L += [i for i in range(1, n+1) if n % i == 0]
    return print (L)

def triplets(n):
    L = []
    L += ((i, j, k) for i in range(1, n+1) for j in range(1, n+1) for k in range(1, n+1) if i**2 + j**2 == k**2)
    # Otra manera más larga con bucles:
    #     for i in range(1, n+1):
    #         for j in range(1, n+1):
    #             for k in range(1, n+1):
    #                 if i**2 + j**2 == k**2:
    #                     L.append((i, j, k))
    return print(L)