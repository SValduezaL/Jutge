import numpy as np
from functools import reduce


def evens_product(L):
    evens = []
    evens += [i for i in L if i % 2 == 0]
    evens_product = np.prod(evens)
    return evens_product


def reverse(L):
    L_reversed = reduce(lambda x, y: [y] + x, L, [])
    return L_reversed


def zip_with(f, L1, L2):
    Sol = []
    Sol += f((L1[i] for i in range(len(L1))), (L2[j] for j in range(len(L2))))
    return Sol


def count_if(f, L):
    #    count_f = 0
    #    count_f += 1 for i in L if f
    #    return count_f
    pass


print(evens_product([1, 2, 4, 3]))

print(reverse([1, 2, 3]))

print(zip_with(lambda x, y: x * y, [1, 2, 3], [10, 2]))

print(count_if(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
