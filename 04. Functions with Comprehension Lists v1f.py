def my_map(f, L):
    my_map = list(map(f, L))
    return my_map

def my_filter(f, L):
    my_filter = list(filter(f, L))
    return my_filter

def factors(n):
    factors = []
    factors += [i for i in range(1, n+1) if n % i == 0]
    return factors

def triplets(n):
    triplets = []
    triplets += ((i, j, k) for i in range(1, n+1) for j in range(1, n+1) for k in range(1, n+1) if i**2 + j**2 == k**2)
    # Otra manera más larga con bucles:
    #     for i in range(1, n+1):
    #         for j in range(1, n+1):
    #             for k in range(1, n+1):
    #                 if i**2 + j**2 == k**2:
    #                     L.append((i, j, k))
    return triplets